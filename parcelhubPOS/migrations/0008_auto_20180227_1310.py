# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-27 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0007_auto_20180227_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='zone_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ZoneType', verbose_name='Zone type'),
        ),
    ]
