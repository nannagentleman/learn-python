# -*- coding: utf-8 -*-
"""键盘输入日期，要求格式：年-月-日，打印输出该日期，但是格式编程：月/日/年"""

import re

s = r'\d\d\d\d\-\d{1,2}\-\d{1,2}'

date = raw_input("please input the date:")
while 1:
    if not re.match(s, date):
        date = raw_input("input again:")
    else:
        break

y, m, d = date.split('-')

print m+'/'+d+'/'+y

#ok，但是要检验用户输入是否符合你预定的格式。