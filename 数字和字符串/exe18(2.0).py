# -*- coding: utf-8 -*-
"""
得到某个字符串中的字母个数（不包含其中的空格），比如：”I use Python”
"""

test_str = "I use Python"

new_str = test_str.split()

s = ''.join(new_str)

print len(s)