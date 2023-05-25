import json 
import re
import os
import random
#Funcion de lectura de archivos json

def leer_json(direccion:str)->list:

    if direccion == "":
        print("No se ingreso una direccion")
    else:
        with open(direccion,"r") as archivo:
            contenido = archivo.read()
            lista = json.loads(contenido)
            return lista


def quick_sort(lista:list, orden:str)->list:
    lista_copia = lista.copy()
    lista_menores=[]
    lista_mayores=[]
    lista_ordenada=[]
    if len(lista) < 2:
        return lista
    else:
        pivote = lista_copia[0]
        for item in lista_copia[1:]:
            if orden == "ascendente" or orden == "asc":
                if (item < pivote):
                    lista_menores.append(item)
                else:
                    lista_mayores.append(item)
            elif orden == "descendente" or orden == "desc":
                if (item < pivote):
                    lista_mayores.append(item)
                else:
                    lista_menores.append(item)
    lista_menores = quick_sort(lista_menores, orden)
    lista_menores.append(pivote)
    lista_mayores = quick_sort(lista_mayores, orden)
    lista_ordenada = lista_menores + lista_mayores
    return lista_ordenada
