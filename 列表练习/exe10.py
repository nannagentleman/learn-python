# -*- coding: utf-8 -*-
"""
对于给定的列表，诸如[1, 45, 90, 8, 76]的样式（将列表中的数字限定在100以内的整数），
将该列表中的数字，对应显示为英文方式，1对应着one，45对应着forty-five
"""
#生成1-99英文写法的list：lst

num_lst = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 
'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

l1 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
l2 = ['','-one', '-two', '-three', '-four', '-five', '-six', '-seven', '-eight', '-nine']

for i in l1:
    for n in l2:
        num_lst.append(i + n)
       
#转换数字的函数f() 
def f(lst, n): 
    l = []
    for i in lst:
        l.append(n[i-1])
        
    return l
    
print f([2,44,55], num_lst)
