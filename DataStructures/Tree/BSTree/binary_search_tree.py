from DataStructures.Tree.BSTree import bst_node as n
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as al

def new_map():
    bst = {"root": None}
    return bst 

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def insert_node(node, key, value):
    
    if node is None:
        return n.new_node(key, value)

    if key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = insert_node(node["right"], key, value)
    else:
        node["value"] = value  # actualiza si ya existe la key

    return node

def get(bst, key):
    return get_node(bst["root"], key)

def get_node(node, key):
    if node is None:
        return None

    if key == node["key"]:
        return node["value"]
    elif key < node["key"]:
        return get_node(node["left"], key)
    else:
        return get_node(node["right"], key)
    
def remove(bst, key):
    bst["root"] = remove_node(bst["root"], key)
    return bst

def remove_node(node, key):
    if node is None:
        return None

    # Buscar
    if key < node["key"]:
        node["left"] = remove_node(node["left"], key)
    elif key > node["key"]:
        node["right"] = remove_node(node["right"], key)
    else: #key = node["key"]
        #sin hijos
        if node["left"] is None and node["right"] is None:
            return None
        #un hijo
        elif node["left"] is None:
            return node["right"]
        elif node["right"] is None:
            return node["left"]
        # Caso 3: dos hijos
        else:
            min_node = get_min_node(node["right"])
            node["key"] = min_node["key"]
            node["value"] = min_node["value"]
            node["right"] = remove_node(node["right"], min_node["key"])

    return node


def size(bst):
    return size_tree(bst["root"])

def size_tree(node):
    if node is None:
        return 0
    return 1 + size_tree(node["left"]) + size_tree(node["right"])

def is_empty(bst):
    return size(bst) == 0

def contains(bst, key):
    return get(bst, key) is not None

def key_set(bst):
    return key_set_tree(bst["root"], sll.new_list())

def key_set_tree(node, result):
    if node is not None:
        _inorder(node["left"], result)
        sll.add_last(result, node["key"])
        _inorder(node["right"], result)
    return result

def value_set(bst):
    return value_set_tree(bst["root"], al.new_list())

def value_set_tree(node, result):
    if node is not None:
        value_set_tree(node["left"], result)
        al.add_last(result, node["value"])
        value_set_tree(node["right"], result)
    return result

def get_min(bst):
    return get_min_node(bst["root"])

def get_min_node(node):
    if node:
        if node["left"]:
            return get_min_node(node["left"])
        return node["key"]
    return None

def get_max(bst):
    return get_max_node(bst["root"])

def get_max_node(node):
    if node:
        if node["right"]:
            return get_max_node(node["right"])
        return node["key"]
    return None

def delete_min(bst):
    bst["root"] = delete_min_tree(bst)
    return bst

def delete_min_tree(bst):
    kmin = get_min(bst)
    bst = remove(bst, kmin)
    return bst

def delete_max(bst):
    bst["root"] = delete_max_tree(bst)
    return bst

def delete_max_tree(bst):
    kmax = get_max(bst)
    bst = remove(bst, kmax)
    return bst

def floor(bst, key):
    return floor_key(bst["root"], key)

def floor_key(node, key):
    if node is None:
        return None
    
    if node["key"] == key:
        return node["key"]

    if key < node["key"]:
        return floor_key(node["left"], key)

    temp = floor_key(node["right"], key)
    if temp is not None:
        return temp
    else:
        return node["key"]
    
def ceiling(bst, key):
    return ceiling_key(bst["root"], key)

def ceiling_key(node, key):
    if node is None:
        return None

    if node["key"] == key:
        return node["key"]

    if key > node["key"]:
        return ceiling_key(node["right"], key)

    temp = ceiling_key(node["left"], key)
    if temp is not None:
        return temp
    else:
        return node["key"]

def select(bst, pos):
    return select_key(bst["root"], pos)

def select_key(node, pos):
    keys = key_set_tree(node, sll.new_list())
    if pos < 0 or pos >= sll.size(keys):
        return None
    return sll.get_element(keys, pos)

def rank(bst, key):
    return rank_keys(bst["root"], key)

def rank_keys(node, key):

    keys = key_set_tree(node, sll.new_list())
    count = 0

    for i in range(sll.size(keys)):
        current_key = sll.get_element(keys, i)
        if current_key < key:
            count += 1
        else:
            break

    return count

def height(bst):
    return height_node(bst["root"])

def height_node(node):
    if node is None:
        return 0  

    left_al = height_node(node["left"])
    right_al = height_node(node["right"])

    if left_al > right_al:
        altura = left_al
    else:
        altura  = right_al

    return 1 + altura

def keys(bst, ki, kf):
    return keys_range(bst["root"], ki, kf)

def keys_range(node, ki, kf):
    keys = key_set_tree(node, sll.new_list())
    keys_r = sll.new_list()

    for i in range(sll.size(keys)):
        k = sll.get_element(keys, i)
        if ki <= k <= kf:
            sll.add_last(keys_r, k)

    return keys_r

def values(bst, ki, kf):
    return values_range(bst["root"], ki, kf, sll.new_list())


def values_range(node, ki, kf, lst):
    if node is None:
        return lst

    if ki < node["key"]:
        values_range(node["left"], ki, kf, lst)

    if ki <= node["key"] <= kf:
        sll.add_last(lst, node["value"])

    if kf > node["key"]:
        values_range(node["right"], ki, kf, lst)

    return lst

#Recorridos
def inorder(bst):
    return _inorder(bst["root"], al.new_list())

def _inorder(node, result):
    if node is not None:
        _inorder(node["left"], result)
        al.add_last(result, node["key"])
        _inorder(node["right"], result)
    return result

def preorder(bst):
    return _preorder(bst["root"], al.new_list())

def _preorder(node, result):
    if node is not None:
        al.add_last(result, node["key"])
        _preorder(node["left"], result)
        _preorder(node["right"], result)
    return result