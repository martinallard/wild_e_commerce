# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170420_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
