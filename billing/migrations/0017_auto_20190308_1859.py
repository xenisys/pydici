# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-08 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0016_auto_20190303_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientbill',
            name='previous_year_bill',
        ),
        migrations.RemoveField(
            model_name='supplierbill',
            name='previous_year_bill',
        ),
    ]
