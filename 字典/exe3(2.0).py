# -*- coding: utf-8 -*-
"""
建立一个字典，字典的key是a-z的随机字母，value是该字母的ascii表的数值
"""

lst = ['d','c','a','b','q','n','v','z']
dct = {}

for i in lst:
    dct[i] = ord(i)
    
print dct

#随机，可以使用random
import random
chars = "abcdefghijklmnopqrstuvwxyz"
new_lst = [random.choice(chars) for i in chars]
print new_lst