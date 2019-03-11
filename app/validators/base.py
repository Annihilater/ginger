#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/1 15:44
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : base.py
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(self.errors)
        return self
