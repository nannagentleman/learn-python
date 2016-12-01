# -*- coding: utf-8 -*-
"""
编写一个函数，用于判断某个数是不是质数，是则返回True，否则返回False。
"""

def is_zs(num):
    if not num.isdigit():
        return "please input a num"
    else:
        num = int(num)
        if num == 2:
            return True
        else:
            n = 0
            for i in range(num):
                i = i + 1
                #print "i=", i
                #print "ys=", n%i
                if num % i == 0:
                    n = n + 1
            if n > 2:
                return True
            else:
                return False
                
                
                
print is_zs('4')