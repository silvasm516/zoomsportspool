# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20180604_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='GridsOut',
            field=models.IntegerField(default=0),
        ),
    ]
