import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tester.settings')
app = Celery('tester')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'UTC'
 
app.conf.beat_schedule = {
    "add_first": {
        "task": "run.tasks.speed",
        "schedule": timedelta(minutes=2),
    },
}
 
app.autodiscover_tasks()