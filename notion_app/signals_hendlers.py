import logging
from django.dispatch import receiver

from .signals import pre_save_multicast, post_save_multicast
from .models import ExampleModel

logger = logging.getLogger("django")

@receiver(pre_save_multicast, sender=ExampleModel)
def pre_save_handler(sender, instance, **kwargs):
    print(f"Pre-save signal received for instance: {instance}")


@receiver(post_save_multicast, sender=ExampleModel)
def post_save_handler(sender, instance, **kwargs):
    print(f"Post-save signal received for instance: {instance}")

