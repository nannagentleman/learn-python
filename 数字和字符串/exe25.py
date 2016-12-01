# -*- coding: utf-8 -*-
"""键盘输入日期，要求格式：年-月-日，打印输出该日期，但是格式编程：月/日/年"""

date = raw_input("please input the date:")

y, m, d = date.split('-')

print m+'/'+d+'/'+y