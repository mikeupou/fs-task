from datetime import datetime
from celery import shared_task
from .models import Subscriber
import logging

logger = logging.getLogger('django')


@shared_task(bind=True)
def get_num_of_new_emails(self):
    today = datetime.now()
    current_month = today.month

    new_emails = Subscriber.objects.filter(subscribed_at__month=current_month).count()

    logger.info(f'>>>>> the number of new emails this month: {new_emails}')