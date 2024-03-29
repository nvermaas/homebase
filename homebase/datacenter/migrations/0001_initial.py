# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-14 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('long', models.CharField(max_length=40)),
                ('date', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('kind', models.CharField(choices=[('person', 'Image'), ('object', 'Movie'), ('other', 'Other')], default='person', max_length=30)),
                ('url', models.URLField(blank=True, default='', max_length=250)),
                ('visible', models.IntegerField(default=1)),
            ],
        ),
    ]
