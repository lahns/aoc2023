import math
bindings = {"L" : 0, "R" : 1}

with open('input.txt', 'r') as file:
    instructions = file.readline().strip()

    instructions_copy = instructions[:]

    nodes = {}

    nodes_A = []

    for line in file:
        single_node = line.split('=')[0].strip()
        node_splits = line.split('=')[1].strip().strip('()').split(',')
        nodes[single_node] = list(map(str.strip, node_splits))

        if single_node[-1] == 'A':
            nodes_A.append(single_node)


    print(nodes_A)
    counts = []
    for node in nodes_A:
        curr_element = node
        i = 0
        while curr_element[-1] != 'Z':
            curr_element = nodes[curr_element][bindings[instructions[i]]] 
            if i == len(instructions)-1:
                instructions = instructions + instructions_copy
            i = i + 1
        else:
            counts.append(i)     

    print(math.lcm(*counts))
        
