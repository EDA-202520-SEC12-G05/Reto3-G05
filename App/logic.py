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
                #5. Añadir al bst con la llave siendo tupla (delay, date_hour) para que se encargue de organizarlos él solito
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


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


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
    return reg1["date_hour_arr"] < reg2["date_hour_arr"]

def min_dif(fecha, hreal, hsch):

    h_real = dt.combine(fecha, hreal)
    h_sch = dt.combine(fecha, hsch)

    if h_real < h_sch: #Pasó medianoche
        h_real += td(days=1) #Ajuste de 1 día para comparar bien

    return (h_real - h_sch).total_seconds() / 60

def format_rango(rango):
    #Convierte rangos en strings en formato "[num1, num2]" a tupla para req 1

    rango = rango.strip("[]").replace(" ", "")   # quita corchetes (y espacios por si acaso)
    l_rango = rango.split(",") 

    return (int(l_rango[0]), int(l_rango[1]))


