# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('managerName', models.CharField(max_length=20)),
                ('managerNumber', models.CharField(max_length=12)),
                ('homeTeam', models.CharField(max_length=20)),
                ('visitingTeam', models.CharField(max_length=20)),
                ('dateOriginated', models.DateTimeField()),
                ('gameDate', models.DateTimeField()),
                ('gameType', models.CharField(max_length=3)),
                ('accessNumber', models.CharField(max_length=9)),
                ('gameNumber', models.CharField(max_length=12)),
                ('name1', models.CharField(max_length=12)),
                ('name2', models.CharField(max_length=12)),
                ('name3', models.CharField(max_length=12)),
                ('name4', models.CharField(max_length=12)),
                ('name5', models.CharField(max_length=12)),
                ('name6', models.CharField(max_length=12)),
                ('name7', models.CharField(max_length=12)),
                ('name8', models.CharField(max_length=12)),
                ('name9', models.CharField(max_length=12)),
                ('name10', models.CharField(max_length=12)),
                ('name11', models.CharField(max_length=12)),
                ('name12', models.CharField(max_length=12)),
                ('name13', models.CharField(max_length=12)),
                ('name14', models.CharField(max_length=12)),
                ('name15', models.CharField(max_length=12)),
                ('name16', models.CharField(max_length=12)),
                ('name17', models.CharField(max_length=12)),
                ('name18', models.CharField(max_length=12)),
                ('name19', models.CharField(max_length=12)),
                ('name20', models.CharField(max_length=12)),
                ('name21', models.CharField(max_length=12)),
                ('name22', models.CharField(max_length=12)),
                ('name23', models.CharField(max_length=12)),
                ('name24', models.CharField(max_length=12)),
                ('name25', models.CharField(max_length=12)),
                ('column1', models.IntegerField()),
                ('column2', models.IntegerField()),
                ('column3', models.IntegerField()),
                ('column4', models.IntegerField()),
                ('column5', models.IntegerField()),
                ('column6', models.IntegerField()),
                ('column7', models.IntegerField()),
                ('column8', models.IntegerField()),
                ('column9', models.IntegerField()),
                ('column10', models.IntegerField()),
                ('row1', models.IntegerField()),
                ('row2', models.IntegerField()),
                ('row3', models.IntegerField()),
                ('row4', models.IntegerField()),
                ('row5', models.IntegerField()),
                ('row6', models.IntegerField()),
                ('row7', models.IntegerField()),
                ('row8', models.IntegerField()),
                ('row9', models.IntegerField()),
                ('row10', models.IntegerField()),
            ],
        ),
    ]
