# -*- coding: utf-8 -*-
"""
有一百个人，分别从1一直到100。现在有人拿枪从第一个开始枪毙，每枪毙一个跳过一个，一直到一轮完成。接着在活着的人里面再次枪毙第一个，间隔一个再枪毙一个，
请问最后活着的是这一百个人里的第几个人？
"""

#方法一
l1 = [i+1 for i in range(100)]
for i in range(1,100,2):
    l1.remove(i)

for i in range(25):
    l1.pop(i)

print "最后活着的人的编号列表是：",l1

#方法二：利用函数更普遍的解决类似问题
def cut(lst):
    if len(lst)%2 == 0:
        n = len(lst)/2
    else:
        n = (len(lst)+1)/2
    for i in range(n):
        lst.pop(i)
    return lst
    
l2 = [i+1 for i in range(100)]
cut(l2)
cut(l2)

print "最后活着的人的编号列表是：",l2