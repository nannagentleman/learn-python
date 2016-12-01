# -*- coding: utf-8 -*-
"""计算圆的周长，结果保留两位小数。"""

#从math模块中直接输出pi
d = 1 #直径

from math import pi

print round(d*pi, 2)

#学概率统计时学到的蒙特卡洛方法求pi
import random

n = 100000000000
k = 0

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        k = k + 1

p = 4 * float(k) / float(n)
print round(d*p, 2)
        
        