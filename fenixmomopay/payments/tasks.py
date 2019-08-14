# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.schedules import crontab
from celery import app
from .models import MomoRequest
from .views import get_status
from django.db.models import Q
import json
import http.client, urllib.request, urllib.parse


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab('*', '*', '*', '*', '*'),
        update_status())


'''periodically update tasks form collections requests'''
@app.task
def update_status():
    status_value = MomoRequest.objects.get(~Q(status="SUCCESSFUL"))
    referenceid = status_value.externalId
    body = urllib.parse.urlencode({
        "referenceId": referenceid
    })
    status_object = get_status("kjdakjdm", "windows", "jhdas2", body, referenceid)
    json_data = json.loads(status_object)

    new_status = json_data['status']
    status_value.objects.update(status=new_status)
