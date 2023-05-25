import json 
import re
import os
#Funcion de lectura de archivos json

def leer_json(direccion:str)->list:

    if direccion == "":
        print("No se ingreso una direccion")
    else:
        with open(direccion,"r") as archivo:
            contenido = archivo.read()
            lista = json.loads(contenido)
            return lista
        