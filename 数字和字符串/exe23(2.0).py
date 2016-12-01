# -*- coding: utf-8 -*-
"""
键盘输入一个整数，比如2016，然后显示，每个数字占据一行，如下：
        2
        0
        1
        6
"""

num = raw_input("please input an integer:")
while 1:
    if not num.isdigit():
        num = raw_input("please input an integer again:")
    else:
        break

for i in num:
    print i

#建议同前，用户输入的如果不是数字，是否处理？