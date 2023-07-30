# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:16:55 2022

@author: jdebr
"""


'''Editando arquivos em .cpc - substituindo CoBleach por CoB e ZoBleac por ZoB'''
'''Esse arquivo esta vazio. Devo ter apagado sem querer ->C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/VT-2019/drive-download-20221012T124133Z-001/Imagens sorteadas 191/Cardinal 191/Cardinal 101081 (2021_11_01 14_59_57 UTC).cpc'''


'''Pastas nas quais o programa foi aplicado para substtuir as notes de branqueamento de zoantideo e coral :
    ->VT-2019/drive-download-20221012T124133Z-001/Imagens sorteadas 191/Cardinal 191
    
    ->
    
'''



'''Pode ser interessante adicionar um contador para indicar quantas vzs a str aparece'''

import os 

'''definindo texto que deve ser buscado e substituido ZoBleac ou CoBleac'''
''' Da para substituir os dois de uma vez, mas faco isso depois'''

search_text = "oBleac"
'''definindo texto que sera escrito''' 
replace_text = "oB"

'''pasta na qual os arquivos estao -> basta clicar em copiar a pasta'''
pasta= 'C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/BTS 2011/Poste4 07 03 11'


'''os arquivos com a extensao .cpc serao selecionados para a busca e substituicao do texto'''
ext = ('.cpc')

for files in os.listdir(pasta):
    if files.endswith(ext):
        with open((pasta+'/'+files),'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)
        with open((pasta+'/'+files), 'w') as file:    
            file.write(data)
            
        print(files)
    else:
        continue
    
