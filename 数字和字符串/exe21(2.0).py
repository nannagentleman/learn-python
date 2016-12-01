# -*- coding: utf-8 -*-
"""键盘输入三个数，计算并输出三个数的平均数"""

a = raw_input("please input the first number:")
while 1:
    if not a.isdigit():
        a = raw_input("please input a number again:")
    else:
        a = float(a)
        break
        
b = raw_input("please input the second number:")
while 1:
    if not b.isdigit():
        b = raw_input("please input a number again:")
    else:
        b = float(b)
        break
        
c = raw_input("please input the third number:")
while 1:
    if not c.isdigit():
        c = raw_input("please input a number again:")
    else:
        c = float(c)
        break
        
ave = a+b+c / 3.0

print ave

#修改意见跟前面的几个作业一样。一定要对用户输入的内容进行判断。