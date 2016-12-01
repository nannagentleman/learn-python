# -*- coding: utf-8 -*-
"承接第5题，计算每个数相对随机数的差，并打印输出"

import random

lst = []
for i in range(10):
    lst.append(random.randint(0,100))
print "100以内的10个随机数:", lst

s = 0
for i in lst:
    s += i

ave = 1.0 * s / len(lst)
print "平均数：", ave

c = 1
for i in lst:
    n = random.randint(0, 100)
    print "随机数是：", n
    print "第", c, "个数与随机数的差值：", i - n
    c += 1