#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # 邮件配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('mc136782643@gmail.com')
    MAIL_PASSWORD = os.environ.get('lilu136782643!')
    ADMINS = ['mc136782643@gmail.com']#ADMINS配置变量是将接收错误报告的电子邮件地址列表，因此您自己的电子邮件地址应该在该列表中。