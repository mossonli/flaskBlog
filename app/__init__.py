#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' # flask-login 指定处理登录的视图函数是谁  login函数

from app import routes,models