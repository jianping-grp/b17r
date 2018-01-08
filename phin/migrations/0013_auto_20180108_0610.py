# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 06:10
from __future__ import unicode_literals

from django.db import migrations
import django_rdkit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phin', '0012_auto_20180105_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='molecule',
            name='mfp2',
            field=django_rdkit.models.fields.BfpField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='scaffold',
            name='mfp2',
            field=django_rdkit.models.fields.BfpField(db_index=True, null=True),
        ),
    ]
