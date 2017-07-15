# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vahay', '0003_auto_20170715_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='account_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vahay',
            name='account_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vahay',
            name='email',
            field=models.CharField(default='example@email.com', max_length=500),
        ),
    ]