#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/6 19:35
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : 1.py
# 本文件可以获取 sqlalchemy 模型对象的下的所有字段
from sqlalchemy.inspection import inspect

from app.models.user import User

a = inspect(User).primary_key[0].name

inspect_user = inspect(User)
inspect_user_list = list(inspect_user._all_tables)
print(inspect_user_list[0]._columns)

columns = inspect(User).columns

print(a)
print(columns)
print(columns.keys())
print(list(columns))

for item in list(columns):
    print(item)

print(set(columns))
for i in set(columns):
    print(i)
