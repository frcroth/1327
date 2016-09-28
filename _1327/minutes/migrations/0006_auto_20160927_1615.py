# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0005_remove_minutesdocument_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutesdocument',
            name='state',
            field=models.IntegerField(choices=[(0, 'Unpublished'), (1, 'Published for Students and University Network'), (2, 'Internal'), (3, 'Custom'), (4, 'Published for Student only')], default=0, verbose_name='State'),
        ),
    ]