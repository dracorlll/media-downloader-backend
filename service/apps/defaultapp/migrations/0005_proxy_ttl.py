# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0004_remove_proxy_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxy',
            name='ttl',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
