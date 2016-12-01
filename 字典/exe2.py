# -*- coding: utf-8 -*-
"""
列表lst1=[1,2,3,4,5,6],lst2=[“a”,”b”,”c”,”d”]，以lst1的元素为key，以lst2的元素为value建立一个字典
"""
lst1=[1,2,3,4,5,6]
lst2=['a','b','c','d']
d = {}

d = dict(zip(lst1,lst2))
print d