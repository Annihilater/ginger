#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 21:10
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : user.py
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(128))

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def register_by_mobile(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.mobile = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify_by_email(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self.password:
            return False
        return check_password_hash(self.password, raw)

    def verify_by_mobile(self, account, password):
        pass

    def verify_by_mina(self, account, password):
        pass

    def verify_by_wx(self, account, password):
        pass

    def delete(self):
        self.status = 0
