from funciones_parcial import *
os.system("cls" if os.name=="nt" else "clear")
lista_dt = leer_json("dt.json")

# 1
def listar_jugadores(dict_jugadores:dict):
    lista_jugadores = dict_jugadores["jugadores"]
    if len(lista_jugadores) > 0:
        print("______________________________________________________________")
        for jugador in lista_jugadores:
            print("|Nombre: {0}| Posicion: {1}|".format(jugador["nombre"].center(20), jugador["posicion"].center(20)))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    else:
        print("No hay jugadores en la lista")

  
#2
def estadisticas_jugador(dict_jugadores:dict,indice:int)-> list:
    lista_estadisticas = []
    lista_jugadores = dict_jugadores["jugadores"]
    if indice > len(lista_jugadores):
        print("El índice del jugador está fuera de rango")
    else:
        jugador = lista_jugadores[indice]
        estadisticas = jugador["estadisticas"]
        print("_________________________________________")
        print("|Nombre: {0}\t\t|".format(jugador["nombre"]))
        print("|Posicion: {0}\t\t\t|".format(jugador["posicion"]))
        print("|Temporadas: {0}\t\t\t\t|".format(estadisticas["temporadas"]))
        print("|Puntos totales: {0}\t\t\t|".format(estadisticas["puntos_totales"]))
        print("|Promedio de puntos por partido: {0}   |".format(estadisticas["promedio_puntos_por_partido"]))
        print("|Rebotes totales: {0}\t\t\t|".format(estadisticas["rebotes_totales"]))
        print("|Promedio de rebotes por partido: {0}\t|".format(estadisticas["promedio_rebotes_por_partido"]))
        print("|Asistencias totales: {0}\t\t|".format(estadisticas["asistencias_totales"]))
        print("|Robos totales: {0}\t\t\t|".format(estadisticas["robos_totales"]))
        print("|Bloqueos totales: {0}\t\t\t|".format(estadisticas["bloqueos_totales"]))
        print("|Porcentaje tiros de campo: {0}\t\t|".format(estadisticas["porcentaje_tiros_de_campo"]))
        print("|Porcentaje tiros libres: {0}\t\t|".format(estadisticas["porcentaje_tiros_libres"]))
        print("|Porcentaje tiros triples: {0}\t\t|".format(estadisticas["porcentaje_tiros_triples"]))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        lista_estadisticas.append(estadisticas)
    if lista_estadisticas != []:
        return lista_estadisticas
    else:
        print("Error, las estadisticas no existen")
#3
def exportar_estadisticas_csv(estadisticas:list,jugador:dict):
    archivo_csv = "estadisticas_jugadores/estadisticas_{0}.csv".format(jugador["nombre"]).replace(" ","_").lower()
    if len(estadisticas) > 0:
        with open(archivo_csv,"w") as archivo:
            archivo.write("nombre_jugador,posicion_posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n")
            for estadistica in estadisticas:
                archivo.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(jugador["nombre"],jugador["posicion"],estadistica["temporadas"],estadistica["puntos_totales"],estadistica["promedio_puntos_por_partido"],estadistica["rebotes_totales"],estadistica["promedio_rebotes_por_partido"],estadistica["asistencias_totales"],estadistica["robos_totales"],estadistica["bloqueos_totales"],estadistica["porcentaje_tiros_de_campo"],estadistica["porcentaje_tiros_libres"],estadistica["porcentaje_tiros_triples"]))
    else:
        print("Error, no se ingresaron estadisticas")
#4
def logros_jugadores(dict_jugadores:dict, nombre_jugador:str):
    jugador_encontrado = None
    lista_jugadores = dict_jugadores["jugadores"]
    patron = r"^[a-zA-Z]+"
    for jugador in lista_jugadores:
        if re.findall(patron,jugador["nombre"])[0] == nombre_jugador.capitalize():
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

