# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rii_Api', '0012_player_imageinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='imageInfo',
            field=models.CharField(default='There is no image available of this player', max_length=90),
        ),
    ]
