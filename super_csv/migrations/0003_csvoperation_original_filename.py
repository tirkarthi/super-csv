# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-12 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_csv', '0002_csvoperation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvoperation',
            name='original_filename',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
