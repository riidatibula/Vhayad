# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vahay', '0012_auto_20170716_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='vahay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vahay.Vahay'),
        ),
    ]
