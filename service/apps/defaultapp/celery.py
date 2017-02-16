from __future__ import absolute_import, unicode_literals
from celery import Celery

# app = Celery(str('apps'), broker='amqp://guest:guest@localhost:5672//',
#              backend='amqp://guest:guest@localhost:5672//',)
app = Celery(str('apps'))
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


