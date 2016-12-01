# -*- coding: utf-8 -*-
'''
写一段python程序，将某个文件压缩成gzip或者bzip格式，然后解压缩到指定目录。
'''
import gzip
import os, sys


with open('new.txt', 'w') as f:
    f.write('This is a new txt file.')
#压缩文件    
def comp(fil, gzip_name):    
    f_in = open(fil, 'rb')
    f_out = gzip.open(gzip_name, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()

f1 = 'new.txt'
g1 = 'new.txt.gz'
comp(f1, g1)
#网上查找到的实现方法




