#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/7 11:19
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : scope.py


class Scope:
    allow_api = []
    allow_module = []
    forbidden_api = []

    def __add__(self, other):
        self.allow_api += other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module += other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden_api += other.forbidden_api
        self.forbidden_api = list(set(self.forbidden_api))
        return self


class UserScope(Scope):
    allow_api = ["v1.user+get_user", "v1.user+delete_user"]

    def __init__(self):
        self + Scope()


class AdminScope(Scope):
    allow_module = ["v1.user"]

    def __init__(self):
        self + UserScope()


class SuperScope(Scope):
    allow_api = [3]

    def __init__(self):
        self + AdminScope + UserScope


def is_in_scope(scope, endpoint):
    scope = globals()[scope]
    red_name = endpoint.split("+")[0]

    if endpoint in scope.forbidden_api:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True

    return False
