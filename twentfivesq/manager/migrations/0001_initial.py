# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Street', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('ZipCode', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=10)),
                ('Country', models.CharField(max_length=20)),
                ('UsrName', models.CharField(max_length=12)),
                ('Email', models.EmailField(max_length=10)),
                ('CardType', models.CharField(max_length=10)),
                ('CardNo', models.CharField(max_length=20)),
                ('PayPal', models.CharField(max_length=20)),
            ],
        ),
    ]
