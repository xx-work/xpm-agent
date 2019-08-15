# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CronConfig(models.Model):
    cron_second = models.CharField(max_length=10, verbose_name='分', default='*')
    cron_minute = models.CharField(max_length=10, verbose_name='分', default='*')
    cron_hour = models.CharField(max_length=10, verbose_name='时', default='*')
    cron_day = models.CharField(max_length=10, verbose_name='天', default='*')
    cron_month = models.CharField(max_length=10, verbose_name='月', default='*')
    cron_week = models.CharField(max_length=10, verbose_name='周', default='*')
    cron_name = models.CharField(max_length=100, verbose_name='Cron名称', default='every 1 second', unique=True)
    # cron_status = models.SmallIntegerField(verbose_name='任务状态', default=None)

    class Meta:
        db_table = 'opsmanage_cron_config'
        verbose_name = 'Cron配置'


class Crontab:

    def __init__(self, cron):
        self.cron = cron

    def obj(self, save=False):
        cron_minute, cron_hour, cron_day, cron_month, cron_week = self.cron.split()
        cron_name = self.cron
        cron_cfg_obj = CronConfig(**locals())
        if save:
            cron_cfg_obj.save()
        return cron_cfg_obj


class Interval:

    def __init__(self, second=None, minute=None, hour=None):
        self.second = second
        self.minute = minute
        self.hour = hour

    def obj(self, save=False):
        if self.second:
            obj = CronConfig(cron_second="*/{}".format(self.second),
                              cron_name="every {} minute".format(str(self.second)))

        if self.minute:
            obj =  CronConfig(cron_second='0', cron_minute='*/{}',
                              cron_name="every {} minute".format(str(self.minute)))

        if self.hour:
            obj = CronConfig(cron_second='0', cron_minute='0', cron_hour='*/{}',
                              cron_name="every {} hour".format(str(self.hour)))
        else:
            raise AttributeError("Interval类型只支持时分秒的扩展。")

        if save:
            obj.save()

