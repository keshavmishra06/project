# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0005_auto_20171101_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
    ]
