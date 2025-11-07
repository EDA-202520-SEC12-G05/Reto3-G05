from DataStructures.Tree.RBTree import rbt_node as rn
from DataStructures.Tree.BSTree import binary_search_tree as bs

def default_compare(key, element):
    
    element_key = rn.get_key(element)
    
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    else:
        return -1
    
def rotate_left(node_rbt):

    x = node_rbt['right']

    node_rbt['right'] = x['left']

    x['left'] = node_rbt

    x['color'] = node_rbt['color']

    node_rbt['color'] = 0  
   
    x['size'] = node_rbt['size']
    node_rbt['size'] = 1 + bs.size_tree(node_rbt['left']) + bs.size_tree(node_rbt['right'])
    
    return x


def rotate_right(node_rbt):

    x = node_rbt['left']

    node_rbt['left'] = x['right']

    x['right'] = node_rbt

    x['color'] = node_rbt['color']
    
    node_rbt['color'] = 0  

    x['size'] = node_rbt['size']
    node_rbt['size'] = 1 + bs.size_tree(node_rbt['left']) + bs.size_tree(node_rbt['right'])
    
    return x

#Para dos negros seguidos en la izquierda
def move_red_left(h):
    rn.flip_colors(h)
    if rn.is_red(h["right"]["left"]):
        h["right"] = rotate_right(h["right"])
        h = rotate_left(h)
        rn.flip_colors(h)
    return h

#Para dos negros seguidos en la derecha
def move_red_right(h):
    rn.flip_colors(h)
    if rn.is_red(h["left"]["left"]):
        h = rotate_right(h)
        rn.flip_colors(h)
    return h

#Función de balanceo general
def balance(h):
    if rn.is_red(h["right"]):
        h = rotate_left(h)
    if rn.is_red(h["left"]) and rn.is_red(h["left"]["left"]):
        h = rotate_right(h)
    if rn.is_red(h["left"]) and rn.is_red(h["right"]):
        rn.flip_colors(h)
    return h
