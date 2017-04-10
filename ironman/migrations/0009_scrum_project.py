# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-10 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170410_1210'),
        ('ironman', '0008_synthesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrum',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project'),
        ),
    ]
