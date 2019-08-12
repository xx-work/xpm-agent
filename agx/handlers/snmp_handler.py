#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author  : actanble
Date    : 2019/3/20
Desc    :
"""
from libs.base_handler import BaseHandler


class SnmpData(BaseHandler):

    def get(self, *args, **kwargs):
        return self.write(dict(code=-1, msg='此方法暂无'))


snmpd_urls = [
    (r"/snmpd/get_data", SnmpData),
]

if __name__ == "__main__":
    pass
