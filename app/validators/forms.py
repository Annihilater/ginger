#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 20:44
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : forms.py
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(
        validators=[DataRequired(message="不允许为空"), length(min=8, max=32)]
    )
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        """
        这里自定义的验证器方法名必须为 'validate_' + 字段名(类变量)
        因为 flask 内部设定的，只有这样写才会触发该自定义的验证器验证
        :param value: type 传入的具体字段，是 flask 调用验证器的时候自动传入的
        :return: 如果在自定义的验证器内抛出异常则表示验证失败；不抛出异常，则表示验证成功(暂时是这么理解的)
        """
        from app.libs.enums import ClientTypeEnum

        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message="invalidate email")])
    secret = StringField(
        validators=[DataRequired(), Regexp(r"^[A-Za-z0-9_*&$#@]{6,22}$")]
    )
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError


class UserMobileForm(ClientForm):
    account = IntegerField(
        validators=[DataRequired(message="不允许为空"), length(min=11, max=11)]
    )
    secret = StringField(
        validators=[DataRequired(), Regexp(r"^[A-Za-z0-9_*&$#@]{6,22}$")]
    )
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(mobile=value.data).first():
            raise ValidationError


class BookSearchForm(Form):
    q = StringField(validators=[DataRequired()])


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])
