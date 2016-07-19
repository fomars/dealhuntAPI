from collector.helpers import RedisQueue
from django.conf import settings


redis_queue = RedisQueue(host=settings.REDIS_HOST, port=settings.REDIS_PORT, queue_id=settings.QUEUE_ID)