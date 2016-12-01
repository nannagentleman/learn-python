# -*- coding: utf-8 -*-
import shutil
import os
import gzip


#解压缩文件：
def decomp(gz, new_filename, new_path):
    f1 = gzip.open(gz, 'rb')
    content = f1.read()
    f1.close()
    
    print 'content=', content  
    
    f = open(new_filename, 'w')
    f.write(content)
    f.close()
     
    old_path = os.path.abspath(new_filename)
    shutil.move(old_path, new_path)

f1 = 'new.txt.gz'
new_path = 'D:\\Git'
new_file = 'n.txt'

decomp(f1, new_file, new_path)
