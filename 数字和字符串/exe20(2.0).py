# -*- coding: utf-8 -*-
"""键盘输入两个数字（一个小数、一个整数），计算两个数的商，并且输出结果，保留2为小数"""

a = raw_input("please input a decimal:")
while 1:
    try :
        a = float(a)
        break
    except ValueError:
        a = raw_input("please input a decimal again:")
    
        
        
b = raw_input("please input a integer:")
while 1:
    if not b.isdigit():
        b = raw_input("please input a integer again:")
    else:
        break
        
result = float(a)/float(b)
print ("%.2f" % result)

#我的测试是这样进行的
#>>> 
#please input a decimal:3
#please input a integer:3.0
#1.0

#没有按照你的预期做，就没有得到规定的结果。请牢记：用户输入不可信。对用户输入要进行判断和识别。
#所以上述解法，仅仅是简单的机械解。