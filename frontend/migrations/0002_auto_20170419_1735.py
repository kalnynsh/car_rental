# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_phone_number',
            field=models.CharField(max_length=100),
        ),
    ]
