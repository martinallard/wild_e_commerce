# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.SubCategory1')),
            ],
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='products',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
