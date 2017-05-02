# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20170426_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='status',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]