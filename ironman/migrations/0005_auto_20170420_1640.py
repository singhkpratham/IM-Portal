# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-20 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ironman', '0004_auto_20170417_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionreq',
            options={'ordering': ['-date'], 'verbose_name': 'Requested Session'},
        ),
    ]
