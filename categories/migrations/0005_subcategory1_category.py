# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20170329_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory1',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
    ]
