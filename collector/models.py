from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    avito_id = models.IntegerField()
    avito_unix_time = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone_checked_unixtime = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class DealhuntRouter(object):
    """
    A router to control all database operations on models in the
    collector application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'item':
            return 'dealhunt'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'item':
            return 'dealhunt'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None