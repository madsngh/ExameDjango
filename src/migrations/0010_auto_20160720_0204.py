# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_auto_20160719_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeuserans',
            name='id',
        ),
        migrations.AlterField(
            model_name='storeuserans',
            name='ques_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
