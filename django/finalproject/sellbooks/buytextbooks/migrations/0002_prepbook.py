# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buytextbooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prepbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prepbooktitle', models.CharField(max_length=250)),
                ('prepbookauthor', models.CharField(max_length=250)),
                ('prepbookpublisher', models.CharField(max_length=250)),
                ('prepbooklocation', models.CharField(max_length=400)),
                ('prepbookimage', models.CharField(max_length=1000)),
            ],
        ),
    ]
