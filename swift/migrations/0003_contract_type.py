# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swift', '0002_auto_20160807_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='type',
            field=models.CharField(choices=[('I', '\u6536\u6b3e\u5408\u540c'), ('O', '\u4ed8\u6b3e\u5408\u540c'), ('P', '\u91c7\u8d2d\u5408\u540c'), ('A', '\u8ba1\u5212\u5408\u540c')], default='I', max_length=2, verbose_name='\u9879\u76ee\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]