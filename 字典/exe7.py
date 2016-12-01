# -*- coding: utf-8 -*-
"""
设置一个密码集，即将某个字母按照某个规则对应为另外一个字符串（3个字母组成）。
然后用户输入一个字符串，得到相应的密码。
"""

password = {'a':'dcz', 'b':'zvc', 'c':'qwe', 'd':'asd', 'e':'hfh', 'f':'xvc',
'g':'zcx', 'h':'wtr','i':'xvc', 'j':'quj', 'k':'uuj', 'l':'jjh', 'm':'mmn',
'n':'nnm', 'o':'bbg', 'p':'jjk', 'q':'llo', 'r':'ppo','s':'shg', 't':'zcr',
'u':'qdc', 'v':'ahv', 'w':'rdh', 'x':'vbt', 'y':'zhg', 'z':'ddc'}

s = raw_input("please input the str:")
while 1:
    if not s.isalpha():
        s = raw_input("input again:")
    else:
        s = s.lower()
        break

pword = []
for i in s:
    n = password[i]
    pword.append(n)

result = ''.join(pword)
print result