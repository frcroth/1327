# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-16 20:15
from __future__ import unicode_literals

import _1327.documents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_attachment_hash_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporarydocumenttext',
            name='hash_value',
            field=models.CharField(default=_1327.documents.models.TemporaryDocumentText.get_hash, max_length=40, unique=True, verbose_name='Hash value'),
        ),
    ]
