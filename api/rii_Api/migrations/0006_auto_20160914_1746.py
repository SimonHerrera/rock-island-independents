# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rii_Api', '0005_auto_20160913_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playerBio',
            field=models.TextField(default='There is no Game summary yet for this game.', max_length=2000),
        ),
    ]
