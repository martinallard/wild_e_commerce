# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_newproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
    ]
