from funciones_parcial import *
os.system("clear")
lista_dt = leer_json("dt.json")
#1
def listar_jugadores(lista_jugaodres:list):
    if len(lista_jugaodres) > 0:
        for jugador in lista_jugaodres["jugadores"]:
            print("Nombre: {0} Posicion: {1}".format(jugador["nombre"], jugador["posicion"]))
    else:
        print("No hay jugadores en la lista")
#2
def estadisticas_jugador(lista_jugadores:list,indice:int)-> list:
    lista_estadisticas = []
    if indice < len(lista_jugadores["jugadores"]):
        jugador = lista_jugadores["jugadores"][indice]
        estadisticas = jugador["estadisticas"]
        print("Nombre: {0} | Posicion: {1}".format(jugador["nombre"], jugador["posicion"]))
        print("Temporadas: {0}".format(estadisticas["temporadas"]))
        print("Puntos totales: {0}".format(estadisticas["puntos_totales"]))
        print("Promedio de puntos por partido: {0}".format(estadisticas["promedio_puntos_por_partido"]))
        print("Rebotes totales: {0}".format(estadisticas["rebotes_totales"]))
        print("Promedio de rebotes por partido: {0}".format(estadisticas["promedio_rebotes_por_partido"]))
        print("Asistencias totales: {0}".format(estadisticas["asistencias_totales"]))
        print("Robos totales: {0}".format(estadisticas["robos_totales"]))
        print("Bloqueos totales: {0}".format(estadisticas["bloqueos_totales"]))
        print("Porcentaje tiros de campo: {0}".format(estadisticas["porcentaje_tiros_de_campo"]))
        print("Porcentaje tiros libres: {0}".format(estadisticas["porcentaje_tiros_libres"]))
        print("Porcentaje tiros triples: {0}".format(estadisticas["porcentaje_tiros_triples"]))

        lista_estadisticas.append(estadisticas)
    else:
        print("El índice del jugador está fuera de rango")
    return lista_estadisticas
#3
def exportar_estadisticas_csv(estadisticas:list,jugador:dict):
    archivo_csv = "estadisticas_jugadores/estadisticas_{0}.csv".format(jugador["nombre"]).replace(" ","_").lower()
    if len(estadisticas) > 0:
        with open(archivo_csv,"w") as archivo:
            archivo.write("nombre_jugador,posicion_posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n")
            for estadistica in estadisticas:
                archivo.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(jugador["nombre"],jugador["posicion"],estadistica["temporadas"],estadistica["puntos_totales"],estadistica["promedio_puntos_por_partido"],estadistica["rebotes_totales"],estadistica["promedio_rebotes_por_partido"],estadistica["asistencias_totales"],estadistica["robos_totales"],estadistica["bloqueos_totales"],estadistica["porcentaje_tiros_de_campo"],estadistica["porcentaje_tiros_libres"],estadistica["porcentaje_tiros_triples"]))
#4
def logros_jugadores(lista_jugadores:list, nombre_jugador:str):
    retorno = []
    jugador_encontrado = None
    for jugador in lista_jugadores["jugadores"]:
        if re.findall(r"^[a-zA-Z]+",jugador["nombre"])[0] == nombre_jugador:
            jugador_encontrado = jugador
            break
    if jugador_encontrado != None:
        print("Logros del jugador: ",jugador_encontrado["nombre"])
        for logro in jugador_encontrado["logros"]:
            print(logro)
    else:
        print("No se encontró el jugador")
#5 
def promedio_puntos_por_partido(lista_jugadores:list)-> float:
    acumulador_promedios = 0
    contador_promedios = 0
    for jugador in lista_jugadores["jugadores"]:
        acumulador_promedios += jugador["estadisticas"]["promedio_puntos_por_partido"]
        contador_promedios += 1
    promedio = acumulador_promedios / contador_promedios
    return promedio

#6
def validar_salon_fama(jugador:dict):
    flag_salon_de_la_fama = False

    if not jugador:
        print("Error, jugador invalido")
    else:
        for logros in jugador["logros"]:
            if re.findall("Miembro del Salon de la Fama del Baloncesto$",logros):
                flag_salon_de_la_fama = True

    if flag_salon_de_la_fama:
        print("El jugador {0} si pertenece al salon de la fama! ".format(jugador["nombre"]))
    else:
        print("El jugador {0} no pertenece al salon de la fama! ".format(jugador["nombre"]))


def obtener_jugador(lista_jugador:list=[],nombre_jugador:str=""):
    retorno = None
    if lista_jugador == [] or nombre_jugador == "":

        print("Error, lista o nombre invalidos")
    else:
        for jugador in lista_jugador["jugadores"]:
            if re.findall(r"^[a-zA-Z]+",jugador["nombre"])[0] == nombre_jugador:
                retorno = jugador
                break
    
    if retorno:
        return retorno
    else:
        print("Error, jugador invalido")

def calcular_estadisticas(lista_jugadores:list,estadistica:float,min_max:str)-> float:
    retorno = 0
    aux_estadistica_min = 9999999
    aux_estadistica_max = 0
    
    if lista_jugadores == [] or estadistica < 0 or min_max == " " :
        print("Error, lista, estadisitica u orden invalido")
    else:
        for jugador in lista_jugadores["jugadores"]:
            if min_max == "min":
                if jugador["estadisticas"][estadistica] < aux_estadistica_min:
                    aux_estadistica_min = jugador["estadisticas"][estadistica]
                else:
                    aux_estadistica_max = jugador["estadisticas"][estadistica]

# listar_jugadores(lista_dt)

# resultado = promedio_puntos_por_partido(lista_dt)

# print("El promedio de los puntos por partido es: {0:.2f}".format(resultado))

nombre_jugador = input("Ingrese el nombre del jugador: ")
resultado = obtener_jugador(lista_dt,nombre_jugador.capitalize())

validar_salon_fama(resultado)

# while opcion != 0:
#     imprimir_menu()
#     opcion = int(input("Ingrese una opcion"))
#     if opcion == 1:
#         listar_jugadores(lista_dt)
#     elif opcion == 2:
#         listar_jugadores(lista_dt)
#         indice = int(input("Ingrese el indice del jugador: "))
#         resultado = estadisticas_jugador(lista_dt,indice)
#     elif opcion == 3:
#         exportar_estadisticas_csv(resultado,lista_dt["jugadores"][indice])
#     elif opcion == 4:
#         nombre_jugador = input("Ingrese el nombre del jugador: ")
#         logros_jugadores(lista_dt,nombre_jugador)
#     elif opcion == 5:
#         resultado = promedio_puntos_por_partido(lista_dt)
#         print("El promedio de los puntos por partido es: {0:.2f}".format(resultado))
#     elif opcion == 6:
#         nombre_jugador = input("Ingrese el nombre del jugador: ")
