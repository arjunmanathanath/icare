# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapedstories', '0003_seedurldefiner'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapedata',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
