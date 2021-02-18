#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro"
__email__ = "pllugo@gmail.com"
__version__ = "1.1"

import json
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
from collections import Counter
import numpy as np


#def report(lista_datos):
    #fig = plt.figure()
    #fig.suptitle('Reporte de busqueda de Apartamentos en Mendoza-Argentina', fontsize=12)
    #ax = fig.add_subplot()
    #x = ['Precio por debajo', 'Precio en el rango', 'Precio por encima del rango']

    #ax.pie(lista_datos, labels = x, autopct='%1.1f%%', shadow=True, startangle=90) 
    # Igualo la relacion de aspecto para que se vea como un círculo
    #ax.axis('equal')
    #plt.show()


def transform(lista_diccionario):
    lista1 = []
    for i in range(len(lista_diccionario)):
        variable = lista_diccionario[i]
        lista1.append(variable['userId'])
    frecuencia = {}
    
    for n in lista1:
        if n in frecuencia:
            frecuencia[n] += 1#se repite mas de 1 vez
        else:
            frecuencia[n] = 1#se repite 1 sola vez

  

def fetch(pagina, id):
    url_nuevo = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=' + pagina
    print(url_nuevo)
    response = requests.get(url_nuevo)
    data = response.json()
    json_response = data['data']
    resultado = []
    for elem in json_response:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        variable = elem['location']
        if variable['id'] == id:
            resultado.append({'userId': elem['userId'], 'amount': elem['amount']})
        else:
            continue
    return resultado

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    page_number = str(input('Ingrese el número de página a estudiar:\n'))
    location_id = int(input('Ingrese la locación_id:\n'))
    dataset = fetch(page_number, location_id)
    if dataset:
        print('se encontraron conincidencias')
        print(dataset)
    else:
        print('no se encuentra location_id = {}'.format(location_id))
    transform(dataset)
    #print(data)
    #report(data)