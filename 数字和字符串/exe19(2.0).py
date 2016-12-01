# -*- coding: utf-8 -*-
"""键盘输入一个字符串，并且将输入的字符串首字母编程大写，打印输出"""

s = raw_input("please input a str:\n")
if s[0].isalpha():
    print s.capitalize()
else:
    print "字符串首位不是字母，无法大写"

