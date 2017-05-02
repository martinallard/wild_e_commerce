# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newproducts',
            name='name',
        ),
        migrations.RemoveField(
            model_name='newproducts',
            name='status',
        ),
        migrations.RemoveField(
            model_name='status',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Status'),
        ),
        migrations.DeleteModel(
            name='NewProducts',
        ),
    ]