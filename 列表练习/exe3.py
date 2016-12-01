# -*- coding: utf-8 -*-
'''
承接第2题目，向已经得到的排序好的列表中添加一个新的人名，添加后再进行排序。
注意，添加，不是追加。打印结果。
'''
#假定names是已经排好序的名字列表
names = ['Mike', 'Park', 'Saxon', 'Zhang']

def InsertSort(a, sort):
    for i in range(len(sort)):
        if sort[i] >= a:
            sort.insert(i, a)
            return sort    
    sort.append(a) 

def resort(lst): #添加新名后的重新排序函数resort()
    if lst[0] > lst[1]: #把特例排除，因为添加了人名，所以列表里至少有两个元素
        n = lst.pop(0)
        InsertSort(n, lst)
        return lst
    if lst[-1] < lst[-2]:
        n = lst.pop(-1)
        InsertSort(n, lst)
        return lst
    for i in range(1, len(lst)-1):
        if lst[i] < lst[i+1] and lst[i] < lst[i-1]:        
            n = lst.pop(i)
            InsertSort(n, lst)
        if lst[i] > lst[i+1] and lst[i] > lst[i-1]:
            n = lst.pop(i)
            InsertSort(n, lst)
    return lst
            
names.insert(2,'Zzz')
print names
print resort(names)