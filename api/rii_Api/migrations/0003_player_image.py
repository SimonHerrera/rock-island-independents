# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rii_Api', '0002_auto_20160912_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ImageField(default='player_images/player_outline.jpg', upload_to='player_images/'),
        ),
    ]