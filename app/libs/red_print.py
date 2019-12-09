#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/12/14 18:45
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : red_print.py


class RedPrint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + "+" + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
