# -*- coding: utf-8 -*-
"""
列举出把两个字典合并的方法
"""

d1 = {'a':3, 'b':4}
d2 = {'c':1, 'd':2}

#方法一
for k, v in d2.items():
    d1[k] = v
    
print d1

#方法二
print dict(d1.items() + d2.items())

#方法三
d1.update(d2)
print d1