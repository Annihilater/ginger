#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 17:36
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : app.py
# from datetime import date
from datetime import date, datetime

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        """
        default 函数式递归调用的，只要遇到不能序列化的对象就会调用 default 函数；
        并且把不能序列化的对象当做 o 传入 default 函数里，让我们来处理。
        :param o: 不能序列化的对象
        :return: 可序列化的对象 or ServerError
        """
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d")
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
