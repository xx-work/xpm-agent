#!/usr/bin/env python
# -*-coding:utf-8-*-

import shortuuid
from .cache import get_cache
from tornado.web import RequestHandler, HTTPError
# from .jwt_token import AuthToken
import jwt


class BaseHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        self.new_csrf_key = str(shortuuid.uuid())
        self.user_id, self.username, self.nickname, self.email, self.is_super = None, None, None, None, False
        self.is_superuser = self.is_super

        super(BaseHandler, self).__init__(*args, **kwargs)

    def prepare(self):

        # 验证客户端CSRF，如请求为GET，则不验证，否则验证。最后将写入新的key
        cache = get_cache()
        if self.request.method not in ("GET", "HEAD", "OPTIONS"):
            csrf_key = self.get_cookie('csrf_key')
            pipeline = cache.get_pipeline()
            result = cache.get(csrf_key, private=False, pipeline=pipeline)
            cache.delete(csrf_key, private=False, pipeline=pipeline)
            if result != '1':
                raise HTTPError(402, 'csrf error')

        cache.set(self.new_csrf_key, 1, expire=1800, private=False)
        self.set_cookie('csrf_key', self.new_csrf_key)

        # 登陆验证
        auth_key = self.get_cookie('auth_key', None)
        if not auth_key:
            if "Authorization" in self.request.headers.keys():
                if self.request.headers["Authorization"].startwith('JWT'):
                    auth_key = self.request.headers["Authorization"].split()[1]
                    print(auth_key)

        if not auth_key:
            url_auth_key = self.get_argument('auth_key', default=None, strip=True)
            if url_auth_key:
                auth_key = bytes(url_auth_key, encoding='utf-8')

        if not auth_key:
            raise HTTPError(401, 'auth failed')
        else:
            # user_info = AuthToken().decode_auth_token(auth_key)
            user_info = jwt.decode(auth_key, verify=False).get('data')
            if not user_info:
                raise HTTPError(401, 'auth failed')

            self.user_id = user_info.get('user_id', None)
            self.username = user_info.get('username', None)
            self.nickname = user_info.get('nickname', None)
            self.email = user_info.get('email', None)
            self.is_super = user_info.get('is_superuser', False)

            if not self.user_id:
                raise HTTPError(401, 'auth failed')
            else:
                self.user_id = str(self.user_id)
                self.set_secure_cookie("user_id", self.user_id)
                self.set_secure_cookie("nickname", self.nickname)
                self.set_secure_cookie("username",  self.username)
                self.set_secure_cookie("email", str(self.email))
        self.is_superuser = self.is_super

    def get_current_user(self):
        return self.username

    def get_current_id(self):
        return self.user_id

    def get_current_nickname(self):
        return self.nickname

    def get_current_email(self):
        return self.email

    def is_superuser(self):
        return self.is_superuser

    # def write_error(self, status_code, **kwargs):
    #     if status_code == 404:
    #         self.set_status(status_code)
    #         return self.finish('找不到相关路径-404')
    #
    #     elif status_code == 400:
    #         self.set_status(status_code)
    #         return self.finish('错误请求')
    #
    #     elif status_code == 402:
    #         self.set_status(status_code)
    #         return self.finish('CSRF错误')
    #
    #     elif status_code == 403:
    #         self.set_status(status_code)
    #         return self.finish('访问阻断')
    #
    #     elif status_code == 500:
    #         self.set_status(status_code)
    #         return self.finish('服务器内部错误')
    #
    #     elif status_code == 401:
    #         self.set_status(status_code)
    #         return self.finish('登录验证失败')
    #
    #     else:
    #         self.set_status(status_code)


class LivenessProbe(RequestHandler):

    def head(self, *args, **kwargs):
        self.write("I'm OK")

    def get(self, *args, **kwargs):
        self.write("I'm OK")
