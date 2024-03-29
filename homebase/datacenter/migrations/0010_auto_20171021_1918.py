# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-21 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0009_auto_20171021_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='url_extra',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='kind',
            field=models.CharField(choices=[('IT-project', 'IT-project'), ('gallery', 'gallery'), ('external-link', 'external-link'), ('folder', 'folder'), ('wiki', 'wiki'), ('docs', 'docs'), ('restricted', 'restricted')], default='folder', max_length=30),
        ),
    ]
