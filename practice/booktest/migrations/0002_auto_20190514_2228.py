# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-14 14:28
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('books', django.db.models.manager.Manager()),
            ],
        ),
    ]
