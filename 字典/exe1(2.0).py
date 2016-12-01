# -*- coding: utf-8 -*-
"""
把下面的字典：{“name”: “python”, “book”: “python”, “lang”:”english”}，然后将该字典的键和值对换。
"""

d = {"name": "python", "book": "python", "lang":"english"}
new = {}
#形式一
for i,k in d.items():
    new[k] = i
    
print new
#形式二
new = {k:i for i, k in d.items()}
print new

#字典中键唯一，所以这种方法使键值对换后信息有损失

#你注释中的是一个问题，遇到这种情况，一种比较好的处理方式，是将相同的两个放到一个列表中作为value。
d = {"name": "python", "book": "python", "lang":"english"}
import collections
nd = collections.defaultdict(list)
for k,v in d.iteritems():
    nd[v].append(k)
print nd
