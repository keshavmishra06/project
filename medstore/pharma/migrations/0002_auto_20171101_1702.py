# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phn_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.Order'),
        ),
    ]
