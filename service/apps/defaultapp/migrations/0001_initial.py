# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(unique=True, max_length=15)),
                ('port', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'proxy',
            },
        ),
    ]
