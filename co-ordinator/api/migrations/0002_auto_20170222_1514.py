# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-22 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='platform_id',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='platform_ip',
        ),
        migrations.AlterField(
            model_name='deployment',
            name='sensor_id',
            field=models.TextField(unique=True),
        ),
    ]
