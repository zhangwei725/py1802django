# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-29 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model03', '0002_auto_20180528_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.ManyToManyField(to='model03.Room'),
        ),
    ]