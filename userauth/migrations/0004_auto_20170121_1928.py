# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-21 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='', upload_to='uploads/images/'),
        ),
    ]
