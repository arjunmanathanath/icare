# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_experience_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templog',
            name='regno',
            field=models.IntegerField(default=0),
        ),
    ]
