# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 02:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180912_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='ctest',
        ),
    ]
