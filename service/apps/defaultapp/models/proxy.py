from django.db import models
from django.db.models import CharField


class Proxy(models.Model):

    ip = CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'proxy'

    def __str__(self):
        return self.ip

    def __unicode__(self):
        return self.ip
