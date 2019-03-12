#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/9 16:03
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : gift.py
from flask import g

from app.libs.error_code import DuplicateGift, Success
from app.libs.red_print import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.book import Book
from app.models.gift import Gift

api = RedPrint("gift")


@api.route("/<int:isbn>", methods=["POST"])
@auth.login_required
def create(isbn):
    # url = http://localhost:5000/v1/gift/<int:isbn>
    uid = g.user.uid
    with db.auto_commit():
        Book.query.filter_by(isbn=isbn).first_or_404()
        gift = Gift.query.filter_by(isbn=isbn, uid=uid).first_or_404()
        if gift:
            raise DuplicateGift()
        gift = Gift()
        gift.isbn = isbn
        gift.uid = uid
        db.session.add(gift)
    return Success()
