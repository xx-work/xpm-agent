#!/usr/bin/env python
# -*-coding:utf-8-*-

# import sys
# import pymysql
from urllib.parse import quote_plus
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from settings import settings


# def get_db_engine(dbkey):
#     databases = settings.get('databases', 0)
#     db_conf = databases[dbkey]
#     dbuser = db_conf['user']
#     dbpwd = db_conf['pwd']
#     dbhost = db_conf['host']
#     dbport = db_conf.get('port', 0)
#     dbname = db_conf['name']
#     return create_engine('mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8'
#                          .format(user=dbuser, pwd=quote_plus(dbpwd), host=dbhost, port=dbport, dbname=dbname),
#                          logging_name=dbkey, pool_size=20, pool_timeout=90)
#     # logging_name = dbkey, poolclass = NullPool)
#
#     # return None


def get_db_url(dbkey):
    databases = settings.get('databases', 0)
    db_conf = databases[dbkey]
    dbuser = db_conf['user']
    dbpwd = db_conf['pwd']
    dbhost = db_conf['host']
    dbport = db_conf.get('port', 0)
    dbname = db_conf['name']
    url = 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8'.format(
        user=dbuser, pwd=quote_plus(dbpwd), host=dbhost, port=dbport, dbname=dbname)
    return url


def get_mongo_client(dbkey="mongodb"):
    databases = settings.get('mongodb', 0)
    db_conf = databases[dbkey]
    from pymongo import MongoClient
    return MongoClient(
        db_conf["host"],
        username=db_conf["username"],
        password=quote_plus(db_conf["password"]),
        authSource=db_conf["auth_db"],
        authMechanism='SCRAM-SHA-256'
    )


# class DBContext(object):
#     def __init__(self, dbkey):
#         engine = get_db_engine(dbkey)
#         self.__engine = engine
#
#     def __enter__(self):
#         self.__session = sessionmaker(bind=self.__engine)()
#         return self.__session
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.__session.close()
#
#     def get_session(self):
#         return self.__session
