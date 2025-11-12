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
            record["id"],
            record["id"],
            record["date"],
            record["dep_time"],
            record["arr_time"],
            f"{record['carrier']} - {record['name']}",
            record["tailnum"],
            f"[{record['origin']} - {record['dest']}]",
            record["air_time"],
            record["distance"]])

    headers = ["ID", "Fecha", "Hora Real de Salida", "Hora Real de llegada", "Aerolínea", "ID Aeronave", "Aeropuerto Origen y Destino", "Duración (min)", "Distancia (mi)"]

    print(tab(filas, headers=headers, tablefmt="rounded_grid"))

#Función general y adaptada para imprimir lo q se necesite
def print_table(records, n, headers=None, columnas=None, ver = False):

    """Recibe una lista de strings en columnas, 
       que incluye los nombres de las llaves que interesa mostrar.
       Itera sobre la lista y busca directamente en los records la 
       llave que se necesita y lo mete a la lista de filas a mostrar.

       Y ya pq en cada requerimiento piden una baina distinta Dios
    """
    if n < 0:
        records_imprimir = records[n:]       
    else:
        records_imprimir = records[:n]   

    #Opción para imprimir en vertical
    if ver:
        filas = []
        for record in records:
            filas.extend(list(record.items()))
            filas.append(("", ""))  # separador visual

        print(tab(filas, tablefmt="fancy_grid"))

    else:
        filas = []
        for record in records_imprimir:
            fila = []
            for col in columnas:
                fila.append(record[col])
            filas.append(fila)
        print(tab(filas, headers=headers, tablefmt="rounded_grid"))

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, codigo, rango):

    resultado = lg.req_1(control, codigo, rango)

    if resultado:
        tiempo, cant, records = resultado
        print(f"\tTiempo total de ejecución: {tiempo}")
        print(f"\tNúmero total de vuelos que cumplen con los filtros: {cant}")

        #Setup de headers y columnas para print_table
        headers = ["ID", "Código", "Fecha", "Nombre de Aerolínea", "Código de Aerolínea", "Aeropuerto Origen", "Aeropuerto Destino", "Minutos de Retraso"]
        columnas = ["id", "flight", "date", "name", "carrier", "origin", "dest", "delay"]

        #Verificación de tamaño de muestra
        if cant > 10:
            print("\nPrimeros 5 registros encontrados: ")
            print_table(records, 5, headers, columnas)
            print("\nÚltimos 5 registros encontrados: ")
            print_table(records, -5, headers, columnas)
        else:
            print_table(records, cant, headers, columnas)
    else:
        print("\nNo se hallaron registros que coincidieran con la búsqueda.")
        print("\n")


def print_req_3(control, cod_al, cod_ap, rango_d):

    resultado = lg.req_3(control, cod_al, cod_ap, rango_d)

    if resultado:
        tiempo, cant, records = resultado
        print(f"\tTiempo total de ejecución: {tiempo}")
        print(f"\tNúmero total de vuelos que cumplen con los filtros: {cant}")

        #Setup de headers y columnas para print_table
        headers = ["ID", "Código", "Fecha y hora de llegada", "Nombre de aerolínea", "Código de aerolínea", "Aeropuerto Orígen", "Aeropuerto Destino", "Distancia Total"]
        columnas = ["id", "flight", "date_hour_arr", "name", "carrier", "origin", "dest", "distance"]

        #Verificación de tamaño de muestra
        if cant > 10:
            print("\nPrimeros 5 registros encontrados: ")
            print_table(records, 5, headers, columnas)
            print("\nÚltimos 5 registros encontrados: ")
            print_table(records, -5, headers, columnas)
        else:
            print_table(records, cant, headers, columnas)
    else:
        print("\nNo se hallaron registros que coincidieran con la búsqueda.")
        print("\n")

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_6(control, rf, rd, n):

    resultado = lg.req_6(control, rf, rd, n)

    if resultado:
        tiempo, cant, records = resultado
        print(f"\tTiempo total de ejecución: {tiempo}")
        print(f"\tNúmero total de aerolíneas consideradas: {cant}")

        #FORMATEO PARA IMPRIMIR VUELOM
        for aerolin in records:
            aerolin["Vuelo con el retraso más cercano al promedio"] = tab(aerolin["Vuelo con el retraso más cercano al promedio"].items(), tablefmt="simple_grid")
        
        print_table(records, cant, ver=True)

    else:
        print("\nNo se hallaron registros que coincidieran con la búsqueda.")
        print("\n")


def print_req_5(control, rango_f, cod, n):

    resultado = lg.req_5(control, rango_f, cod, n)

    if resultado:
        tiempo, cant, records = resultado
        print(f"\tTiempo total de ejecución: {tiempo}")
        print(f"\tNúmero total de aerolíneas consideradas: {cant}")

        #FORMATEO PARA IMPRIMIR VUELOM
        for aerolin in records:
            aerolin["Vuelo de mayor distancia"] = tab(aerolin["Vuelo de mayor distancia"].items(), tablefmt="simple_grid")
        

        print_table(records, cant, ver=True)

    else:
        print("\nNo se hallaron registros que coincidieran con la búsqueda.")
        print("\n")

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
            codigo = input("Ingrese el código de la aerolínea buscada: ")
            rango = input("Ingrese el rango de minutos de retraso en salida a filtrar (formato [inicio, final]): ")
            print_req_1(control, codigo, rango)

        elif int(inputs) == 3:
            cod_al = input("Ingrese el códig de la aerolínea buscada: ")
            cod_ap = input("Ingrese el código de aeropuerto buscado: ")
            rango_d = input("Ingrese el rango de distancia a filtrar (formato [inicio, final]): ")
            print_req_3(control, cod_al, cod_ap, rango_d)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            rango = input("Ingrese el rango de fechas a filtrar (formato [inicio, final]): ")
            codigo = input("Ingrese el código del aeropuerto destino buscado: ")
            n = input("Ingrese la cantidad N de aerolíneas a considerar: ")
            print_req_5(control, rango, codigo, n)

        elif int(inputs) == 6:
            rf = input("Ingrese el rango de fechas a filtrar (formato [inicio, final]): ")
            rd = input("Ingrese el rango de distancias a filtrar (formato [inicio, final]): ")
            n = input("Ingrese la cantidad N de aerolíneas a considerar: ")
            print_req_6(control, rf, rd,n)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
