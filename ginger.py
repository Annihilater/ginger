#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 16:21
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : ginger.py
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if app.config["DEBUG"]:
            raise e
        else:
            return ServerError()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6000, debug=True)
