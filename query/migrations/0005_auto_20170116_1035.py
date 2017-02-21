# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-16 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_downvote_upvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downvote',
            name='voted_user',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='voted_user',
        ),
        migrations.DeleteModel(
            name='Downvote',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
