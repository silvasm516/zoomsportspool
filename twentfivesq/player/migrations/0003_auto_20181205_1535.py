# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20161203_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='Email',
            field=models.EmailField(max_length=20),
        ),
    ]