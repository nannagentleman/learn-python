# -*- coding: utf-8 -*-
"""
b)请统计字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
并输出成一个字典。 例 {'a':3,'b':1}
"""
a = "aAsmr3idd4bgs7Dlsf9eAF"

for i in a:
    if i.isdigit():
        a = a.replace(i, '')
a = a.lower()
d = {}

for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print d 