# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phin', '0009_auto_20170420_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetinteraction',
            name='first_target',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='as_first', to='phin.Target'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='targetinteraction',
            name='molecule',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='phin.Molecule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='targetinteraction',
            name='second_target',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='as_second', to='phin.Target'),
            preserve_default=False,
        ),
    ]
