# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:23:02 2021

@author: user
"""

print('Beden Kitle Endeksi Hesaplama')
b=float(input('Kullanıcı Boyu :'))
k=int(input('Kullanıcı Kilosu :'))

bedenKitleEndeksi=k/b**2


if bedenKitleEndeksi <18.5 :
    print('zayıf')
elif 18.5< bedenKitleEndeksi <25 :
    print('normal')
elif 25< bedenKitleEndeksi <30 :
    print('Fazla Kilolu')
else:
    print('obez')
