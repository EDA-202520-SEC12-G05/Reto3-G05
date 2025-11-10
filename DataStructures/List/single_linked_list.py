#Función New list
def new_list():
    newlist = {
        "first": None, 
        "last": None,
        "size": 0,
        "type": "SINGLE_LINKED"
    }
    return newlist

#Función get_element
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

#Función is_present
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

#Función add_first
def add_first(my_list, element):

    node = {"info": element}

    if my_list["size"] > 0:
        node["next"] = my_list["first"]
        my_list["first"] = node
    else:
        node["next"] = None
        my_list["first"] = node
        my_list["last"] = node

    my_list["size"] += 1
    
    return my_list

#Función add_last
def add_last(my_list, element):
    
    node = {"info": element, "next": None}

    if my_list["size"] > 0:
        my_list["last"]["next"] = node
        my_list["last"] = node
    else:
        my_list["first"] = node
        my_list["last"] = node
    
    my_list["size"] += 1

    return my_list

#Función Size
def size(my_list):
    return my_list["size"]

#Función First Element
def first_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    else: 
        return my_list["first"]
    
#Función is_empty
def is_empty(my_list):
    return my_list["size"] == 0

#Función last element
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]
    
#Función delete element
def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    else:
        i = 0
        node_actual = my_list["first"]
        node_previo = None

        while node_actual is not None:
            if i == pos:
                if node_previo == None:
                    #Si el nodo anterior al actual está vacío, significa que se está borrando el primer nodo
                    #El nuevo primer nodo se vuelve el next del primer nodo
                    my_list["first"] = node_actual["next"]
                    if my_list["first"] is None:  # si quedó vacía
                        my_list["last"] = None
                
                else:
                    #Borrar al medio 
                    node_previo["next"] = node_actual["next"]
                    #Si el nodo no tiene un next, es el último
                    if node_actual["next"] == None:
                        my_list["last"] = node_previo
            
                my_list["size"] -= 1
                break
            
            #Si no se ha llegado a la posición, se avanza al siguiente todo y se aumenta el contador
            else:
                node_previo = node_actual
                node_actual = node_actual["next"]
                i += 1
    
    return my_list

#Función remove first
def remove_first(my_list):

    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    
    first_node = my_list["first"]
    my_list["first"] = my_list["first"]["next"]
    if my_list["first"] is None: 
        my_list["last"] = None

        my_list["size"] -= 1

    return first_node["info"]

#Función remove last
def remove_last(my_list):

    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')

    #Iniciar con el primer nodo de la lista
    node_actual = my_list["first"]
    node_previo = None

    #Si el primer nodo es también el último
    if node_actual["next"] == None:
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        
        return node_actual["info"]
    
    else:
        #Iniciar el recorrido hasta llegar al último nodo
        while node_actual["next"] is not None:
            node_previo = node_actual
            node_actual = node_actual["next"]

        node_previo["next"] = None
        my_list["last"] = node_previo
    
        my_list["size"] -= 1
    
    return node_actual["info"]

#Función insert_element
def insert_element(my_list, element, pos):

    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    #Crear nuevo nodo con el elemento
    nuevo_nodo = {"info": element, "next": None}
    #Insertar al principio
    if pos == 0:
        nuevo_nodo["next"] = my_list["first"]
        my_list["first"] = nuevo_nodo
        #Si la lista estaba vacía, se actualiza last tbm
        if my_list["size"] == 0:
            my_list["last"] = nuevo_nodo
        
        my_list["size"] += 1
        return my_list
    
    node_actual = my_list["first"]
    node_previo = None
    i = 0

    #El while recorre todo hasta que node_actual = last node
    while node_actual["next"] is not None:
            if i == pos:
                nuevo_nodo["next"] = node_previo["next"]
                node_previo["next"] = nuevo_nodo
                my_list["size"] += 1
                return my_list
            else:
                node_previo = node_actual
                node_actual = node_actual["next"]
                i += 1
    
    #Si se sale del while, significa que estamos en el último nodo y se hace la insersión al final
    node_actual["next"] = nuevo_nodo
    my_list["last"] = nuevo_nodo
    my_list["size"] += 1
    return my_list

#Función change_info
def change_info(my_list, pos, new_info):

    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    #Caso 1. Primera posición
    if pos == 0:
        my_list["first"]["info"] = new_info
        return my_list
    
    nodo = my_list["first"]
    i = 0

    #Recorrido completo
    while nodo is not None:
        if pos == i:
            nodo["info"] = new_info
            return my_list
        else:
            nodo = nodo["next"]
            i += 1

