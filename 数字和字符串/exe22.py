# -*- coding: utf-8 -*-
"""
键盘输入两个字符串，输出结果是：
  每个字符串，以及它的长度
  两个字符串连接起来，以及连接之后的字符串长度
"""

a = raw_input("please input str a:")
b = raw_input("please input str b:")

c = a+b

print "the lenth of a:", len(a)
print "the lenth of b:", len(b)
print "the lenth of a+b:", len(c)