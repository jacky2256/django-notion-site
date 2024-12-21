from celery import shared_task
import logging

logger = logging.getLogger("django")

@shared_task
def multicast_signal_task(signal_name, sender_name, instance_id):
    try:
        logger.info(f"[Celery Task] Signal: {signal_name}, Sender: {sender_name}, Instance ID: {instance_id}")
    except Exception as err:
        logger.error(f"{err}")
