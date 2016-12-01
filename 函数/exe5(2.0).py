# -*- coding: utf-8 -*-
"""
编写解一元二次方程的程序
"""
#疑问：import math 应该放在函数内还是函数外面？
#恒等的情况如何表示？retrun True?

import math, cmath

def delta(a,b,c):
    return b**2 - 4*a*c

def f(a,b,c):
    if a == 0 :
        if b == 0 and c != 0:
            return False
        elif b == 0 and c == 0:
            return True
        else:        
            return -c/b
    else:
        if delta(a,b,c) < 0:
            return (-b + math.sqrt(delta(a,b,c))*1j)/(2*a), (-b - math.sqrt(delta(a,b,c))*1j)/(2*a)
            #出错，但没找到问题出在哪里
        #1j，这不是程序中的写法。关于复数的问题，请参考complex()内建函数的使用
        elif delta(a,b,c) == 0:
            return -b/(2*a)
        elif delta(a,b,c) > 0:
            return (-b + math.sqrt(delta(a,b,c)))/(2*a), (-b - math.sqrt(delta(a,b,c)))/(2*a)
        
print f(1,4,6)