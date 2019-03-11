#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/6 07:42
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : fake.py.py
# 本文件是一个离线脚本用来创建测试数据
from app import create_app
from app.models.base import db
from app.models.user import User

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        with db.auto_commit():
            # 创建一个超级管理员
            user = User()
            user.nickname = 'Super'
            user.email = 'super@qq.com'
            user.password = '00000000'
            user.auth = 2
            db.session.add(user)
