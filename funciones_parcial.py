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
    lista_menores = []
    lista_mayores = []
    lista_ordenada = []

    if len(lista) < 2:
        return lista
    else:
        aux = lista_copia[0]
        for item in lista_copia[1:]:
            if orden == "ascendente" or orden == "asc":
                if (item < aux):
                    lista_menores.append(item)
                else:
                    lista_mayores.append(item)
            elif orden == "descendente" or orden == "desc":
                if (item < aux):
                    lista_mayores.append(item)
                else:
                    lista_menores.append(item)
    lista_menores = quick_sort(lista_menores, orden)
    lista_menores.append(aux)
    lista_mayores = quick_sort(lista_mayores, orden)
    lista_ordenada = lista_menores + lista_mayores
    return lista_ordenada

def obtener_numero_entero(mensaje:str,mensaje_error:str)-> int:
    patron = r'^[0-9+]?\d+$'
    if mensaje == "" or mensaje_error == "":
        print("Error, no se ingresaron parametros")
    else:
        while True:
            numero = input(mensaje)
            if re.match(patron,numero):
                return int(numero)
            else:
                print(mensaje_error)

def obtener_texto(mensaje:str,mensaje_error:str)-> str:
    patron = r'^[a-zA-Z +]?\d+$'
    if mensaje == "" or mensaje_error == "":
        print("Error, no se ingresaron parametros")
    else:
        while True:
            numero = input(mensaje)
            if re.match(patron,numero):
                return numero
            else:
                print(mensaje_error)

def validar_estadisticas(estadisticas:list, estadistica:str)->bool:
    if len(estadisticas) == 0:
        print("No se ingresaron estadisticas")
    else:
        for estadistica in estadisticas:
            if estadistica != estadistica:
                return False
            else:
                return True

def listar_jugadores_con_indice(dict_jugadores:dict):
    lista_jugadores = dict_jugadores["jugadores"]
    indice_jugador = -1
    if len(lista_jugadores) > 0:
        print("______________________________________________________________")
        for jugador in lista_jugadores:
            indice_jugador += 1
            print("|Id: {0}\t\t|Nombre: {1}| Posicion: {2}|".format(indice_jugador,jugador["nombre"].center(20), jugador["posicion"].center(20)))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    else:
        print("No hay jugadores en la lista") 


def obtener_jugador(dict_jugadores:dict,nombre_jugador:str=""):
    retorno = None
    patron = r"^[a-zA-Z]+"
    lista_jugadores = dict_jugadores["jugadores"]
    if lista_jugadores == [] or nombre_jugador == "":

        print("Error, lista o nombre invalidos")
    else:
        for jugador in lista_jugadores:
            if re.findall(patron,jugador["nombre"])[0] == nombre_jugador:
                retorno = jugador
                break
    
    if retorno:
        return retorno
    else:
        print("Error, jugador invalido")

def imprimir_menu():
    print("_____________________________________________________________________________________________________________________________________")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Seleccionar un jugador por su índice y mostrar sus estadísticas completas")
    print("3. Guardar las estadísticas de un jugador seleccionado en un archivo CSV")
    print("4. Buscar un jugador por su nombre y mostrar sus logros")
    print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team")
    print("6. Verificar si un jugador es miembro del Salón de la Fama del Baloncesto")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo")
    print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales")
    print("10. Mostrar los jugadores que han promediado más puntos por partido que un valor dado")
    print("11. Mostrar los jugadores que han promediado más rebotes por partido que un valor dado")
    print("12. Mostrar los jugadores que han promediado más asistencias por partido que un valor dado")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales")
    print("15. Mostrar los jugadores que han tenido un porcentaje de tiros libres superior a un valor dado")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18. Mostrar los jugadores que han tenido un porcentaje de tiros triples superior a un valor dado")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20. Mostrar los jugadores que han tenido un porcentaje de tiros de campo superior a un valor dado")
    print("21. Calcular el ranking de puntos de cada jugador")
    print("22. Calcular el ranking de rebotes de cada jugador")
    print("23. Calcular el ranking de asistencias de cada jugador")
    print("24. Calcular el ranking de robos de cada jugador")
    print("25. Exportar rankings a un archivo CSV")
    print("0. Salir del programa")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
