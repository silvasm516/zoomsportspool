# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0008_auto_20170201_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='active',
            field=models.CharField(default='10', max_length=12),
        ),
    ]