def calcular_estadisticas(dict_jugadores:dict,estadistica:str,min_max:str)-> dict:
    lista_jugadores = dict_jugadores["jugadores"]
    if not lista_jugadores or not estadistica or not min_max:
        print("Error, datos invalidos")
    
    if min_max != "min" and min_max != "max":
        print("Error, no se pudo obtener ninguna estadística mínima o máxima")

    aux_jugador = None
    for jugador in lista_jugadores:
        if not aux_jugador:
            aux_jugador = jugador
        else:
            if min_max == "min":
                if jugador["estadisticas"][estadistica] < aux_jugador["estadisticas"][estadistica]:
                    aux_jugador = jugador
            elif min_max == "max":
                if jugador["estadisticas"][estadistica] > aux_jugador["estadisticas"][estadistica]:
                    aux_jugador = jugador
    return aux_jugador





resultado_estadisticas_jugador = []

opcion = None
while opcion != 0:
    imprimir_menu()
    opcion = obtener_numero_entero("Ingrese una opcion: ","Error, no se ingreso un entero :(")
    if opcion == 1:
        listar_jugadores(lista_dt)
        input("Presione key para continuar...")
    elif opcion == 2:
        listar_jugadores_con_indice(lista_dt)
        indice = obtener_numero_entero("Ingrese el indice del jugador: ","Error, indice invalido")
        resultado_estadisticas_jugador = estadisticas_jugador(lista_dt,indice)
    elif opcion == 3:
        if resultado_estadisticas_jugador:
            exportar_estadisticas_csv(resultado_estadisticas_jugador,lista_dt["jugadores"][indice])
            print("Estadisticas guardadas correctamente..")
            input("Presione key para continuar...")
        else:
            print("No se eligio un jugador")
    elif opcion == 4:
        nombre_jugador = input("Ingrese el nombre del jugador: ")
        logros_jugadores(lista_dt,nombre_jugador.capitalize())
    elif opcion == 5:
        resultado = promedio_puntos_por_partido(lista_dt)
        print("El promedio de los puntos por partido es: {0:.2f}".format(resultado))
    elif opcion == 6:
        listar_jugadores(lista_dt)
        nombre_jugador = input("Ingrese el nombre del jugador: ")
        resultado = obtener_jugador(lista_dt,nombre_jugador.capitalize())
        validar_salon_fama(resultado)
    elif opcion == 7:
        jugador_resultado = calcular_estadisticas(lista_dt,"rebotes_totales","max")
        print("El jugador con mayor cantidad de rebotes totales es: {0} y tiene {1:.0f}".format(jugador_resultado["nombre"],jugador_resultado["estadisticas"]["rebotes_totales"]))
    elif opcion == 8:
        jugador_resultado = calcular_estadisticas(lista_dt,"porcentaje_tiros_de_campo","max")
        print("El jugador con mayor el mayor porcentaje de tiros de campo es: {0} y tiene {1:.0f}".format(jugador_resultado["nombre"],jugador_resultado["estadisticas"]["porcentaje_tiros_de_campo"]))
    elif opcion == 9:
        jugador_resultado = calcular_estadisticas(lista_dt,"asistencias_totales","max")
        print("El jugador con mayor cantidad de asistencias totales es: {0} y tiene {1:.0f}".format(jugador_resultado["nombre"],jugador_resultado["estadisticas"]["asistencias_totales"]))
    elif opcion == 10:
        pass
    elif opcion == 11:
        pass
    elif opcion == 12:
        pass
    elif opcion == 13:
        pass
    elif opcion == 14:
        pass
    elif opcion == 15:
        pass
    elif opcion == 16:
        pass
    elif opcion == 17:
        pass
    elif opcion == 18:
        pass
    elif opcion == 19:
        pass
    elif opcion == 20:
        pass
    elif opcion == 21:
        pass
    elif opcion == 22:
        pass
    elif opcion == 23:
        pass
    elif opcion == 0:
        print("Gracias por usar mi programa...")
        break
    else:
        print("Error, opcion invalida")