#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    print('sqlite://' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False