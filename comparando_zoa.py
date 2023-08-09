# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:26:48 2023

@author: jdebr
"""

'''Comparando Zoantídeos'''
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

'''somando labels redundantes'''
cobertura2.loc['PcVa']=(cobertura2.loc[['PcVa', 'Epi', 'PcVa+ZoB']].sum())

'''Agrupando zoantideos'''
zoa=['PcVa','ZOAN','PAca']
cobertura2.loc['Zoantideos']=cobertura2.loc[zoa].sum()

'''Calcular a media por ano'''
def average_columns_by_year(dataframe, year):
    # Filter columns containing the specified year in their names
    selected_columns = [col for col in dataframe.columns if float(year) in col]

    # Calculate the average for each selected column
    column_averages = dataframe[selected_columns].mean(axis=1)

    return column_averages

cobertura_media_2011 = average_columns_by_year(cobertura2,2011)
cobertura_media_2016 = average_columns_by_year(cobertura2,2016)
cobertura_media_2017 = average_columns_by_year(cobertura2,2017)
cobertura_media_2019 = average_columns_by_year(cobertura2,2019)
cobertura_media_2021 = average_columns_by_year(cobertura2,2021)
cobertura_media_2022 = average_columns_by_year(cobertura2,2022)

cobertura_media=pd.DataFrame()
cobertura_media['2011']=cobertura_media_2011
cobertura_media['2016']=cobertura_media_2016
cobertura_media['2017']=cobertura_media_2017
cobertura_media['2019']=cobertura_media_2019
cobertura_media['2021']=cobertura_media_2021
cobertura_media['2022']=cobertura_media_2022

'''plotando'''
cobertura_media.loc['PcVa'].plot(label='Palythoa variabilis')
cobertura_media.loc['ZOAN'].plot(label='Zoanthus sociatus')
cobertura_media.loc['PAca'].plot(label='Palythoa caribeorum')
cobertura_media.loc['Zoantideos'].plot(label='Palythoa variabilis + Zoanthus sociatus + Palythoa caribeorum',linestyle='--')
plt.legend()
plt.title('Variação temporal da cobertura média das diferentes espécies de zoantídeos nos recifes da Baía de Todos os Santos ')
plt.ylabel(ylabel='%')
plt.xlabel(xlabel='Ano')

cobertura_media.loc['CYAb'].plot(label='Cianobactérias')
plt.legend()