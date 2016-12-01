# -*- coding: utf-8 -*-
'''
类似第一题，但是输入的是人名，请将这些人名按照字典顺序排序，并打印出结果。
'''

names = []

while 1:
    n = raw_input(u"请输入英文人名(一次输入一个名字，默认首字母大写，停止输入请按回车键):")
    if n == '':
        break
    while 1:
        if n.isalpha():
            names.append(n.capitalize())
            break
        else:
            n = raw_input('input again:')  

names.sort()  
print names