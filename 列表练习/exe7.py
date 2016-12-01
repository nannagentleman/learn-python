# -*- coding: utf-8 -*-
"""
有一个列表，其中有重复元素，请将重复元素删除，并且在另外一个列表中存储重复的元素，
例如列表[1, 1, 2, 3, 3]这里面有重复元素，删除之后变成了[1,2,3]，在另外一个列表中存储[1,3]
"""

def detect_dup(lst): #去重并返回重复元素的列表
    lst1 = list(set(lst))
    for i in lst1:
        lst.remove(i)
    lst = list(set(lst))
    return lst, lst1
   
lst = [1,2,3,4,5,3,3,3] 
a,b = detect_dup(lst)
print "重复的元素为：",a 
print "去重后的列表为：",b

    