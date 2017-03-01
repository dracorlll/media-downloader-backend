# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxy',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 1, 18, 40, 50, 358221, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
