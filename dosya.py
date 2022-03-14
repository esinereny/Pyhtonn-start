# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:26:59 2021

@author: user
"""

f = open('dosyaacmadenemesi.py')
f = open('dosyaacmadenemesi.py')
#print (f.read(6))
#print (f.readline())     
for k in f :
    print(k)
    

# w yaptığımızda dosyadaki verileri sildi dikkat

import os
os.remove('sudents.py')

#%%
import os
os.rmdir('sudents.py')

#burdaki çalışmalar silindi