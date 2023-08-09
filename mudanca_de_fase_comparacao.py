# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:11:17 2023

@author: jdebr
"""

'''comparando recifes -> com e sem mudança de fase'''

'''executando o outro script, com dados agrupados em categorias'''

exec(open("C:/Users/jdebr/Documents/Ic_Recifes_de_corais/dados_agrupados_sem_plot.py").read())

'''separando os recifes que estão em mudanca de fase'''

locais_mud_fase=['Dentao','Poste 1','Portugues','Cardinal N']

teste4=cobertura3.columns.values.tolist()
teste4=[list(x) for x in teste4]

lista=[]
for item in teste4:
    lista.append(item[0])
locais= []
for local in lista:
    if local not in locais:
        locais.append(local)
        

locais_sem_mud_fase=[]
for local in locais:
    if local not in locais_mud_fase:
        locais_sem_mud_fase.append(local)


#com mudanca de fase
mud_fase=[col for col in cobertura3.columns.values if col[0] in locais_mud_fase]
mud_fase=[list(x)for x in mud_fase]

cob_mud_fase = cobertura3[mud_fase]

#sem mudanca de fase
sem_mud_fase = [col for col in cobertura3.columns.values if col[0] not in locais_mud_fase]
sem_mud_fase=[list(x) for x in sem_mud_fase]
cob_sem_mud_fase=cobertura3[sem_mud_fase]


'''Calculando a media por ano - com mudanca de fase'''

'''Calcular a media por ano'''
def average_columns_by_year(dataframe, year):
    # Filter columns containing the specified year in their names
    selected_columns = [col for col in dataframe.columns if float(year) in col]

    # Calculate the average for each selected column
    column_averages = dataframe[selected_columns].mean(axis=1)

    return column_averages

cobertura_media_mud_fase_2011 = average_columns_by_year(cob_mud_fase,2011)
cobertura_media_mud_fase_2016 = average_columns_by_year(cob_mud_fase,2016)
cobertura_media_mud_fase_2017 = average_columns_by_year(cob_mud_fase,2017)
cobertura_media_mud_fase_2019 = average_columns_by_year(cob_mud_fase,2019)
cobertura_media_mud_fase_2021 = average_columns_by_year(cob_mud_fase,2021)
cobertura_media_mud_fase_2022 = average_columns_by_year(cob_mud_fase,2022)

cobertura_media_mud_fase=pd.DataFrame()
cobertura_media_mud_fase['2011']=cobertura_media_mud_fase_2011
cobertura_media_mud_fase['2016']=cobertura_media_mud_fase_2016
cobertura_media_mud_fase['2017']=cobertura_media_mud_fase_2017
cobertura_media_mud_fase['2019']=cobertura_media_mud_fase_2019
cobertura_media_mud_fase['2021']=cobertura_media_mud_fase_2021
cobertura_media_mud_fase['2022']=cobertura_media_mud_fase_2022

'''Calculando a media por ano - sem mudanca de fase'''
cobertura_media_sem_mud_fase_2011 = average_columns_by_year(cob_sem_mud_fase,2011)
cobertura_media_sem_mud_fase_2016 = average_columns_by_year(cob_sem_mud_fase,2016)
cobertura_media_sem_mud_fase_2017 = average_columns_by_year(cob_sem_mud_fase,2017)
cobertura_media_sem_mud_fase_2019 = average_columns_by_year(cob_sem_mud_fase,2019)
cobertura_media_sem_mud_fase_2021 = average_columns_by_year(cob_sem_mud_fase,2021)
cobertura_media_sem_mud_fase_2022 = average_columns_by_year(cob_sem_mud_fase,2022)

cobertura_media_sem_mud_fase=pd.DataFrame()
cobertura_media_sem_mud_fase['2011']=cobertura_media_sem_mud_fase_2011
cobertura_media_sem_mud_fase['2016']=cobertura_media_sem_mud_fase_2016
cobertura_media_sem_mud_fase['2017']=cobertura_media_sem_mud_fase_2017
cobertura_media_sem_mud_fase['2019']=cobertura_media_sem_mud_fase_2019
cobertura_media_sem_mud_fase['2021']=cobertura_media_sem_mud_fase_2021
cobertura_media_sem_mud_fase['2022']=cobertura_media_sem_mud_fase_2022


'''Plotando'''
cobertura_media_mud_fase.loc['Zoantideos'].plot(label='Recifes com mudança de fase')
cobertura_media_sem_mud_fase.loc['Zoantideos'].plot(label='Recifes sem mudança de fase ')
plt.legend()

for label in labels:
    plt.figure()
    cobertura_media_mud_fase.loc[label].plot(label='Recifes com mudança de fase')
    cobertura_media_sem_mud_fase.loc[label].plot(label='Recifes sem mudança de fase ')
    plt.title('Cobertura média de '+label)
    plt.legend()