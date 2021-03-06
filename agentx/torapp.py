#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : actanble
date   : 2017-10-11
role   : Application
"""

from websdk.application import Application as myApplication
from handlers.snmp_handler import snmpd_urls
from handlers.cron_handler import cron_urls
from handlers.task_log_handle import task_log_urls


class Application(myApplication):

    def __init__(self, **settings):
        # self.inital_fun(**settings)
        urls = []
        urls.extend(snmpd_urls)
        urls.extend(cron_urls)
        urls.extend(task_log_urls)

        super(Application, self).__init__(urls, **settings)


if __name__ == '__main__':
    pass
