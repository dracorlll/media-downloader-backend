from django.db import models
from django.db.models import BooleanField, CharField


class Proxy(models.Model):

    ip = CharField(max_length=15, unique=True)
    port = CharField(max_length=5)
    country = CharField(max_length=5)

    class Meta:
        db_table = 'proxy'

    def __str__(self):
        return self.ip + ':' + self.port

    def __unicode__(self):
        return self.ip + ':' + self.port
