from django.db import models
from notion_app.signals import pre_save_multicast, post_save_multicast


class ExampleModel(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        created = not self.pk

        if not getattr(self._meta, 'auto_created', False):
            pre_save_multicast.send(
                sender=self.__class__,
                instance=self,
                raw=kwargs.get('raw', False),
                using=kwargs.get('using', None),
                update_fields=kwargs.get('update_fields', None),
            )

        super().save(*args, **kwargs)

        if not getattr(self._meta, 'auto_created', False):
            post_save_multicast.send(
                sender=self.__class__,
                instance=self,
                created=created,
                raw=kwargs.get('raw', False),
                using=kwargs.get('using', None),
                update_fields=kwargs.get('update_fields', None),
            )

    def __str__(self):
        return self.name
