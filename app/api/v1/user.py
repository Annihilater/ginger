#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 18:23
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : user.py
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess, Forbidden
from app.libs.red_print import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = RedPrint('user')


# class QiYue:
#     name = 'qiyue'
#     age = 18
#
#     def __init__(self):
#         self.gender = 'male'
#
#     @staticmethod
#     def keys():
#         return ['name', 'age', 'gender']
#
#     def __getitem__(self, item):
#         return getattr(self, item)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # url = http://localhost:5000/v1/user/<int:uid>
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    # url = http://localhost:5000/v1/user/<int:uid>
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    # url = http://localhost:5000/v1/user
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # url = http://localhost:5000/v1/user
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
