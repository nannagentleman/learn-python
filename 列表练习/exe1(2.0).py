# -*- coding: utf-8 -*-
"""
通过键盘输入若干个数字（每次输入一个，输入的个数也由用户来决定），然后将这些数字从小到大排序，并打印出排序结果。
"""
nums = []

while 1:
    n = raw_input(u"请输入数字(一次输入一个数字，停止输入请按回车键):")
    if n == '':
        break
    while 1:
        if n.isdigit():
            nums.append(int(n))
            break
        else:
            try:
                n = float(n)
                nums.append(n)
                break
            except ValueError:
                n = raw_input('input again:')
            
nums.sort() 
print nums
            
#以上方法有点复杂了。可以这样做：
#用户输入-》判断输入是否为数字-》是则加入列表-》用列表排序方法l.sort()完成排序