import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as lt
from DataStructures.List import array_list as lt


#Funciones de comparación
def default_compare_higher_value(father_node, child_node):
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

def default_compare_lower_value(father_node, child_node):
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)

#Funciones de implementación
def new_heap(is_min_pq=True):

    heap = {"elements": lt.new_list(),
            "size": 0}
    
    lt.add_last(heap["elements"], None)
    
    if is_min_pq:
        heap["cmp_function"] = default_compare_lower_value
    else:
        heap["cmp_function"] = default_compare_higher_value
    
    return heap

def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

def exchange(heap, n1, n2):
    arr = heap["elements"]
    heap["elements"] = lt.exchange(arr, n1, n2)
    return heap

def size(heap):
    return heap["size"]

def is_empty(heap):
    return heap["size"] == 0

def swim(heap, pos):
    array_l = heap["elements"]

    while pos > 1:
        parent = pos // 2

        if priority(heap, lt.get_element(array_l, parent), lt.get_element(array_l, pos)):
            break
        else:
            exchange(heap, parent, pos)
            pos = parent
    return heap

def insert(heap, prio, value):
    nodo = pqe.new_pq_entry(prio, value)
    array_l = heap["elements"]
    
    lt.add_last(array_l, nodo)
    heap["size"] += 1
    
    swim(heap, heap["size"])
    
    return heap

def get_first_priority(heap):
    if is_empty(heap):
        return None
    return heap["elements"]["elements"][1]["value"]

def is_present_value(heap, value):

    def cmp(na, nb):
        if na == nb["value"]:
            return 0
        else:
            return -1

    array_l = heap["elements"]
    size = array_l["size"]
    if size > 0:
        keyexist = False
        for keypos in range(1, size):
            info = array_l["elements"][keypos]
            if cmp(value, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def contains(heap, value):
    return is_present_value(heap, value) != -1

def improve_priority(heap, priority, value):
    if heap["size"] != 0:
        pos = is_present_value(heap, value)

        #Si no existe un elemento con ese value
        if pos == -1:
            return None
        heap["elements"]["elements"][pos]["priority"] = priority

        swim(heap, pos)

    return heap

def sink(heap, pos):
    array_l = heap["elements"]
    n = heap["size"]

    while 2 * pos <= n:
        h_iz = 2 * pos
        h_der = 2 * pos + 1
        hijo_p = h_iz

        if h_der <= n and priority(heap, lt.get_element(array_l, h_der), lt.get_element(array_l, h_iz)):
            hijo_p = h_der

        if not priority(heap, lt.get_element(array_l, pos), lt.get_element(array_l, hijo_p)):
            exchange(heap, pos, hijo_p)
            pos = hijo_p
        else:
            break

def remove(heap):
    if heap["size"] > 0:
        array_l = heap["elements"]

        min_elem = lt.get_element(array_l, 1)

        exchange(heap, 1, heap["size"])

        lt.delete_element(array_l, heap["size"])
        heap["size"] -= 1

        # Restaura el heap solo si quedan elementos
        if heap["size"] > 0:
            sink(heap, 1)

        return min_elem["value"]
    return None