#Función exchange
def exchange(my_list, pos_1, pos_2):
    size = my_list["size"]

    # Caso de posición no válida
    if pos_1 < 0 or pos_2 < 0 or pos_1 >= size or pos_2 >= size:
        raise Exception("IndexError: list index out of range")
    
    # Caso nodo1 = nodo2 
    if pos_1 == pos_2:
        return my_list
    
    node_actual = my_list["first"]
    i = 0

    nodo1 = None   
    nodo2 = None   

    # Recorrido completo
    while node_actual is not None:
        if i == pos_1:
            nodo1 = node_actual
        if i == pos_2:
            nodo2 = node_actual
        if nodo1 is not None and nodo2 is not None:   
            break
        
        node_actual = node_actual["next"]
        i += 1
    
    # Intercambiar info
    nodo1["info"], nodo2["info"] = nodo2["info"], nodo1["info"]

    return my_list

#Función sub list
def sub_list(my_list, pos, num_elements):

    if pos < 0 or pos > size(my_list):
        return new_list()
    
    #Si la sublista está vacía
    if num_elements <= 0:
        return new_list()
    
    #Sino, recorrido hasta llegar a la posición indicada
    nodo_actual = my_list["first"]
    posicion = 0

    while posicion < pos:
        nodo_actual = nodo_actual["next"]
        posicion += 1
    
    sub_lista = new_list()
    agregados = 0
    while nodo_actual is not None and agregados < num_elements:
        #Crear un nuevo nodo con la información del actual
        nuevo_nodo = {"info": nodo_actual["info"], "next": None}

        #Si la sublista está pasando por el ciclo por primera vez, o solo hay que añadir un nodo
        if sub_lista["first"] == None:
            sub_lista["first"] = nuevo_nodo
            sub_lista["last"] = nuevo_nodo
        #Si ya se añadió algo a la sublista
        else:
            sub_lista["last"]["next"] = nuevo_nodo
            sub_lista["last"] = nuevo_nodo
        
        sub_lista["size"] += 1
        nodo_actual = nodo_actual["next"]
        agregados += 1

    return sub_lista
#SORT

#Comparación de números
def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

#SELECTION SORT
def selection_sort(lst, sort_crit):

    if lst["size"] == 0 or lst["size"] == 1:
        return lst
    else:
        for i in range(0, lst["size"]-1):
            p_ch = i
            min_ = get_element(lst,  i)
            for ch in range(i+1, lst["size"]):
                if sort_crit(get_element(lst, ch), min_):
                    p_ch = ch 
                    min_ = get_element(lst, ch)

            exchange(lst, i, p_ch)
        
        return lst

def insertion_sort(lst, sort_crit):
    
    if lst["size"] == 0 or lst["size"] == 1:
        return lst
    else:
        for i in range(1, lst["size"]):
            ch = i 
            while ch > 0 and sort_crit(get_element(lst, ch), get_element(lst, ch-1)):
                exchange(lst, ch, ch-1)
                ch -= 1

        return lst

def shell_sort(lst, sort_crit):
    size = lst["size"]

    if size == 0 or size == 1:
        return lst
    else:
        # Generar h Knuth
        h = 1
        while h < size // 3:
            h = 3 * h + 1

        # Recorrido por gaps
        while h >= 1:
            # Recorrido total izq a der
            for i in range(h, size):  
                current = i
                # comparación hacia atrás con gap h
                while current >= h and sort_crit(get_element(lst, current), get_element(lst, current-1)):
                    exchange(lst, current, current - h)
                    current -= h
            
            #Reducción de h
            h = h // 3

    return lst

#Ordenamientos recursivos
def merge_sort(L, sort_crit):

    if L["size"] <= 1:   
        return L
    
    im = L["size"] // 2

    izq = sub_list(L, 0, im)
    der = sub_list(L, im, L["size"] - im)

    izord = merge_sort(izq, sort_crit)
    derord = merge_sort(der, sort_crit)

    return merge(izord, derord, sort_crit)

def merge(L1, L2, sort_crit):
    n1 = L1["first"]
    n2 = L2["first"]
    NL = new_list()

    while n1 is not None and n2 is not None:
        if sort_crit(n1["info"], n2["info"]) <= 0:
            add_last(NL, n1["info"])
            n1 = n1["next"]
        else:
            add_last(NL, n2["info"])
            n2 = n2["next"]

    while n1 is not None:
        add_last(NL, n1["info"])
        n1 = n1["next"]

    while n2 is not None:
        add_last(NL, n2["info"])
        n2 = n2["next"]

    return NL


def qsort(lst, i, f, sort_crit):
    if i >= f:
        return lst

    prev = i - 1
    ppivot = f
    pivot = get_element(lst, ppivot)

    for recorr in range(i, f):
        if sort_crit(get_element(lst, recorr), pivot):
            prev += 1
            exchange(lst, prev, recorr)

    exchange(lst, prev + 1, ppivot)
    ppivot = prev + 1

    qsort(lst, i, ppivot - 1, sort_crit)
    qsort(lst, ppivot + 1, f, sort_crit)

    return lst


def quick_sort(lst, sort_crit):
    if lst["size"] <= 1:   
        return lst
    
    qsort(lst, 0, lst["size"] - 1, sort_crit)
    return lst