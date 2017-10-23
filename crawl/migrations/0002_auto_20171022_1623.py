# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('block_hash', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
