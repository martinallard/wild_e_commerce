# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20170427_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='status.Status'),
        ),
        migrations.DeleteModel(
            name='status',
        ),
    ]
