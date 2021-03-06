#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 20:41
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : enums.py
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
