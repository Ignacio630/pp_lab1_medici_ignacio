from funciones_parcial import *
os.system("cls" if os.name=="nt" else "clear")
lista_dt = leer_json("dt.json")

# 1
def listar_jugadores(dict_jugadores:dict):
    """
    Lista el nombre y posicion de los jugadores
    
    Parametros:
    dict_jugadores:dict = Diccionario con los jugadores
    """
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
    """
    Muestra y devuelve las estadisticas del jugador seleccionado
    
    Parametros:
    dict_jugadores:dict = Diccionario con los jugadores
    indice:int = Indice del jugador
    Devuelve:
    lista_estadisticas:list: Lista de las estadisticas del jugador seleccionado
    """
    
    
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
    """
    Exporta a un archivo csv con las estadisticas del jugador
    
    Parametros:
    dict_jugadores:dict = Diccionario con los jugadores
    jugador:dict = Jugador
    """
    archivo_csv = "estadisticas_jugadores/estadisticas_{0}.csv".format(jugador["nombre"]).replace(" ","_").lower()
    if len(estadisticas) > 0:
        with open(archivo_csv,"w") as archivo:
            archivo.write("nombre_jugador,posicion_posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n")
            for estadistica in estadisticas:
                archivo.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(jugador["nombre"],jugador["posicion"],estadistica["temporadas"],estadistica["puntos_totales"],estadistica["promedio_puntos_por_partido"],estadistica["rebotes_totales"],estadistica["promedio_rebotes_por_partido"],estadistica["asistencias_totales"],estadistica["robos_totales"],estadistica["bloqueos_totales"],estadistica["porcentaje_tiros_de_campo"],estadistica["porcentaje_tiros_libres"],estadistica["porcentaje_tiros_triples"]))
    else:
        print("Error, no se ingresaron estadisticas")

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

def promedio_estadistica(dict_jugadores:dict,estadistica:str)-> float:
    lista_jugadores = dict_jugadores["jugadores"]
    acumulador_promedios = 0
    contador_promedios = 0
    for jugador in lista_jugadores:
        acumulador_promedios += jugador["estadisticas"][estadistica]
        contador_promedios += 1
    promedio = acumulador_promedios / contador_promedios
    return promedio

#6
def validar_salon_fama(jugador:dict):
    """
    Valida y muestra si el jugador pasado por parametros esta en el salon de la fama 
    
    Parametro:
    jugador:dict = Jugador
    
    """
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

def estadistica_por_partido(dict_jugadores:dict,estadistica:str,valor:int):
    listar_jugadores = dict_jugadores["jugadores"]
    aux_max_estadistica = []
    
    if not dict_jugadores or not estadistica or not valor:
        print("Error al cargar los parametros")
    
    for jugador in listar_jugadores:
        if valor < jugador["estadisticas"][estadistica]:
            aux_max_estadistica.append(jugador)
    
    if not aux_max_estadistica:
        print("Error, no se encontraron jugadores con un {0} inferior a {1}".format(re.sub("_"," ",estadistica),valor))
    else:
        print("Los jugadores con mas puntos en la estadistica {0} por partido que el valor son: {1}".format(re.sub("_"," ",estadistica),valor))
        for jugador in aux_max_estadistica:
            print("|Nombre: {0} con un {1} de {2}".format(jugador["nombre"],re.sub("_"," ",estadistica),jugador["estadisticas"][estadistica]))

# Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.

def lista_jugadores_con_valor_inferior(dict_jugadores:dict,estadistica:str,valor:float)->list:
    lista_jugadores = dict_jugadores["jugadores"]
    aux_lista_jugadores = []
    
    if not dict_jugadores or not estadistica or not valor:
        print("Error al cargar los parametros")

    for jugador in lista_jugadores:
        if jugador["estadisticas"][estadistica] < valor:
            aux_lista_jugadores.append(jugador)
    
    if not aux_lista_jugadores:
        print("Error, no se encontraron jugadores con un {0} inferior a {1}".format(re.sub("_"," ",estadistica),valor))
    else:
        return aux_lista_jugadores

