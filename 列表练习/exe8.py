# -*- coding: utf-8 -*-
"""一个列表中的元素是由字符串组成的，将其中长度超过2的元素删除。"""

lst = ["love", "me", "you", "a", "b", "love"]

for i in lst:
    if len(i) > 2:
        lst.remove(i)
        
print lst

        