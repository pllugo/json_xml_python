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


def report(lista_datos):
    fig = plt.figure()
    fig.suptitle('Reporte de busqueda de Apartamentos en Mendoza-Argentina', fontsize=12)
    ax = fig.add_subplot()
    x = ['Precio por debajo', 'Precio en el rango', 'Precio por encima del rango']

    ax.pie(lista_datos, labels = x, autopct='%1.1f%%', shadow=True, startangle=90) 
    # Igualo la relacion de aspecto para que se vea como un círculo
    ax.axis('equal')
    plt.show()


def transform(lista_diccionario, precio_minimo, precio_maximo):
    lista1 = []
    lista2 = []
    lista3 = []
    for i in lista_diccionario:
        if i['price'] < precio_minimo:
            lista1.append(i['price'])
        else:
            if (i['price'] > precio_minimo) and (i['price'] < precio_maximo):
                lista2.append(i['price'])
            else:
                if i['price'] > precio_maximo:
                    lista3.append(i['price'])
                else:
                    continue
    lista_departamentos = []
    min_count = len(lista1)
    lista_departamentos.append(min_count) 
    min_max_count = len(lista2)
    lista_departamentos.append(min_max_count)
    max_count = len(lista3)
    lista_departamentos.append(max_count)

    return lista_departamentos


def fetch():
    #Ejercicio de busqueda de alquileres en Mercalo libre
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    data = response.json()
    json_response = data['results']
    print(json_response)
    resultado = [{'price': x['price'], 'condition': x['condition']} for x in json_response if x['currency_id'] == "ARS"]
    return resultado

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    min = float(input('Ingrese el prcio minimo (en $ARS) para busqueda de apartamentos:\n'))
    max = float(input('Ingrese el prcio minimo (en $ARS) para busqueda de apartamentos:\n'))
    dataset = fetch()
    data = transform(dataset, min, max)
    print(data)
    report(data)