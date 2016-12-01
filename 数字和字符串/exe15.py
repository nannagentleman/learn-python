# -*- coding: utf-8 -*-
"""有字符串”good good study, day day up”，变成”study, up”"""

s = "good good study, day day up"
a, b = s.split(',')

print a[-5:] + ', ' + b[-2:]

