# -*- coding: utf-8 -*-
'''
类似第一题，但是输入的是人名，请将这些人名按照字典顺序排序，并打印出结果。
'''

names = []

def InsertSort(a, sort):
    for i in range(len(sort)):
        if sort[i] >= a:
            sort.insert(i, a)
            return sort    
    sort.append(a) 



while 1:
    n = raw_input(u"请输入英文人名(一次输入一个名字，默认首字母大写，停止输入请按回车键):")
    if n == '':
        break
    if n.isalpha():
        InsertSort(n.capitalize(), names)
    else:
        n = raw_input('input again:')  
        InsertSort(n.capitalize(), names)
  
print names