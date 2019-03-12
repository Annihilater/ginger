#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 20:28
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : client.py
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.red_print import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm, UserMobileForm

api = RedPrint("client")


@api.route("/register", methods=["POST"])
def create_client():
    # url = http://localhost:5000/v1/client/register
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_by_email,
        ClientTypeEnum.USER_MOBILE: __register_by_mobile,
        ClientTypeEnum.USER_MINA: __register_by_mina,
        ClientTypeEnum.USER_WX: __register_by_wx,
    }
    promise[form.type.data]()
    return Success()


def __register_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


def __register_by_mobile():
    form = UserMobileForm().validate_for_api()
    User.register_by_mobile(form.nickname.data, form.account.data, form.secret.data)


def __register_by_mina():
    pass


def __register_by_wx():
    pass
