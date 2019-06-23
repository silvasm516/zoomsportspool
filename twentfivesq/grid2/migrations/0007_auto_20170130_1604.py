# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0006_grid_gametype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='active',
            field=models.CharField(default='Open', max_length=12),
        ),
    ]
