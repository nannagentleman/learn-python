# -*- coding: utf-8 -*-
"""
用raw_input()函数获得输入的字符串：what’s your name，并且把输入的内容打印出来，要求打印的结果如同：
what’s
your
name
"""

s = raw_input("input your str:\n")

for i in s.split():
    print i