#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask import Flask

app = Flask(__name__)

from app import routes