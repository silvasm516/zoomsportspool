# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_purchases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='GridsPurch',
            field=models.IntegerField(default=0),
        ),
    ]