def promedio_puntos_por_partido_excluyendo_menor(dict_jugadores:dict,estadistica:str,valor:float):
    lista_jugadores = dict_jugadores["jugadores"]
    aux_lista_jugadores = []
    acumulador_estadistica = 0
    
    if not dict_jugadores or not estadistica or not valor:
        print("Error al cargar los parametros")

    jugador_con_peor_promedio = calcular_estadisticas(dict_jugadores,estadistica,"min")
    print(jugador_con_peor_promedio)

    for jugador in lista_jugadores:
        if jugador["nombre"] != jugador_con_peor_promedio["nombre"]:
            aux_lista_jugadores.append(jugador)
    if not aux_lista_jugadores:
        print("Error, no se encontraron jugadores con un {0} inferior a {1}".format(re.sub("_"," ",estadistica),valor))
    else:
        print("El promedio de puntos en la estadistica {0} por partido que el valor son: {1}".format(re.sub("_"," ",estadistica),valor))
        for jugador in aux_lista_jugadores:
            acumulador_estadistica += jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedio_puntos_por_partido_equipo = acumulador_estadistica / len(aux_lista_jugadores)
        
        print("El promedio de puntos por partido del equipo es: {0:.2f}".format(promedio_puntos_por_partido_equipo))
        print("El jugador excluido es: {0} con un promedio de {1}".format(jugador_con_peor_promedio["nombre"], jugador_con_peor_promedio["estadisticas"]["promedio_puntos_por_partido"]))
    


def calcular_logros(dict_jugadores:dict)-> int:
    
    if not dict_jugadores:
        print("Error, parametros invalidos")
    lista_jugadores = dict_jugadores["jugadores"]
    contador_logros_max = 0
    jugador_logros_max = {}
    for jugador in lista_jugadores: 
        if contador_logros_max < len(jugador["logros"]):
            contador_logros_max = len(jugador["logros"])
            jugador_logros_max = jugador
    print("El jugador con la mayor cantidad de logros es {} con {} logros".format(jugador_logros_max["nombre"],contador_logros_max))

opcion = None
promedio_puntos_por_partido_excluyendo_menor(lista_dt,"promedio_puntos_por_partido",10)
while opcion != 0:
    imprimir_menu()
    opcion = obtener_numero_entero("Ingrese una opcion: ","Error, no se ingreso un entero :(")
    
    if opcion == 1:
        listar_jugadores(lista_dt)
        input("Presione key para continuar...")
    elif opcion == 2:
        resultado_estadisticas_jugador = []
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
        resultado = promedio_estadistica(lista_dt,"promedio_puntos_por_partido")
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
        valor = obtener_numero_entero("Ingrese un valor: ","Error, valor invalido")
        print("Los jugadores con mas puntos en promedio de puntos por partido que el valor {0} son: ".format(valor))
        estadistica_por_partido(lista_dt,"promedio_puntos_por_partido",valor)
    elif opcion == 11:
        valor = obtener_numero_entero("Ingrese un valor: ","Error, valor invalido")
        print("Los jugadores con mas puntos en promedio de rebotes por partido que el valor {0} son: ".format(valor))
        estadistica_por_partido(lista_dt,"promedio_rebotes_por_partido",valor)
    elif opcion == 12:
        valor = obtener_numero_entero("Ingrese un valor: ","Error, valor invalido")
        print("Los jugadores con mas puntos en promedio de asistencias por partido que el valor {0} son: ".format(valor))
        estadistica_por_partido(lista_dt,"promedio_asistencias_por_partido",valor)
    elif opcion == 13:
        jugador_resultado = calcular_estadisticas(lista_dt,"robos_totales","max")
        print("El jugador con mayor cantidad de robos totales es: {0} y tiene {1:.0f}".format(jugador_resultado["nombre"],jugador_resultado["estadisticas"]["robos_totales"]))
    elif opcion == 14:
        jugador_resultado = calcular_estadisticas(lista_dt,"bloqueos_totales","max")
        print("El jugador con mayor cantidad de bloqueos totales es: {0} y tiene {1:.0f}".format(jugador_resultado["nombre"],jugador_resultado["estadisticas"]["bloqueos_totales"]))
    elif opcion == 15:
        valor = obtener_numero_entero("Ingrese un valor: ","Error, valor invalido")
        print("Los jugadores con mas puntos en porcentaje de tiros libres por partido que el valor {0} son: ".format(valor))
        estadistica_por_partido(lista_dt,"porcentaje_tiros_libres",valor)
    elif opcion == 16:
        promedio_puntos_por_partido_excluyendo_menor(lista_dt,"promedio_puntos_por_partido",10)
    elif opcion == 17:
        calcular_logros(lista_dt)
    elif opcion == 18:
        valor = obtener_numero_entero("Ingrese un valor: ","Error, valor invalido")
        estadistica_por_partido(lista_dt,"porcentaje_tiros_triples",valor)
    elif opcion == 19:
        jugador_resultado = calcular_estadisticas(lista_dt,"temporadas","max")
        print("El jugador con mayor cantidad de temporadas es: {0} y tiene {1:.0f}".format(jugador_resultado["nombre"],jugador_resultado["estadisticas"]["temporadas"]))
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