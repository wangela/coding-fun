def convert(A):
    a = A.splitlines()
    result = []
    for each in a:
        b = each.split()
        c = []
        c.append(b[0])
        weight = int(str.strip(b[1], '()'))
        c.append(weight)
        d = []
        if len(b) > 2:
            for item in b[3:]:
                program = re.sub(',', '', item)
                d.append(program)
            c.append(d)
        result.append(c)

    return result

def get_parent(A, nodes_dict):
    parent = nodes_dict[A]['parent']
    if parent != None:
        parent = get_parent(parent, nodes_dict)
    else:
        return A
    return parent

def find_bottom(A):
    # Input: An array, where each element has the structure:
    #   [name, weight, [programs]]
    # Output: The name of the bottom program
    # Example:
    #   [[tknk, 41, [ugml, padx, fwft]], [fwft, 72, [ktlj, cntj, xhth]]] --> tknk
    # Approach:
    #   Every node has a parent except for the bottom node.
    #   Nested Dictionary: {name: {weight: x, parent: y}}
    #   nodes = {fwft: {weight: 72, parent: tknk}}
    #   nodes[fwft][weight] = 72
    nodes = {}
    try_node = []

    for node in A:
        name = node[0]
        try_node.append(name)
        if name in nodes:
            nodes[name]['weight'] = node[1]
        else:
            nodes[name] = {'weight': node[1], 'parent': None}
        if len(node) > 2:
            for child in node[2]:
                if child in nodes:
                    nodes[child]['parent'] = name
                else:
                    nodes[child] = {'weight': 0, 'parent': name}

    if nodes[try_node[0]]['parent'] == None:
        ancestor = get_parent(try_node[1], nodes)
    else:
        ancestor = get_parent(try_node[0], nodes)

    return ancestor

def weigh_children(A, parents_dict):
    kids = parents_dict[A]['children']
    family_weights = {}

    for kid in kids:
        kid_weight = parents_dict[kid]['weight']
        if parents_dict[kid]['children'] != None:
            kids_weight = weigh_children(kid, parents_dict)
            for baby_weight in kids_weight:
                kid_weight += baby_weight
        if kid_weight in family_weights:
            family_weights[kid_weight].append(kid)
        else:
            family_weights[kid_weight] = [kid]

    return family_weights

def find_imbalance(family_weights, parents_dict):
    off_child = None
    if len(family_weights) == 1:
        return None
    elif len(family_weights) > 1:
        for weight in family_weights.keys():
            if len(family_weights[weight]) == 1:
                child = family_weights[weight]
                off_child = find_imbalance(weigh_children(child, parents_dict))

    return off_child

def find_imbalance(A):
    # Input: An array, where each element has the structure:
    #   [name, weight, [programs]]
    # Output: The revised weight of the imbalanced node
    # Example:
    #   [[tknk, 41, [ugml, padx, fwft]], [fwft, 72, [ktlj, cntj, xhth]]] --> 60
    # Approach:
    #   Get the weights of children including the weights of their children
    #   Return a list of children's weights
    #   Compare the children's weights and look for odd one out
    #   Return list of odd one, common one (if only one weight, just return that)
    #   
    nodes = {}

    for node in A:
        name = node[0]
        if name in nodes:
            nodes[name]['weight'] = node[1]
        else:
            nodes[name] = {'weight': node[1], 'children' = None}
        if len(node) > 2:
            nodes[name]['children'] = node[2]

    total_weights = compare_children(nodes['svugo'])

    return
