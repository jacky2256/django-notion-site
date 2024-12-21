import logging

from celery import Celery
from kombu.common import Broadcast
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True

app.conf.task_queues = (
    Broadcast('broadcast_tasks'),
)


app.conf.task_routes = {
    'core.task.multicast_signal_task': {
        'queue': 'broadcast_tasks',
        'exchange': 'broadcast_tasks'
    }
}

app.autodiscover_tasks()

logging.getLogger('celery.worker').setLevel(logging.WARNING)
logging.getLogger('celery.app.trace').setLevel(logging.WARNING)