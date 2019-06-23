# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0004_auto_20170107_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='active',
            field=models.BooleanField(default='True'),
        ),
    ]
