
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
DB = 'wsntest'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[接口监控]'
    FLASKY_MAIL_SENDER = 'Tree <lincf97@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)


config = {
    'dev': DevelopmentConfig,
    'default': DevelopmentConfig
}

jobstores = {
    'default': SQLAlchemyJobStore(url='mysql://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)),
}

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}


