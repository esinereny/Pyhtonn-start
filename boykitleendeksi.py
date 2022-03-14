# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:11:29 2021

@author: user
"""
print('Vücut kitle endeksi hesaplanması')
a=int(input('kullanıcı boyu :'))
b= int(input('kullanıcı kilosu :')) 

print('vücut kitle endeksi hesaplanıyor...')

bilgiler=int(input(b/a))

print('kullanıcı boyu : {} \n kullanıcı kilosu : {} \n  ' .format(bilgiler[0],bilgiler[1]))      