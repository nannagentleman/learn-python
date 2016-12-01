# -*- coding: utf-8 -*-
"""
计算：将华氏度转化为摄氏度，公式：DegreesC = 5(DegreesF-32)/9，要求输出的摄氏度，小数点后保留1位小数。
"""

f = raw_input("please input the DegreeF:")


while 1:
    if not f.isdigit():
        f = raw_input("please input again:")
    else:
        f = float(f)
        break

c = 5*(f-32)/9

print "the DegreeC:", round(c, 1)

#检验用户输入