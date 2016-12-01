# -*- coding: utf-8 -*-
"""键盘输入两个数字（一个小数、一个整数），计算两个数的商，并且输出结果，保留2为小数"""

a = raw_input("please input a decimal:")
b = raw_input("please input a integer:")

result = float(a)/float(b)
print round(result, 2)