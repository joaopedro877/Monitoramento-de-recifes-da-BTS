# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:29:49 2023

@author: jdebr
"""

import pandas as pd
import matplotlib.pyplot as plt

'''abrindo o arquivo'''
achando_csv ='C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/dados_cobertura.csv'
df = pd.read_csv(achando_csv,sep = ',')



'''agrupando por ocorrencia de organismos em cada recife'''
cobertura= df.groupby(["Local", "Ano"])["Label"].value_counts()

cobertura=cobertura.unstack(level='Label')

'''invertendo e reorganizando as dimensoes do dataframe'''
cobertura=cobertura.T

'''cobertura em porcentagem para cada recife'''
cobertura2=(cobertura/cobertura.sum())*100

'''deletando as colunas dos anos de 2016 e 2017'''
cobertura3=cobertura2

#criando uma lista com os nomes das colunas e convertendo os itens para list(originalmente sao tuplas)
teste2=cobertura.columns.values.tolist()
teste3 = [list(x) for x in teste2]

#criando um loop para deletar dados de 2016 ou 2017, que nao serao considerados
for i in (teste3):
    if i[1]==2016 or i[1]==2017:
        cobertura3=cobertura3.drop([(i[0],i[1])],axis=1)
        print(i[0])

'''plotando'''

#criando um loop para plotar as imagens de uma vez 
teste4=cobertura3.columns.values.tolist()
teste4=[list(x) for x in teste4]

lista=[]
for item in teste4:
    lista.append(item[0])
locais= []
for local in lista:
    if local not in locais:
        locais.append(local)

for i in locais:
    print(i)
    cobertura3[i].dropna(how='all').plot.bar(title='cobertura recifal em %'+','+i)
    plt.tight_layout()
    plt.savefig((i+'- Cobertura recifal ao longo do tempo'))
    
    
plt.plot()
cobertura3[i].dropna(how='all').plot.bar(title='cobertura recifal em %'+[i])

plt.plot()
cobertura3['Poste 1'].dropna(how='all').plot.bar(title=('cobertura recifal em %'+locais[0]))
plt.tight_layout()
plt.savefig('teste do caminho.png')
# consegui!



'''Fazer para os outros locais'''
'''Fazer da BTS como um todo'''
'''Fazer agrupando em corais duros, algas etc'''

fr=frades.groupby(['Ano'])['Label'].value_counts()
fr=fr.unstack(level='Label')
fr=fr.T
fr=(fr[2019] / fr[2019].sum()) * 100
fr.plot.bar(title='cobertura recifal em %, Frades')