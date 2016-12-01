# -*- coding: utf-8 -*-
"""
编写实现斐波那契数列的程序。
（有多种实现方法，必须编写函数。建议至少写两种。其中一种用递归实现。
建议要自己研究，尽可能不上网搜索。因为这个题目非常常见。
如果你写好了，再上网搜索，对照修改是可以的。）
"""

"""
#方法一：
def fib(n):
    a1 = 1
    a2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n-2):
            a = a1 + a2
            a1 = a2
            a2 = a
    return a
 


"""
#方法二：
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        r = fib(n-1) + fib(n-2)
        return r

                
        
def fib_list(n):
    list_fib = [fib(i+1) for i in range(n)]    
    return list_fib
    
print fib_list(12)
    
