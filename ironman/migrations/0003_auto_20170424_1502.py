# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ironman', '0002_auto_20170421_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharedoc',
            options={'ordering': ['-time'], 'verbose_name': 'Shared Files'},
        ),
        migrations.AddField(
            model_name='sharedoc',
            name='title',
            field=models.CharField(default='Minutes of Meetings:', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sharedoc',
            name='text',
            field=models.TextField(),
        ),
    ]
