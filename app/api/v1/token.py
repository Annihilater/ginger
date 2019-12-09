#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/2 18:03
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : token.py
import time

from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.red_print import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm, TokenForm
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired,
)

api = RedPrint("token")


@api.route("", methods=["POST"])
def get_token():
    # url = http://localhost:5000/v1/token
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify_by_email,
        ClientTypeEnum.USER_MOBILE: User.verify_by_mobile,
        ClientTypeEnum.USER_MINA: User.verify_by_mina,
        ClientTypeEnum.USER_WX: User.verify_by_wx,
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data, form.secret.data
    )
    expiration = current_app.config["TOKEN_EXPIRATION"]
    token = generate_auth_token(
        identity["uid"], form.type.data, identity["scope"], expiration
    )
    t = {"token": token.decode("ascii")}
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
    return s.dumps({"uid": uid, "type": ac_type.value, "scope": scope})


@api.route("/secret", methods=["POST"])
def get_token_info():
    # url = http://localhost:5000/v1/secret
    form = TokenForm().validate_for_api()
    token = form.token.data
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(token, return_header=True)
    except BadSignature:
        raise AuthFailed(msg="token is invalid", error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg="token is expired", error_code=1003)

    create_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data[1]["iat"]))
    expire_in = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data[1]["exp"]))
    r = {
        "uid": data[0]["uid"],
        "scope": data[0]["scope"],
        "create_at": create_at,
        "expire_in": expire_in,
    }
    return jsonify(r)
