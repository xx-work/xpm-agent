#!/usr/bin/env python
# -*-coding:utf-8-*-
import fire
from tornado.options import define
from websdk.program import MainProgram
from settings import settings as app_settings
from agx.applications import Application as TaskApp
# from agx.other_app import Application as OtherApp
# from agx.cron_app import Application as CronApp
# from agx.program import Application as DealApp
# from agx.subscribe import RedisSubscriber as SubApp


define("service", default='api', help="start service flag", type=str)


class MyProgram(MainProgram):
    def __init__(self, service='task_api', progress_id='task'):
        self.__app = None
        settings = app_settings
        if service == 'task_api':
            self.__app = TaskApp(**settings)
        # elif service == 'exec_task':
        #     self.__app = DealApp(**settings)
        # elif service == 'log_record':
        #     self.__app = SubApp(**settings)
        # elif service == 'cron_app':
        #     self.__app = CronApp(**settings)
        # elif service == 'other':
        #     # 日志查看、报警 定时获取, 任务提交
        #     self.__app = OtherApp(**settings)
        super(MyProgram, self).__init__(progress_id)
        self.__app.start_server()


if __name__ == '__main__':
    fire.Fire(MyProgram)
