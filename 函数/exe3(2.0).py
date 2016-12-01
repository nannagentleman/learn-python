# -*- coding: utf-8 -*-
"""
编写一个函数，用以判断某个对象是否可迭代。
比如给该函数传入23这个数字，返回True则说明可迭代，返回false则不可迭代
"""

def is_iterable(obj):
    try:
        for i in obj:
            return True
    except TypeError:
        return False
        
        
print is_iterable([2])

#>>> hasattr("hello", "__iter__")
#也可以用这个函数判断是否可迭代