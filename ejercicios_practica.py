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

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
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

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = {
                  "nombre": "Pedro",
                  "apellido": "Lugo",
                  "DNI": 95742846,
                  "prendas": [
                      {
                       "zapatillas": 2,
                       "remeras": 15,
                       "gorras": 4
                      }
                      ]
                }

    with open('json_personal.json', 'w') as jsonfile:
        data = [json_data]
        json.dump(data, jsonfile, indent=4)
    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()
    with open('json_personal.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    json_string = json.dumps(json_data, indent=4)
    print(json_string)
    pass


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    root = minidom.Document()
    xml = root.createElement('Datos')
    root.appendChild(xml)
    productchild = root.createElement('Nombre')
    productchild.appendChild(root.createTextNode('Pedro'))
    xml.appendChild(productchild)

    productchild = root.createElement('Apellido')
    productchild.appendChild(root.createTextNode('Lugo'))
    xml.appendChild(productchild)

    productchild = root.createElement('DNI')
    productchild.appendChild(root.createTextNode('167855552'))
    xml.appendChild(productchild)

    productchild = root.createElement('Prendas')
    productchild.appendChild(root.createTextNode('Prendas'))
    xml.appendChild(productchild)

    child0product = root.createElement('tipo')
    child0product.appendChild(root.createTextNode('zapatos'))
    productchild.appendChild(child0product)

    child0product = root.createElement('Cantidad')
    child0product.appendChild(root.createTextNode('5'))
    productchild.appendChild(child0product)

    child0product = root.createElement('tipo')
    child0product.appendChild(root.createTextNode('Remeras'))
    productchild.appendChild(child0product)

    child0product = root.createElement('Cantidad')
    child0product.appendChild(root.createTextNode('15'))
    productchild.appendChild(child0product)

    xml_str = root.toprettyxml(indent="\t")
    archivo = "archivo_xml.xml"
    with open(archivo, "w") as f:
        f.write(xml_str)
  

def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.

    tree = ET.parse('archivo_xml.xmL')
    root = tree.getroot()

    print('Recorrer el archivo XML')
    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)

    pass


def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.
    
    response = requests.get(url)
    data = response.json()
    resultados = {}
    csvfile = open('diccionario.csv', 'w', newline='')
    header = ["userId", "Cantidad"]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    contador = 0
    for i in range(1,11):
        for x in data:
            if i == x['userId']:
                if x['completed'] == True:
                    contador += 1
                else:
                    continue
            else:
                if contador != 0:
                    resultados = {"userId" : i, "Cantidad" : contador}
                    writer.writerow(resultados)
                    contador = 0
                    break
                else:
                    continue
    csvfile.close()
    datos = np.genfromtxt('diccionario.csv', delimiter=',', skip_header=1)
    print(datos)
    x = datos[:, 0]
    y = datos[:, 1]
    fig = plt.figure()
    fig.suptitle('Usuarios que completaron los titulos', fontsize=16)
    ax = fig.add_subplot()

    ax.pie(y, labels = x, autopct='%1.1f%%', shadow=True, startangle=90) 
    # Igualo la relacion de aspecto para que se vea como un círculo
    ax.axis('equal')
    plt.show()

    fig = plt.figure()
    fig.suptitle('Usuarios que completaron los titulos', fontsize=16)
    ax1 = fig.add_subplot()

    ax1.bar(x, y, label='Titulos completados')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    custom_ticks = np.linspace(1, 10, 11, dtype=int)
    ax1.set_xticks(custom_ticks)
    ax1.set_ylabel("Cantidad de Titulos")
    ax1.set_xlabel("Usuarios")
    plt.show()
     

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
