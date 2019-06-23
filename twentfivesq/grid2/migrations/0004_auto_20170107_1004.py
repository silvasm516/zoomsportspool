# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0003_auto_20161231_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grid',
            name='gameNumber',
        ),
        migrations.RemoveField(
            model_name='grid',
            name='gameType',
        ),
        migrations.AddField(
            model_name='grid',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
