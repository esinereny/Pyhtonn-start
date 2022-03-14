 # -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:45:24 2021

@author: user
"""

#dictionary

sozluk = {'book':'kitap',
         'table':'masa'
         }

print(sozluk)

sozluk2 =dict(book='kitap', table='masa')
print(sozluk2)

sozluk['pencil']='kalem'
print(sozluk)

del(sozluk['table'])
print(sozluk)
