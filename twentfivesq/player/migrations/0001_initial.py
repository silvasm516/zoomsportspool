# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Street', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('ZipCode', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=10)),
                ('Country', models.CharField(max_length=20)),
                ('UsrName', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=10)),
            ],
        ),
    ]
