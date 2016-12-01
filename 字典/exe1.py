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