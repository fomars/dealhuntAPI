# coding=utf-8
from collector import redis_queue
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse('collector index')


def savetask(request):
    try:
        items = json.loads(request.body.decode('utf-8', errors='ignore'))['items']
        redis_queue.push(*items)
    except UnicodeDecodeError as e:
        return HttpResponse(str(e), status=400)
    except ValueError as e:
        return HttpResponse(e.message, status=400)
    return HttpResponse('ok')