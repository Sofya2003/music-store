import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicbackend.settings')

app = Celery('musicbackend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'send_report': {
        'task': 'musicbackend.tasks.send_report',
        'schedule': crontab(minute='*/15')
    },
    "get_cache": {
        'task': 'instruments.tasks.get_cache',
        "schedule": crontab(minute="*/1"),
    }
}



# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')