# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:09:05 2021

@author: user
"""

#break

öğrenciler=['esin','hamza','sevda']

for öğrenci in öğrenciler:
    if öğrenci == 'sevda':
        break
    print('**')

#burdaki olay benim oraya yazdığım öğrenci basta olsaydı döngü hiç çalısmazdı 
#oraya gelen kişeye kadar calişicak,kac tane varsa

#continue

meyveler=['muz','çilek','karpuz']

for meyve in meyveler :
    if meyve == 'çilek':
        continue
    print(meyve + ' içi kod =' + meyve[0:1])
    
#sadece sartın oldugu kısmı çalıştırmaz
        
    
        