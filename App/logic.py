import time
import csv
import sys
import os
from datetime import datetime as dt
from datetime import timedelta as td

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-3'

from DataStructures.List import array_list as lt
from DataStructures.Tree.BSTree import binary_search_tree as bst

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"flights": lt.new_list()}
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    ti = get_time()

    data_file = os.path.join(data_dir, "flights_large.csv")
    file = csv.DictReader(
            open(data_file, encoding = "utf-8"), delimiter =",")
    
    for record in file:
        record["id"] = int(record["id"])
        record["date"] = dt.strptime(record["date"], '%Y-%m-%d').date()
        record["dep_time"] = dt.strptime(record["dep_time"], "%H:%M").time()
        record["date_hour_dep"] = dt.combine(record["date"], record["dep_time"])
        record["sched_dep_time"] = dt.strptime(record["sched_dep_time"], "%H:%M").time()
        record["arr_time"] = dt.strptime(record["arr_time"], "%H:%M").time()
        record["date_hour_arr"] = dt.combine(record["date"], record["arr_time"])
        record["sched_arr_time"] = dt.strptime(record["sched_arr_time"], "%H:%M").time()
        record["delay"] = min_dif(record["date"], record["arr_time"], record["sched_arr_time"])
        record["num_flight"] = int(record["flight"])
        record["airtime"] = float(record["air_time"])
        record["distance"] = float(record["distance"])
        
        lt.add_last(catalog["flights"], record)

    lt.quick_sort(catalog["flights"], cmp_f_loadata)
    tf = get_time()
    
    return catalog["flights"]["elements"], catalog["flights"]["size"], round(delta_time(ti, tf), 4)

# Funciones de consulta sobre el catálogo


def req_1(catalog, cod_aerolinea, rango_min):

    ti = get_time()

    l_vuelos = catalog["flights"]["elements"]
    rango_min = format_rango(rango_min)

    arbol = bst.new_map()

    #Recorrido a l_vuelos O(n)
    for vuelo in l_vuelos:
        #1. Filtrar por aerolínea
        if vuelo["carrier"] == cod_aerolinea:
            #2. Calcular dif de min
            dif_min = min_dif(vuelo["date"], vuelo["dep_time"], vuelo["sched_dep_time"])
            #3. Validar si es retraso (if dif > 0) y si está dentro del rango
            if dif_min > 0 and rango_min[0] <= dif_min <= rango_min[1]:
                vuelo["delay"] = dif_min
                #5. Añadir al bst con la llave siendo tupla (delay, date_hour_dep) para que se encargue de organizarlos él solito
                llave = (vuelo["delay"], vuelo["date_hour_dep"])
                bst.put(arbol, llave, vuelo)

    #6. Sacar los values en una array list y mandar para el view
    resultado = bst.value_set(arbol)

    tf = get_time()

    return round(delta_time(ti, tf),4), resultado["size"], resultado["elements"]


def req_3(catalog, cod_al, cod_ap, rango_d):
    
    ti = get_time()
    l_vuelos = catalog["flights"]["elements"]
    rango_d = format_rango(rango_d)
    arbol = bst.new_map()

    for vuelo in l_vuelos:

        #Filtrar por aerolinea y aeropuero destino
        if vuelo["carrier"] == cod_al and vuelo["dest"] == cod_ap:
            #Filtrar por rango de distancia
            if  rango_d[0] <= vuelo["distance"] <= rango_d[1]:             
                    #Insertar al árbol según distancia o fecha y hora de llegada
                    llave = (vuelo["distance"], vuelo["date_hour_arr"])
                    bst.put(arbol, llave, vuelo)
    resultado = bst.value_set(arbol)
    tf = get_time()

    return round(delta_time(ti, tf),4), resultado["size"], resultado["elements"]


