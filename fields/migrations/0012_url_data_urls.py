# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0011_auto_20170517_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='data_urls',
            field=models.TextField(blank=True),
        ),
    ]
