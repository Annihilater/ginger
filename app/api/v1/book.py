#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 18:23
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : book.py
from flask import jsonify
from sqlalchemy import or_

from app.libs.red_print import RedPrint
from app.models.book import Book
from app.validators.forms import BookSearchForm

api = RedPrint("book")


@api.route("/search", methods=["GET"])
def search():
    # url = http://localhost:5000/v1/book/search?q={}
    form = BookSearchForm().validate_for_api()
    q = "%" + form.q.data + "%"
    books = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide("summary") for book in books]
    return jsonify(books)


@api.route("/<int:isbn>/detail", methods=["GET"])
def detail(isbn):
    # url = http://localhost:5000/v1/book/<int:isbn>/detail
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)


@api.route("", methods=["GET"])
def get_book():
    # url = http://localhost:5000/v1/book/
    return "get book"


@api.route("", methods=["POST"])
def create_book():
    # url = http://localhost:5000/v1/book/
    return "create book"
