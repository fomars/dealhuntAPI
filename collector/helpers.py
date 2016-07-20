import redis


class RedisQueue(object):
    def __init__(self, host='localhost', port=6379, db=0, password=None, queue_id=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, password=password)
        self.queue_id = queue_id

    def push(self, *items):
        """Push an element to the tail of the queue"""
        return self.client.lpush(self.queue_id, *items)

    def pop(self):
        """Pop an element from the head of the queue"""
        return self.client.rpop(self.queue_id)

    def popall(self):
        pipe = self.client.pipeline()
        responses = pipe.lrange(self.queue_id, 0, -1).delete(self.queue_id).execute()
        return responses[0]


