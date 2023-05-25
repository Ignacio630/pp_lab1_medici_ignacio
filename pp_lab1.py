from funciones_parcial import *
os.system("clear")
lista_dt = leer_json("dt.json")

def listar_jugadores(lista_jugaodres:list):
    if len(lista_jugaodres) > 0:
        for jugador in lista_jugaodres["jugadores"]:
            print("Nombre: {0} Posicion: {1}".format(jugador["nombre"], jugador["posicion"]))
    else:
        print("No hay jugadores en la lista")

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

def exportar_estadisticas_csv(estadisticas:list,jugador:dict):
    if len(estadisticas) > 0:
        with open("estadisticas.csv","w") as archivo:
            archivo.write("nombre_jugador,posicion_posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n")
            for estadistica in estadisticas:
                archivo.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(jugador["nombre"],jugador["posicion"],estadistica["temporadas"],estadistica["puntos_totales"],estadistica["promedio_puntos_por_partido"],estadistica["rebotes_totales"],estadistica["promedio_rebotes_por_partido"],estadistica["asistencias_totales"],estadistica["robos_totales"],estadistica["bloqueos_totales"],estadistica["porcentaje_tiros_de_campo"],estadistica["porcentaje_tiros_libres"],estadistica["porcentaje_tiros_triples"]))



# listar_jugadores(lista_dt)
indice = int(input("Ingrese el indice del jugador: "))
resultado = estadisticas_jugador(lista_dt,indice)
exportar_estadisticas_csv(resultado,lista_dt["jugadores"][indice])


