#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/9 15:57
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : gift.py
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
