# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='status',
            field=models.CharField(default='Todo', max_length=254),
        ),
    ]
