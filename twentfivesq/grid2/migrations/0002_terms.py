# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('MIN', models.CharField(max_length=20)),
                ('MAX', models.CharField(max_length=20)),
                ('PRICE', models.CharField(max_length=50)),
                ('FIRST', models.CharField(max_length=50)),
                ('SECND', models.CharField(max_length=10)),
                ('THIRD', models.CharField(max_length=10)),
                ('FINAL', models.CharField(max_length=20)),
                ('FRTH', models.CharField(max_length=12)),
            ],
        ),
    ]
