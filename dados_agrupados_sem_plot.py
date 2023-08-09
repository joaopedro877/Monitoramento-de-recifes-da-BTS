# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:53:44 2023

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

labels=cobertura.index.values.tolist()


'''somando labels redundantes'''
cobertura2=cobertura
cobertura2.loc['Turf'] = (cobertura2.loc[['TURF', 'Bn-Tf', 'MCT']].sum())
cobertura2=cobertura2.drop(['TURF', 'Bn-Tf', 'MCT'])
cobertura2.loc['PcVa']=(cobertura2.loc[['PcVa', 'Epi', 'PcVa+ZoB']].sum())
cobertura2=cobertura2.drop(['Epi', 'PcVa+ZoB'])
labels=cobertura2.index.values.tolist()

'''agrupando corais em um unico label'''
hard_coral = ['AGa','AGa+CoB','AGf','AGh','ASso','ASso+CoB','ASso+RCD','FAg','FAg+CoB','FAg+RCD','FAl','HC','MADd','MADd+CoB','MADd+RCD','MEb','MEb+CoB','MEb+RCD','MOca','MOca+CoB','MOca+RCD','MOca+W','MUbr','MUbr+CoB','MUbr+RCD','MUha','MUha+CoB','MUha+RCD','MUhi','MUhi+CoB','MUhi+RCD','OCD','PORa','PORa+CoB','PORa+RCD','PORb','PORb+CoB','PORb+RCD','REC','SCcu','SCw','SCw+CoB','SCw+RCD','SID','SID+CoB','SID+RCD','STEm','Tcoc','Ttag','UnC']
hardcoral=[i for i in hard_coral if i in labels]
cobertura3=cobertura2
cobertura3.loc['Coral']=cobertura3.loc[hardcoral].sum()
cobertura3=cobertura3.drop(hardcoral)
labels=[i for i in labels if i not in hardcoral]
'''agrupando hidrocorais em um unico label'''
hidrocorais=labels[19:22]
cobertura3.loc['Hidrocorais']=cobertura3.loc[hidrocorais].sum()
cobertura3=cobertura3.drop(hidrocorais)
labels=[i for i in labels if i not in hidrocorais]
labels=cobertura3.index.values.tolist()
'''Agrupando outros'''
outros=['Wand','Unk','Tape','Shad+HOLE','Shad']
cobertura3.loc['Outros']=cobertura3.loc[outros].sum()
cobertura3=cobertura3.drop(outros)
labels=[i for i in labels if i not in outros]
labels=cobertura3.index.values.tolist()
'''Agrupando alga calcaria'''
ac=['AC','CCA']
cobertura3.loc['Alga calcaria']=cobertura3.loc[ac].sum()
cobertura3=cobertura3.drop(ac)
labels=[i for i in labels if i not in ac]
labels=cobertura3.index.values.tolist()
'''Agrupando zoantideos'''
zoa=['PcVa','ZOAN','PAca']
cobertura3.loc['Zoantideos']=cobertura3.loc[zoa].sum()
cobertura3=cobertura3.drop(zoa)
labels=[i for i in labels if i not in zoa]
labels=cobertura3.index.values.tolist()
'''Agrupando algas'''
alga=['UnFr','SARG','Dpyteris','Dta','HA','OtFr','PEN','CAra','CAUL']
cobertura3.loc['Algas']=cobertura3.loc[alga].sum()
cobertura3=cobertura3.drop(alga)
labels=[i for i in labels if i not in alga]
labels=cobertura3.index.values.tolist()
'''Agrupando octocorais'''
octo=['CAri','HEau','NEat','Ooct','PHdi']
cobertura3.loc['Octocorais']=cobertura3.loc[octo].sum()
cobertura3=cobertura3.drop(octo)
labels=[i for i in labels if i not in octo]
labels=cobertura3.index.values.tolist()
'''Agrupando esponjas'''
esp=['APLY','CLIO','MONA','OSp']
cobertura3.loc['Esponjas']=cobertura3.loc[esp].sum()
cobertura3=cobertura3.drop(esp)
labels=[i for i in labels if i not in esp]
labels=cobertura3.index.values.tolist()
'''Agrupando cianobacteria'''
cian=['CYAb']
cobertura3.loc['Cianobacteria']=cobertura3.loc[cian].sum()
cobertura3=cobertura3.drop(cian)
labels=[i for i in labels if i not in cian]
labels=cobertura3.index.values.tolist()
'''Agrupando outros invertebrados'''
ou_in=['ASCI','BRIO','CIRR','CoAs','Dave','LEBR','LYva','Olive','SOLA','SeaS','SerpS']
cobertura3.loc['Outros invertebrados']=cobertura3.loc[ou_in].sum()
cobertura3=cobertura3.drop(ou_in)
labels=[i for i in labels if i not in ou_in]
labels=cobertura3.index.values.tolist()

'''cobertura em porcentagem para cada recife'''
cobertura3=(cobertura3/cobertura3.sum())*100
