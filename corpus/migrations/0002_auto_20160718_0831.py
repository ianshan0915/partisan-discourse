# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='n_vocab',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='n_words',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]