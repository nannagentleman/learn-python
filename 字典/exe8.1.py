# -*- coding: utf-8 -*-
"""
对于字符串a = "aAsmr3idd4bgs7Dlsf9eAF"，请依次完成如下任务：
a)请将字符串中的数字取出，并输出成一个新的字符串。
"""

a = "aAsmr3idd4bgs7Dlsf9eAF"

#第一题
for i in a:
    if i.isdigit():
        a = a.replace(i, '')
        
print a