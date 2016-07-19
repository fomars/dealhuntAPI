# coding=utf-8
from collector.tasks import get_url
from django.http import HttpResponse
import json

def index(request):
    return HttpResponse('collector index')


def push_data_to_queue(data):
    pass


def savetask(request):
    try:
        data = json.loads(request.body.decode('utf-8', errors='ignore'))
        get_url.delay(data)
    except UnicodeDecodeError as e:
        return HttpResponse(str(e), status=400)
    except ValueError as e:
        return HttpResponse(e.message, status=400)
    return HttpResponse('ok')