# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swift', '0004_auto_20160809_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='value',
        ),
        migrations.AddField(
            model_name='income',
            name='value',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=20, verbose_name='\u5408\u540c\u91d1\u989d'),
            preserve_default=False,
        ),
    ]
