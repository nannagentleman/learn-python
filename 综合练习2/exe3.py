# -*- coding: utf-8 -*-
"""
编写一段程序，抓取www.itdiffer.com首页的内容。
"""

import urllib

def get_content(url):
    
    content = urllib.urlopen(url)
    return content.read()

url = "http://www.itdiffer.com"  
 
'''
with open('b.txt', 'r+') as f:
    f.write(get_content(url))
    con = f.read()
    print con


    
'''
con = get_content(url)
f = open('xx.txt', 'r+')
f.write(con)
c = f.readline()
print c #疑问：c与con的内容为何不同呢？
f.close()

