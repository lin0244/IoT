# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-17 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sensor_id', models.TextField()),
                ('sensor_ip', models.TextField()),
                ('sensor_config_path', models.TextField()),
                ('platform_id', models.TextField(default='')),
                ('platform_ip', models.TextField(default='')),
            ],
        ),
    ]
