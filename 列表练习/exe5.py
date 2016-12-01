# -*- coding: utf-8 -*-
"""生成100以内的10个随机数，并计算它们的平均数"""

import random

lst = []
for i in range(10):
    lst.append(random.randint(0,100))
print "100以内的10个随机数:", lst

s = 0
for i in lst:
    s += i
print s
ave = 1.0 * s / len(lst)
print "平均数：", ave