#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"