# -*- coding: utf-8 -*-
"""比较一下，a=333和a=’333’有什么区别？"""

a = 333
b = '333'

print dir(a) #变量a的值是数值
print dir(b) #变量b的值是字符串

print a+23 #数值可以与数值直接进行运算
print b + '23' #字符串可以与其他字符串进行拼接，直接与数值相加会报错
print int(b) + 23 #转换后可以进行运算

print a == b #False
print id(a) == id(b) #False