# -*- coding: utf-8 -*-
"""
一段英文的文本，统计该文本中单词的出现次数。比如：
How are you. How are you.
"""

s = "How are you. How are you."
d = {}
s = s.lower()

new = s.replace('.', '')
n = new.split()
for i in n:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print d