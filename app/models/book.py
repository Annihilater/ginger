#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/9 13:18
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : book.py
from sqlalchemy import Column, Integer, String, orm

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未知')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    @orm.reconstructor
    def __init__(self):
        super(Book, self).__init__()
        self.fields = [
            'id',
            'title',
            'author',
            'binding',
            'publisher',
            'price',
            'pages',
            'pubdate',
            'isbn',
            'summary',
            'image']
