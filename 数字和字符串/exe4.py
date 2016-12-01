# -*- coding: utf-8 -*-
"""计算两个数的乘法，并且将结果打印出来，结果保留两位小数"""

a = 3.33
b = 4.43

p = a * b
print p

#解法一
p1 = ("%.2f"% p)
print p1

#解法二
p2 = round(p, 2)
print p2