from DataStructures.Tree.RBTree import rbt_node as rn
from DataStructures.Tree.BSTree import binary_search_tree as bs
from DataStructures.Tree.RBTree import rbt_aux_functions as aux
from DataStructures.List import array_list as sll

def new_map():
    rbt = {"root": None,
           "type": "RBT"}
    return rbt

def put(my_rbt, key, value):

    my_rbt['root'] = insert_node(my_rbt['root'], key, value)
    my_rbt['root']['color'] = 1  
    return my_rbt


def insert_node(root, key, value):

    if root is None:
        return rn.new_node(key, value, color=0) 
    
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value  # actualiza si ya existe la key
    
    root = aux.balance(root)

    root['size'] = 1 + bs.size_tree(root['left']) + bs.size_tree(root['right'])
    
    return root

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

def remove_node(h, key):
    if key < h["key"]:
        if h["left"] is not None:
            # Asegurar no dos negros seguidos
            if not rn.is_red(h["left"]) and not rn.is_red(h["left"]["left"]):
                h = aux.move_red_left(h)
            h["left"] = remove_node(h["left"], key)
    else:
        # rotar si hay rojo a la izquierda, para mantener la inclinación izquierda
        if rn.is_red(h["left"]):
            h = aux.rotate_right(h)
        #Caso hoja
        if key == h["key"] and h["right"] is None:
            return None 
        
        if h["right"] is not None:
            # si el hijo derecho y su hijo izquierdo no son rojos, movemos rojo a la derecha
            if not rn.is_red(h["right"]) and not rn.is_red(h["right"]["left"]):
                h = aux.move_red_right(h)
            if key == h["key"]:
                min_node = get_min_node(h["right"])
                h["key"] = min_node["key"]
                h["value"] = min_node["value"]
                h["right"] = aux.remove_min(h["right"])
            else:
                h["right"] = remove_node(h["right"], key)

    return aux.balance(h)

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

def contains(bst, key):
    return get(bst, key) is not None

def size(bst):
    return size_tree(bst["root"])

def size_tree(node):
    if node is None:
        return 0
    return 1 + size_tree(node["left"]) + size_tree(node["right"])

def is_empty(bst):
    return size(bst) == 0

def key_set(bst):
    return key_set_tree(bst["root"], sll.new_list())

def key_set_tree(node, result):
    if node is not None:
        bs._inorder(node["left"], result)
        sll.add_last(result, node["key"])
        bs._inorder(node["right"], result)
    return result

def value_set(bst):
    return value_set_tree(bst["root"], sll.new_list())

def value_set_tree(node, result):
    if node is not None:
        bs._inorder(node["left"], result)
        sll.add_last(result, node["value"])
        bs._inorder(node["right"], result)
    return result

def delete_min(bst):
    delete_min_tree(bst)
    return bst

def delete_min_tree(bst):
    kmin = get_min(bst)
    bst = remove(bst, kmin)
    return bst

def delete_max(bst):
    delete_max_tree(bst)
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
        if  isinstance(k, int) and ki <= k <= kf:
            sll.add_last(keys_r, k)

    return keys_r

def values(bst, ki, kf):
    return values_range(bst["root"], ki, kf, sll.new_list())


def values_range(node, ki, kf, lst):
    if node is None:
        return lst

    if ki < node["key"]:
        lst = values_range(node["left"], ki, kf, lst)

    if ki <= node["key"] <= kf:
        sll.add_last(lst, node["value"])

    if kf > node["key"]:
        lst = values_range(node["right"], ki, kf, lst)

    return lst