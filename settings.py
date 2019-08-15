#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
from websdk.consts import const

ROOT_DIR = os.path.dirname(__file__)
debug = True
xsrf_cookies = False
expire_seconds = 365 * 24 * 60 * 60
cookie_secret = '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2X6TP1o/Vo='

sign_name = 'CSO客户端监控任务加密认证工具',
template_code = 'CSO_AGENTX_190811',

try:
    from local_settings import *
except:
    pass

settings = dict(
    debug=debug,
    xsrf_cookies=xsrf_cookies,
    cookie_secret=cookie_secret,
    expire_seconds=expire_seconds,
    sign_name=sign_name,
    template_code=template_code,
    app_name='cso_agentx',
    databases={
        const.DEFAULT_DB_KEY: {
            const.DBHOST_KEY: DEFAULT_DB_DBHOST,
            const.DBPORT_KEY: DEFAULT_DB_DBPORT,
            const.DBUSER_KEY: DEFAULT_DB_DBUSER,
            const.DBPWD_KEY: DEFAULT_DB_DBPWD,
            const.DBNAME_KEY: DEFAULT_DB_DBNAME,
        },
    },
    redises={
        const.DEFAULT_RD_KEY: {
            const.RD_HOST_KEY: DEFAULT_REDIS_HOST,
            const.RD_PORT_KEY: DEFAULT_REDIS_PORT,
            const.RD_DB_KEY: DEFAULT_REDIS_DB,
            const.RD_AUTH_KEY: DEFAULT_REDIS_AUTH,
            const.RD_CHARSET_KEY: DEFAULT_REDIS_CHARSET,
            const.RD_PASSWORD_KEY: DEFAULT_REDIS_PASSWORD
        }
    },
    mongodb={
        "mongodb": {
            "host": DEFAULT_MONGO_HOST,
            "port": DEFAULT_MONGO_PORT,
            "username": DEFAULT_MONGO_USER,
            "password": DEFAULT_MONGO_PASS,
            "auth_db": DEFAULT_MONGO_AUTH_DB
        }
    }

)


# Add Django ORM
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agentx.dj_settings")
import django
django.setup()
