from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consentful_messaging.settings')

import django
django.setup()

from django.conf import settings
from celery import Celery

app = Celery('consentful_messaging')
app.config_from_object('django.conf:settings', namespace="CELERY")

# For autodiscover_tasks to work, you must define your tasks in a file called 'tasks.py'.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))