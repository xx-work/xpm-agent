#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author  : actanble
Date    : 2019/3/20
Desc    :
"""
from libs.base_handler import BaseHandler
from tornado.web import RequestHandler, HTTPError


class ManageSnmpCfg(BaseHandler):

    def get(self, uniq_flag, **kwargs):
        """
        针对部件的标号 对SNMP
        :param uniq_flag:
        :param kwargs:
        :return:
        """
        return self.write(dict(code=-1, msg='此方法暂无'))


# 获取当前部件SNMP数据
class GetCurrentSnmpDataHandle(BaseHandler):

    def get(self, uniq_flag, **kwargs):
        """
        针对部件的标号 对SNMP
        :param uniq_flag:
        :param kwargs:
        :return:
        """
        return self.write(dict(code=-1, msg='此方法暂无'))


class SnmpCfgModify(BaseHandler):
    pass


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


class Test4(RequestHandler):

    def get(self, *args, **kwargs):
        from opssdk.operate.mail import Mail
        Mail(mail_user="xz_ops_mail", mail_pass="actanble1", ).send_mail(to_list='2970090120@qq.com,180573956@qq.com',
                                                                         header='无尘', sub='test000011',
                                                                         content="<div>?????</div>")
        self.write(dict(code=-1, msg='send OK'))

    def post(self, *args, **kwargs):
        from opssdk.operate.mail import Mail
        Mail(mail_user="actanble", mail_pass="string123",).send_mail(to_list='2970090120@qq.com,180573956@qq.com,admin@actanble.com',
                                                                        header='无尘', sub='test000011',
                                                                        content="<div>?????</div>")
        self.write(dict(code=0, msg='send OK'))


class Test5(RequestHandler):

    def get(self, *args, **kwargs):
        task_name = self.get_argument('task_name', default='print5', strip=True)
        args = self.get_argument('args', default='11112233', strip=True)

        from agentx import tasks
        txt = getattr(tasks, task_name)(args)
        print(txt)

        self.write(dict(code=0, msg=txt))




snmpd_urls = [
    (r'/cop/snmp_cfg/(.*)', GetSnmpData),
    (r"/2", Test2),
    (r"/3", Test3),
    (r"/4", Test4),
    (r"/5", Test5),
]


if __name__ == "__main__":
    pass
