# -*- coding: utf-8 -*-
"""
将地址簿中一条地址看做一个类，它的属性为：
a)         姓名
b)         电子信箱
c)         电话号码
拥有的方法：
d)         修改个属性
编写程序，实现上述地址簿
"""

class address(object):
    def __init__(self, name, email, phone):
        self.name = name
        self. email = email
        self. phone = phone
        
    def change_name(self, new_name):
        self.name = new_name
        
    def change_email(self, new_email):
        self.email = new_email
        
    def change_phone(self, new_phone):
        self.phone = new_phone

if __name__ == "__main__":        
    a = address('zhang', '3@qq.com', '18888888888')
    a.change_name('wang')
    a.change_phone('22222222222')
    print a.name
    print a.phone
