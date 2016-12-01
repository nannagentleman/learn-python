# -*- coding: utf-8 -*-
"""
统计上述文件中共有多少个不重复的单词，每个单词在文档中的出现次数。并将统计结果打印出来（英文大小写不敏感）。
"""
def f(con):
    dic = {}

    
    con = con.lower()
    con = con.replace(',', '')
    con = con.replace('.', '')
    con = con.replace('-', '')
    con = con.replace(':', '')
    con = con.replace('(', '')
    con = con.replace(')', '')
    l = con.split()
    
    for i in l:
        if i.isdigit():
            continue
        elif i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
            
    return dic
    
    
fl = open('1.txt', 'r+')
con = fl.read()
print f(con)

fl.close()
