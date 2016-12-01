# -*- coding: utf-8 -*-
"""
用户通过键盘输入员工姓名和员工的工号，将输入的信息存入一个字典中。
并且按照姓名顺序，将姓名和工号打印出来。
"""

d = {}

while 1:
    name = raw_input("please input the name(press Enter to stop):")
    if name == '':
        break
    while 1:
        if not name.isalpha():
            name = raw_input("input the name again:")
        else:
            ID = raw_input("please input the id:")
            while 1:
                if not ID.isdigit():
                    ID = raw_input("input the id again:")
                else:
                    d[name] = ID
                    break
            break

for k, v in d.items():
    print "name:", k
    print "ID:", v, "\n"

#这个程序写得不好。参考下面的。
names = []
ids = []
while 1:
    print "input names and id, 'q'-exit"
    name = raw_input("input name:")
    if name in names:
        print name," has been inputed, please change another."
        continue
    elif name == 'q':
        print "You have exited"
        break
    else:
        names.append(name)
    print "input id of ",name
    id = raw_input("id:")
    ids.append(id)

new_dict = dict(zip(names, ids))
print new_dict