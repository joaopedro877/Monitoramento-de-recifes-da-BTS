# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:49:46 2023

@author: jdebr
"""

'''Monitoramento dos dados de cobertura dos recifes ao longo do tempo na BTS - 2011 até 2022'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''abrindo o arquivo'''
achando_csv ='C:/Users/jdebr/Documents/Ic_Recifes_de_corais/Coralnet-CPCe/dados_cobertura.csv'
df = pd.read_csv(achando_csv,sep = ',')


'''separando por recife'''

#criar um data frame para cada local e analisar a variacao ao longo do tempo
alvas=df[df['Local']=='Alvas']
cardinal=df[df['Local']=='Cardinal']   
cardinalN=df[df['Local']=='Cardinal N']  
dentao=df[df['Local']=='Dentao']  
frades=df[df['Local']=='Cardinal']  
fradesS=df[df['Local']=='Frades Sul']  
macroalga_1=df[df['Local']=='Macroalga 1']
macroalga_2=df[df['Local']=='Macroalga 2']
macroalga_3=df[df['Local']=='Macroalga 3']
mangueira=df[df['Local']=='Mangueira']  
mareS=df[df['Local']=='MareS']  
mareW=df[df['Local']=='MareW']  
portugues=df[df['Local']=='Portugues']  
poste1=df[df['Local']=='Poste 1']  
poste4=df[df['Local']=='Poste 4']  
poste6=df[df['Local']=='Poste 6']  

'''avaliando a cobertura ao longo do tempo, de um recife apenas, inicialmente'''
count=df['Label'].value_counts(subset=['Ano'=='2022'],normalize=True)
print(count)

teste= df.groupby(["Local", "Ano"])["Label"].value_counts()
cobertura=teste.to_frame()

teste3=alvas.groupby(['Ano'])['Label'].value_counts()
teste3=teste3.unstack(level='Label')
teste4=pd.melt(teste3)
#inverter o  formato do dataframe
teste5=teste3.T
#transformar em porcentagem
teste6=(teste5[2021] / teste5[2021].sum()) * 100
teste7=(teste5[2022] / teste5[2022].sum()) * 100

#substituindo valores pelas porcentagens
teste5[2021]=teste6
teste5[2022]=teste7
#poderia criar um loop para fazer isso com todos

'''plotando'''
plt.plot()
teste5.plot.bar(title='cobertura %')
# consegui!