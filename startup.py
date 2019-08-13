#!/usr/bin/env python
# -*-coding:utf-8-*-
import fire
from tornado.options import define
from websdk.program import MainProgram
from settings import settings as app_settings
from agentx.torapp import Application as TaskApp

define("service", default='api', help="start service flag", type=str)


class MyProgram(MainProgram):
    def __init__(self, service='task_api', progress_id='task'):
        self.__app = None
        settings = app_settings
        if service == 'web':
            self.__app = TaskApp(**settings)
        super(MyProgram, self).__init__(progress_id)
        self.__app.start_server()


if __name__ == '__main__':
    fire.Fire(MyProgram)
