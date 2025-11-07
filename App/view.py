import sys
from App import logic as lg
from tabulate import tabulate as tab


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = lg.new_logic()

    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    return lg.load_data(control)

def print_records(records, n):
    
    if n < 0:
        records_imprimir = records[n:]       
    else:
        records_imprimir = records[:n]      
    
    filas = []
    for record in records_imprimir:
        filas.append([
            record["date"],
            record["dep_time"],
            record["arr_time"],
            f"{record['carrier']} - {record['name']}",
            record["tailnum"],
            f"[{record['origin']} - {record['dest']}]",
            record["air_time"],
            record["distance"]])

    headers = ["Fecha", "Hora Real de Salida", "Hora Real de llegada", "Aerolínea", "ID Aeronave", "Aeropuerto Origen y Aeropuerto 12xDestino", "Duración", "Distancia"]
    
    print(tab(filas, headers=headers, tablefmt="rounded_grid"))

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            if data:
                records, cant, time = data
                print(f"Tiempo de carga: {time}")
                print(f"Total de vuelos cargados: {cant}")
                print("Primeros 5 vuelos registrados:")
                print_records(records, 5)
                print("Últimos 5 vuelos registrados:")
                print_records(records, -5)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
