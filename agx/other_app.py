#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : actanble
date   : 2019-03-19
role   : Application 非核功能
"""

import tornado
from websdk.application import Application as myApplication
from agx.handlers.task_log_handler import tail_data, get_log_data
from agx.handlers.task_log_handler import task_log_urls
#
from agx.handlers.asset_info_handler import asset_info_urls
from agx.handlers.task_submission_handler import opt_info_urls
from agx.handlers.other_handler import other_urls


class Application(myApplication):
    def __init__(self, **settings):
        urls = []
        urls.extend(task_log_urls)
        tailed_callback = tornado.ioloop.PeriodicCallback(tail_data, 500)
        tailed_callback.start()
        get_log_callback = tornado.ioloop.PeriodicCallback(get_log_data, 1000)
        get_log_callback.start()
        # 
        urls.extend(asset_info_urls)
        urls.extend(opt_info_urls)
        urls.extend(other_urls)
        super(Application, self).__init__(urls, **settings)


if __name__ == '__main__':
    pass
