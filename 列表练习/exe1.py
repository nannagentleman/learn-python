# -*- coding: utf-8 -*-
"""
通过键盘输入若干个数字（每次输入一个，输入的个数也由用户来决定），然后将这些数字从小到大排序，并打印出排序结果。
"""
nums = []

def InsertSort(a, sort):
    for i in range(len(sort)):
        if sort[i] >= a:
            sort.insert(i, a)
            return sort    
    sort.append(a) 



while 1:
    n = raw_input(u"请输入数字(一次输入一个数字，停止输入请按回车键):")
    if n == '':
        break
    if n.isdigit():
        InsertSort(int(n),nums)
    else:
        try:
            n = float(n)
            InsertSort(n, nums)
        except ValueError:
            n = raw_input('input again:')  
            InsertSort(int(n),nums)
  
print nums
            
