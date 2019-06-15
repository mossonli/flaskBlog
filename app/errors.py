#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask import render_template
from app import app, db


"""
要声明自定义错误处理程序，请使用@errorhandler装饰器。
我将把我的错误处理程序放在一个新的app / errors.py模块中
"""

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500