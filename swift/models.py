# coding=UTF-8
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    id = models.CharField(u'编号', max_length=20, primary_key=True)
    name = models.CharField(u'项目名称', max_length=200)
    types = (
      ('C', u'市场'),
      ('N', u'国投'),
      ('P', u'省投'),
      ('A', u'下达'),
    )
    type = models.CharField('项目类型', max_length=2, choices=types)
    start_date = models.DateField(u'签订日期')
    due_date = models.DateField(u'完成日期')
    status = models.CharField('状态', max_length=100, null=True)

    def progress(self):
        return 50

    def __unicode__(self):
        return self.name


class Income(models.Model):
    id = models.CharField(u'编号', max_length=16, primary_key=True)
    name = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    year = models.CharField(u'年度', max_length=4, null=True)
    signing_time = models.DateField(u'签订日期')
    due_time = models.DateField(u'完成日期')
    yesorno=(
            ('Y', '是'),
            ('N', '否'),)
    planned = models.CharField(u'是否计划项目', max_length=2, choices=yesorno)
   #file = models.ForeignKey(
    description = models.CharField(u'详细信息', max_length=200)
    company = models.CharField(u'签订方', max_length=42)
    value = models.DecimalField(u'合同金额', max_digits=20, decimal_places=3)
    other = models.CharField(u'备注', max_length=200, blank=True, null=True)




