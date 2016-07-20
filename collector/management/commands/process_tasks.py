import json

from collector import redis_queue
from collector.models import Item
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'retrieves items from queue and stores the new ones in db'

    def handle(self, *args, **options):
        items = [json.loads(i) for i in redis_queue.popall()]
        avito_ids = [i['avitoid'] for i in items]
        old_ids = Item.filter_present(avito_ids)
        Item.objects.bulk_create(
            [Item(title=i['title'], price=i['price'], image=i['img'], avito_id = i['avitoid'])
             for i in items if int(i['avitoid']) not in old_ids]
        )


        # '{u\\'avitoid\\': u\\'808850880\\', u\\'price\\': u\\'1500\\', u\\'datetime\\': 1468494120, u\\'img\\': u\\'03.img.avito.st/140x105/2819294403.jpg\\', u\\'title\\': u\\'Continental sport contact\\'}'