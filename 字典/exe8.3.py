# -*- coding: utf-8 -*-
"""
c)请去除字符串多次出现的字母，仅留最先出现的一个,大小写不敏感。
例 'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出 'asmr3id4bg7lf9e'
"""

a = "aAsmr3idd4bgs7Dlsf9eAF"

#第三题  
lst = []
a = a.lower()

for i in a:
    if i in lst:
        pass
    else:
        lst.append(i)
        
print ''.join(lst)