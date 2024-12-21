from django.dispatch import Signal
from functools import partial
from core.task import multicast_signal_task

class MulticastSignal(Signal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def _lazy_method(self, method, apps, receiver, sender, **kwargs):
        from django.db.models.options import Options
        from django.db.models.utils import make_model_tuple

        partial_method = partial(method, receiver, **kwargs)
        if isinstance(sender, str):
            apps = apps or Options.default_apps
            apps.lazy_model_operation(partial_method, make_model_tuple(sender))
        else:
            return partial_method(sender)

    def connect(self, receiver, sender=None, weak=True, dispatch_uid=None, apps=None):
        def wrapped_receiver(sender, **kwargs):
            receiver(sender, **kwargs)
            instance = kwargs.get('instance')
            if instance is not None:
                multicast_signal_task.apply_async(
                    args=(self.name, sender.__name__, instance.pk),
                    queue='broadcast_tasks'
                )

        self._lazy_method(
            super().connect,
            apps,
            wrapped_receiver,
            sender,
            weak=weak,
            dispatch_uid=dispatch_uid,
        )

    def disconnect(self, receiver=None, sender=None, dispatch_uid=None, apps=None):
        return self._lazy_method(
            super().disconnect, apps, receiver, sender, dispatch_uid=dispatch_uid
        )


class PreSaveMulticastSignal(MulticastSignal):
    def __init__(self):
        super().__init__("pre_save_multicast")


class PostSaveMulticastSignal(MulticastSignal):
    def __init__(self):
        super().__init__("post_save_multicast")


pre_save_multicast = PreSaveMulticastSignal()
post_save_multicast = PostSaveMulticastSignal()
