# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0007_auto_20170130_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='active',
            field=models.CharField(max_length=12, default='1'),
        ),
    ]
