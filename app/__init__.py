#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 17:34
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : __init__.py.py
from .app import Flask


def register_blueprints(flask_app):
    from app.api.v1 import create_blueprint_v1
    flask_app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugins(flak_app):
    from app.models.base import db
    db.init_app(flak_app)
    db.create_all(app=flak_app)
    # 第二种写法
    # with flak_app.app_context():
    #     db.create_all()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('app.config.setting')
    flask_app.config.from_object('app.config.secure')

    register_blueprints(flask_app)
    register_plugins(flask_app)

    return flask_app
