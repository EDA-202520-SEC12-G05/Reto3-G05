import time
import csv
import sys
import os
from datetime import datetime as dt

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-3'

from DataStructures.List import array_list as lt

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

    barrios_file = os.path.join(data_dir, "flights_large.csv")
    file = csv.DictReader(
            open(barrios_file, encoding = "utf-8"), delimiter =",")
    
    for record in file:

        record["id"] = int(record["id"])
        record["date"] = dt.strptime(record["date"], '%Y-%m-%d').date()
        record["dep_time"] = dt.strptime(record["dep_time"], "%H:%M").time()
        record["date_hour"] = dt.combine(record["date"], record["dep_time"])
        record["sched_dep_time"] = dt.strptime(record["sched_dep_time"], "%H:%M")
        record["arr_time"] = dt.strptime(record["arr_time"], "%H:%M").time()
        record["sched_arr_time"] = dt.strptime(record["sched_arr_time"], "%H:%M")
        record["num_flight"] = int(record["flight"])
        record["airtime"] = float(record["air_time"])
        record["distance"] = float(record["distance"])

        lt.add_last(catalog["flights"], record)

    lt.quick_sort(catalog["flights"], cmp_f)
    tf = get_time()
    
    return catalog["flights"]["elements"], catalog["flights"]["size"], round(delta_time(ti, tf), 4)

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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
def cmp_f(reg1, reg2):
    return reg1["date_hour"] < reg2["date_hour"]

