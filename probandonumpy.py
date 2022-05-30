
from cProfile import label
from os import rename
from tkinter import Frame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy
import matplotlib.pyplot as plt

filename = "Informacion_proyecto_apartamenntos_bochalema.csv"
#dataset = numpy.loadtxt(filename, delimiter=",", dtype="str")
#print(" dataset: ")
#print(len(dataset))
dataframe = pd.read_csv(filename, header=None, dtype="str")
#dataframe = dataframe.rename(columns={"2": "Champions"})
#dataframe.columns.values[0] = "links"
#dataframe.columns.values[1] = "precioTotal"
  

mapping = {dataframe.columns[0]: 'links', dataframe.columns[1]: 'precioTotal',dataframe.columns[2]: 'habitaciones',dataframe.columns[3]: 'precioUnitario',dataframe.columns[4]: 'metros2'} 
su = dataframe.rename(columns=mapping) 
print(su)
#dataframe.columns.values[2] = "habitaciones"
#dataframe.columns.values[3] = "precioUnitario"
#dataframe.columns.values[4] = "Metros cuadrados"
print(" dataframe: ")
print(dataframe)
dataset = su.values
print(" data_float:")
print(" dataset: ")
print(dataset)
#print(dataset.shape)
#print(dataset.ndim)
linksT=dataframe[0]
preciosT=dataframe[1]
habitaciones=dataframe[2]
precioU=dataframe[3]
metros2=dataframe[4]
data_int = habitaciones.values
#data_float = data_int.astype(float)
#print(data_float)
"""fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(data_int, label="Data")
ax.set_xlabel(" Numero De Personas")
ax.set_ylabel("Metros Cuadrado")
ax.set_title("Precio Total Por Cada Uno")
ax.legend(loc=1) # upper left corner"""
#su.groupby('habitaciones')['precioTotal'].sum().plot(kind='barh',legend='Reverse')#saca la suma de las coloumnas
#plt.plot(su['links'],su['precioTotal']).sum().plot(kind='barh',legend='Reverse')
colors={"dodgerblue","salmon","palevioletred","steelblue","seagreen","plum","blue","indigo","beige","yellow"

}
i=0
for col in su:
    sizes=su[col].value_counts()
    pie=su[col].value_counts().plot(kind='pie',colors=colors,shadow=True,autopct='%1.1f%%',startangle=30,radius=1.5,center=(0.5,0.5),textprops={'fontsize':12},frame=False,pctdistance=.65)
    labels=sizes.index.unique()
    plt.gca().axis("equal") 
    plt.title(su.columns[i],weight='bold',size=14)
    plt.subplots_adjust(left=0.0,bottom=0.1,right=0.85)
    plt.savefig(str(su.columns[i])+'.png',dpi=100,bbox_inches="tight")
    pie.set_ylabel('')
    plt.legend(labels, bbox_to_anchor=(0.5,-.2))
    
    i=i+1
    plt.show()


#media_preciosT=preciosT.mean()
media_preciosT = su.describe()
mediana_preciosT=preciosT.median()
desvi_preciosT=dataframe.std(axis=1)
print("media of Each Column:")
print(media_preciosT)
print("medians of Each Column:")
print(mediana_preciosT)
print("desviacion :")
print(desvi_preciosT)


#dataframe.plot(x='preciosT', y='habitaciones')
#plt.show()


#a=dataframe.value_counts
"""fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(a, label="Data")
ax.set_xlabel("x axis label")
ax.set_ylabel("y axis label")
ax.set_title("title")
ax.legend(loc=2) # upper left corner
--
print(linksT)
print(preciosT)
print(habitaciones)
print(precioU)
print(metros2)
--
plt.show()"""

#X_str = dataset[:, 0:3]
#Y_str = dataset[:, 3]

"""
#pandas  
df = pd.DataFrame({'partidos': partidos}) # primero un diccionario y dentro de un dirccionario una lista
print(df)
df.to_csv('partidos.csv', index=False)"""
