import time

from celery import shared_task

@shared_task
def get_url(data):
    time.sleep(10)
    return data['url']