def req_4(catalog, r_fechas, f_horaria, n):
    
    ti = get_time()
    n = int(n)
    vuelos = catalog["flights"]["elements"]
    r_fechas = format_rango(r_fechas, "f")
    f_horaria = format_rango(f_horaria, "h")
    heap = hp.new_map(False)

    for vuelo in vuelos:
        if r_fechas[0]<= vuelo["date"] <= r_fechas[1]:
            if f_horaria[0] <= vuelo["dep_time"] <= f_horaria[1]:

                aerolineas = {
                    vuelo["carrier"]: {"num_vuelos": 0,
                                       "duracion": 0,
                                       "distancia": 0,
                                       "vuelo_min_d": vuelo,
                                       "codigo": vuelo["carrier"]}
                }

                #Si la aerolinea no está en el diccionario
                if vuelo["carrier"] not in aerolineas:
                    aerolineas[vuelo["carrier"]] = {"num_vuelos": 1,
                                                    "duracion": vuelo["airtime"],
                                                    "distancia": vuelo["distance"],
                                                    "vuelo_min_d": vuelo,
                                                    "codigo": vuelo["carrier"]}
                #Si la aerolinea ya existe en el diccionario
                if vuelo["carrier"] in aerolineas:
                    aerolineas[vuelo["carrier"]]["num_vuelos" ]+= 1
                    aerolineas[vuelo["carrier"]]["duracion"] += vuelo["airtime"]
                    aerolineas[vuelo["carrier"]]["distancia"] += vuelo["distance"]
                    if vuelo["airtime"] < aerolineas[vuelo["carrier"]["vuelo_min_d"]]:
                        aerolineas[vuelo["carrier"]]["vuelo_min_d"] = vuelo

    for codigo in aerolineas.values():
        codigo["duracion"] = codigo["duracion"]/codigo["num_vuelos"]
        codigo["distancia"] = codigo["distance"]/codigo["num_vuelos"]
        #Insertar en heap para ordenar de forma descendente
        heap = hp.insert(heap, codigo["num_vuelos"], codigo)

    lista = []
    i = 0

    while not i == n:
        elem = hp.remove(heap)
        lista.append(elem)
        i += 1
    tf = get_time()
    
    return lista, delta_time(ti,tf)

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_5(catalog, rango_f, cod, n):

    ti = get_time()

    #1. Formatear
    rango_f = format_rango(rango_f, "f")
    n = int(n)
    vuelos = catalog["flights"] #Array_list!!!
    aerolineas = {}
    arbol = bst.new_map()
    #2. Aplicar filtros
    for vuelo in vuelos["elements"]:#O(n)
        if rango_f[0] <= vuelo["date"] <= rango_f[1] and vuelo["dest"] == cod:
        #4. Añadir al dict de aerolineas (normal)
            car = vuelo["carrier"]
            if car not in aerolineas:
                #4.1. Llevar cuenta de: Puntualidad, vuelos, distancia, duración, y elegir el vuelo de mayor distancia
                aerolineas[car] = {"Aerolínea": (f"{vuelo['carrier']} - {vuelo['name']}"), 
                                         "Puntualidad": vuelo['delay'],
                                         "Cantidad de vuelos": 1,
                                         "Duración Promedio": vuelo['airtime'],
                                         "Distancia Promedio": vuelo['distance'],
                                         "Vuelo de mayor distancia": vuelo}
            else:
                aerolineas[car]['Puntualidad'] += vuelo["delay"]
                aerolineas[car]['Cantidad de vuelos'] += 1
                aerolineas[car]['Duración Promedio'] += vuelo["airtime"]
                aerolineas[car]['Distancia Promedio'] += vuelo['distance']

                if vuelo['distance'] > aerolineas[car]["Vuelo de mayor distancia"]['distance']:
                    aerolineas[car]['Vuelo de mayor distancia'] = vuelo

    #Por si ninguna paso el filtro
    if not aerolineas:
        return None

    #5. Promedios y etc
    for aer in aerolineas.keys(): #O(a)
        aerolinea = aerolineas[aer]
        if aerolinea and aerolinea["Cantidad de vuelos"] > 0:
            aerolinea["Puntualidad"] = aerolinea["Puntualidad"]/aerolinea["Cantidad de vuelos"]
            aerolinea["Duración Promedio"] = aerolinea["Duración Promedio"]/aerolinea["Cantidad de vuelos"]
            aerolinea["Distancia Promedio"] = aerolinea["Distancia Promedio"]/aerolinea["Cantidad de vuelos"]
            #Solo campos importantes para vmayor
            vuelom = aerolinea["Vuelo de mayor distancia"]
            if vuelom:
                aerolinea["Vuelo de mayor distancia"] = {"ID": vuelom['id'],
                                        "Codigo": vuelom['flight'],
                                        "Fecha de llegada": vuelom['date_hour_arr'],
                                        "Aeropuertos Origen y Destino": (vuelom['origin'], vuelom['dest']),
                                        "Duracion": vuelom['airtime']}
                #6. Meter al arbol con tupla (puntualidad, cod)
                key = (abs(aerolinea["Puntualidad"]), aer)
                arbol = bst.put(arbol, key, aerolinea)

    #7. Sacar value set
    values = bst.value_set(arbol) #Values -> Array_list!!!!
    #8. Sublist hasta N
    values = lt.sub_list(values, 0, n)
    #9. Retornar
    tf = get_time()
    return round(delta_time(ti, tf), 4), values["size"], values["elements"]


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

#Auxiliares
def cmp_f_loadata(reg1, reg2):
    return reg1["date_hour_dep"] < reg2["date_hour_dep"]

def min_dif(fecha, hreal, hsch):
    h_real = dt.combine(fecha, hreal)
    h_sch = dt.combine(fecha, hsch)
    dif = (h_real - h_sch).total_seconds() / 60

    # Si la diferencia es muy grande en negativo, probablemente pasó medianoche
    if dif < -720:  # -12 horas, margen de seguridad
        dif += 1440  # sumar un día

    return dif

def format_rango(rango, tipo="n"):
    #Convierte rangos en strings en formato "[num1, num2]" o "[fecha1, fecha2]" a tupla 

    rango = rango.strip("[]").replace(" ", "")   # quita corchetes (y espacios por si acaso)
    l_rango = rango.split(",") 
    #Si necesita formatear fecha
    if tipo == "f":
        return (dt.strptime(l_rango[0], '%Y-%m-%d').date(), dt.strptime(l_rango[1], '%Y-%m-%d').date()) 
    #Si formatea hora
    if tipo == "h":
        return (dt.strptime(l_rango[0], "%H:%M").time(), dt.strptime(l_rango[1], "%H:%M").time())
    #Por default viene para formatear números
    return (int(l_rango[0]), int(l_rango[1]))