# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hexo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
