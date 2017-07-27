# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0002_proxy_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxy',
            name='country',
        ),
        migrations.RemoveField(
            model_name='proxy',
            name='timestamp',
        ),
    ]
