# -*- coding: utf-8 -*-
"""编写一个赋值语句，将变量interest的值设置为变量balance的值乘以0.05"""

balance = raw_input('please input a num:')
while 1:
    if balance.isdigit():
        balance = float(balance)
        break
    else:
        try:
            balance = float(balance)
            break
        except ValueError:
            balance = raw_input('input again:')   
    
        
interest = balance * 0.05
print "interest:", interest
#please print them
#另外，要考虑一个问题，如果balance的值不是数字怎么办？是否允许乘呢？如果不允许，如何判断？