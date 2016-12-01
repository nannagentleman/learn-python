# -*- coding: utf-8 -*-
'''
复制文件。通过命令行参数，把第一个文件的内容复制到第二个文件。（os、sys）
'''
import os

with open("file1.txt", "w") as f1:
    f1.write("This is a file")
        
command = 'copy file1.txt file2.txt'

os.system(command)

#疑问：运行结果为何会出现乱码？
f = open("file2.txt")
c = f.read()
print c
f.close()
