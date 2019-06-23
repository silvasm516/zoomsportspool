# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid2', '0009_auto_20170208_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='NOTES',
            field=models.CharField(default='NONE', max_length=300),
            preserve_default=False,
        ),
    ]
