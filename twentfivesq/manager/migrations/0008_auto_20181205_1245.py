# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20181205_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='DollarPurch',
            field=models.FloatField(default=0, max_length=20),
        ),
    ]
