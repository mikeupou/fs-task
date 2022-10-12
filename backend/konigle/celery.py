from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'konigle.settings')

app = Celery('konigle')

# Run in separate terminals under backend dir | CELERY TASK
# celery -A konigle worker --loglevel=info -P solo
# celery -A konigle beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    # Executes every Monday and Wednesday morning at 8:30 a.m.
    'count_new_email_task': {
        'task': 'unity.tasks.get_num_of_new_emails',
        'schedule': crontab(hour=8, minute=30, day_of_week=[1, 3]),
        # 'schedule': crontab(),
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

