# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-08 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0015_auto_20180104_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_date',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='createtimestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='*Invoice datetime'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Height(cm)'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Length(cm)'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Width(cm)'),
        ),
    ]
