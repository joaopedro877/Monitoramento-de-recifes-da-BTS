# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:59:56 2023

@author: jdebr
"""

''' Juntando os dataframes de dados classificados manualmente e automaticamente, excluindo colunas
duplicadas'''

import pandas as pd



''' Primeiro arquivo - somente dados classificados manualmente '''

'''abrindo o  primeiro arquivo'''
achando_csv ='C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/dados_cobertura.csv'
df = pd.read_csv(achando_csv,sep = ',')
'''agrupando por ocorrencia de organismos em cada recife'''
cobertura= df.groupby(["Local", "Ano"])["Label"].value_counts()
cobertura=cobertura.unstack(level='Label')
'''invertendo e reorganizando as dimensoes do dataframe'''
cobertura=cobertura.T

#############################################################################

'''Segundo arquivo - dados classificados automaticamente pelo coralnet'''

'''abrindo o arquivo'''
achando_csv2 ='C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/dados_cobertura_automatic.csv'
df2 = pd.read_csv(achando_csv2,sep = ',')
'''agrupando por ocorrencia de organismos em cada recife'''
cobertura2 = df2.groupby(["Local", "Ano"])["Label"].value_counts()
cobertura2 =cobertura2.unstack(level='Label')
'''invertendo e reorganizando as dimensoes do dataframe'''
cobertura2=cobertura2.T

#############################################################################
'''jundando os dois DataFrames'''

cob=pd.concat([cobertura,cobertura2],axis=1)
cob=cob.sort_index()

cob2 = cob.loc[:,~cob.columns.duplicated()].copy()

#############################################################################
'''Salvando'''
cob2.to_pickle('dados_completo.pkl')

'''Acessando posteriormente'''
df=pd.read_pickle("dados_completo.pkl")

############################################################################
'''Salvando com porcentagens e agrupados em grandes grupos'''


labels=cob2.index.values.tolist()


'''somando labels redundantes'''

cob2.loc['Turf'] = (cob2.loc[['TURF', 'Bn-Tf', 'MCT']].sum())
cob2=cob2.drop(['TURF', 'Bn-Tf', 'MCT'])
cob2.loc['PcVa']=(cob2.loc[['PcVa', 'Epi', 'PcVa+ZoB']].sum())
cob2=cob2.drop(['Epi', 'PcVa+ZoB'])
labels=cob2.index.values.tolist()

'''agrupando corais em um unico label'''
hard_coral = ['AGa','AGa+CoB','AGf','AGh','ASso','ASso+CoB','ASso+RCD','FAg','FAg+CoB','FAg+RCD','FAl','HC','MADd','MADd+CoB','MADd+RCD','MEb','MEb+CoB','MEb+RCD','MOca','MOca+CoB','MOca+RCD','MOca+W','MUbr','MUbr+CoB','MUbr+RCD','MUha','MUha+CoB','MUha+RCD','MUhi','MUhi+CoB','MUhi+RCD','OCD','PORa','PORa+CoB','PORa+RCD','PORb','PORb+CoB','PORb+RCD','REC','SCcu','SCw','SCw+CoB','SCw+RCD','SID','SID+CoB','SID+RCD','STEm','Tcoc','Ttag','UnC']
hardcoral=[i for i in hard_coral if i in labels]
cob3=cob2
cob3.loc['Coral']=cob3.loc[hardcoral].sum()
cob3=cob3.drop(hardcoral)
labels=[i for i in labels if i not in hardcoral]
'''agrupando hidrocorais em um unico label'''
hidrocorais=labels[19:22]
cob3.loc['Hidrocorais']=cob3.loc[hidrocorais].sum()
cob3=cob3.drop(hidrocorais)
labels=[i for i in labels if i not in hidrocorais]
labels=cob3.index.values.tolist()
'''Agrupando outros'''
outros=['Wand','Unk','Tape','Shad+HOLE','Shad']
cob3.loc['Outros']=cob3.loc[outros].sum()
cob3=cob3.drop(outros)
labels=[i for i in labels if i not in outros]
labels=cob3.index.values.tolist()
'''Agrupando alga calcaria'''
ac=['AC','CCA']
cob3.loc['Alga calcaria']=cob3.loc[ac].sum()
cob3=cob3.drop(ac)
labels=[i for i in labels if i not in ac]
labels=cob3.index.values.tolist()
'''Agrupando zoantideos'''
zoa=['PcVa','ZOAN','PAca']
cob3.loc['Zoantideos']=cob3.loc[zoa].sum()
cob3=cob3.drop(zoa)
labels=[i for i in labels if i not in zoa]
labels=cob3.index.values.tolist()
'''Agrupando algas'''
alga=['UnFr','SARG','Dpyteris','Dta','HA','OtFr','PEN','CAra','CAUL']
cob3.loc['Algas']=cob3.loc[alga].sum()
cob3=cob3.drop(alga)
labels=[i for i in labels if i not in alga]
labels=cob3.index.values.tolist()
'''Agrupando octocorais'''
octo=['CAri','HEau','NEat','Ooct','PHdi']
cob3.loc['Octocorais']=cob3.loc[octo].sum()
cob3=cob3.drop(octo)
labels=[i for i in labels if i not in octo]
labels=cob3.index.values.tolist()
'''Agrupando esponjas'''
esp=['APLY','CLIO','MONA','OSp']
cob3.loc['Esponjas']=cob3.loc[esp].sum()
cob3=cob3.drop(esp)
labels=[i for i in labels if i not in esp]
labels=cob3.index.values.tolist()
'''Agrupando cianobacteria'''
cian=['CYAb']
cob3.loc['Cianobacteria']=cob3.loc[cian].sum()
cob3=cob3.drop(cian)
labels=[i for i in labels if i not in cian]
labels=cob3.index.values.tolist()
'''Agrupando outros invertebrados'''
ou_in=['ASCI','BRIO','CIRR','CoAs','Dave','LEBR','LYva','Olive','SOLA','SeaS','SerpS']
cob3.loc['Outros invertebrados']=cob3.loc[ou_in].sum()
cob3=cob3.drop(ou_in)
labels=[i for i in labels if i not in ou_in]
labels=cob3.index.values.tolist()

'''cob em porcentagem para cada recife'''
cob3=(cob3/cob3.sum())*100


############################################################################################
'''Salvando novamente'''
cob3.to_pickle('C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/dados_completo_grupos_taxonomicos.pkl')
