#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author  : actanble
Date    : 2019/3/20
Desc    :
"""
from libs.base_handler import BaseHandler
from tornado.web import RequestHandler, HTTPError


class SnmpData(BaseHandler):

    def get(self, *args, **kwargs):
        return self.write(dict(code=-1, msg='此方法暂无'))


class Test2(RequestHandler):

    def get(self, *args, **kwargs):
        from agentx.app.models import ChangeAudit
        ChangeAudit.objects.create(opreate_username='ccc')

        return self.write(dict(code=-1, msg='222222222'))


class Test3(RequestHandler):

    def get(self, *args, **kwargs):
        from opssdk.operate.sync_query import DjangoSqlConn
        res = yield DjangoSqlConn.fetch('select * from django_migrations;')
        print(res)
        self.write(dict(code=-1, msg='3333333333'))


snmpd_urls = [
    (r"/test1", SnmpData),
    (r"/2", Test2),
    (r"/3", Test3),
]

if __name__ == "__main__":
    pass
