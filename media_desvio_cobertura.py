# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:30:40 2023

@author: jdebr
"""

'''media e desvio padrao da cobertura recifal, por ano'''

import pandas as pd
import matplotlib.pyplot as plt


'''executando o script onde os dados estao agrupados'''
exec(open("C:/Users/jdebr/Documents/Ic_Recifes_de_corais/dados_agrupados_sem_plot.py").read())

'''Calcular a media por ano'''
def average_columns_by_year(dataframe, year):
    # Filter columns containing the specified year in their names
    selected_columns = [col for col in dataframe.columns if float(year) in col]

    # Calculate the average for each selected column
    column_averages = dataframe[selected_columns].mean(axis=1)

    return column_averages

cobertura_media_2011 = average_columns_by_year(cobertura3,2011)
cobertura_media_2016 = average_columns_by_year(cobertura3,2016)
cobertura_media_2017 = average_columns_by_year(cobertura3,2017)
cobertura_media_2019 = average_columns_by_year(cobertura3,2019)
cobertura_media_2021 = average_columns_by_year(cobertura3,2021)
cobertura_media_2022 = average_columns_by_year(cobertura3,2022)

cobertura_media=pd.DataFrame()
cobertura_media['2011']=cobertura_media_2011
cobertura_media['2016']=cobertura_media_2016
cobertura_media['2017']=cobertura_media_2017
cobertura_media['2019']=cobertura_media_2019
cobertura_media['2021']=cobertura_media_2021
cobertura_media['2022']=cobertura_media_2022

'''Calculando o desvio padrão'''
def std_columns_by_year(dataframe, year):
    # Filter columns containing the specified year in their names
    selected_columns = [col for col in dataframe.columns if float(year) in col]

    # Calculate the average for each selected column
    column_std = dataframe[selected_columns].std(axis=1)

    return column_std

std_cobertura_media_2011 = std_columns_by_year(cobertura3,2011)
std_cobertura_media_2016 = std_columns_by_year(cobertura3,2016)
std_cobertura_media_2017 = std_columns_by_year(cobertura3,2017)
std_cobertura_media_2019 = std_columns_by_year(cobertura3,2019)
std_cobertura_media_2021 = std_columns_by_year(cobertura3,2021)
std_cobertura_media_2022 = std_columns_by_year(cobertura3,2022)

std_cobertura_media=pd.DataFrame()
std_cobertura_media['2011']=std_cobertura_media_2011
std_cobertura_media['2016']=std_cobertura_media_2016
std_cobertura_media['2017']=std_cobertura_media_2017
std_cobertura_media['2019']=std_cobertura_media_2019
std_cobertura_media['2021']=std_cobertura_media_2021
std_cobertura_media['2022']=std_cobertura_media_2022

'''plotando media e desvio de grupos específicos'''
cobertura_media.loc['Coral'].plot(title='Cobertura média em % ',marker='o')
plt.errorbar(cobertura_media.loc['Coral'].index, cobertura_media.loc['Coral'].values, yerr=std_cobertura_media.loc['Coral'].values, capsize=5, linestyle='', alpha=0.6)
cobertura_media.loc['Turf'].plot(marker='o')
plt.errorbar(cobertura_media.loc['Turf'].index, cobertura_media.loc['Turf'].values, yerr=std_cobertura_media.loc['Turf'].values, capsize=5, linestyle='', alpha=0.6)
cobertura_media.loc['Zoantideos'].plot(marker='o')
plt.errorbar(cobertura_media.loc['Zoantideos'].index, cobertura_media.loc['Zoantideos'].values, yerr=std_cobertura_media.loc['Zoantideos'].values, capsize=5, linestyle='', alpha=0.6)
plt.legend()

plt.plot(cobertura_media.loc['Coral'].index, cobertura_media.loc['Coral'].values, marker='o')

# Plot the standard deviation as error bars
plt.errorbar(cobertura_media.loc['Coral'].index, cobertura_media.loc['Coral'].values, yerr=std_cobertura_media.loc['Coral'].values, capsize=5, linestyle='', alpha=0.6)


'''plotando todas as imagens separadamente'''
for i in cobertura_media.index.values:
    plt.figure()
    cobertura_media.loc[i].plot(title='Cobertura média de '+i+' em %',marker='o')
    plt.tight_layout()
plt.legend()


