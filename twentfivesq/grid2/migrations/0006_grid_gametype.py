# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0005_auto_20170107_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='gameType',
            field=models.CharField(max_length=3, default='p'),
            preserve_default=False,
        ),
    ]
