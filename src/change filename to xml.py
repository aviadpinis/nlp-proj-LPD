
# coding: utf-8

import os
import re

path = "./20000-29999"
dirs = os.listdir( path )

for filename in dirs:
    new_name = re.findall('\d+_', filename)[0][:-1]
    os.rename(path+'/'+filename, path+'/'+new_name+'.xml')
    print(new_name)