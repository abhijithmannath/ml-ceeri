# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-06 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20170405_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawsession',
            name='session_name',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]
