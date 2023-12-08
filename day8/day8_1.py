bindings = {"L" : 0, "R" : 1}

with open('input.txt', 'r') as file:
    instructions = file.readline().strip()

    instructions_copy = instructions[:]

    nodes = {}

    for line in file:
        single_node = line.split('=')[0].strip()
        node_splits = line.split('=')[1].strip().strip('()').split(',')
        nodes[single_node] = list(map(str.strip, node_splits))

    
    curr_element = 'AAA'
    i = 0

    total_moves = 0

    print(curr_element)
    while curr_element != 'ZZZ':
        curr_element = nodes[curr_element][bindings[instructions[i]]] 
        if i == len(instructions)-1:
            instructions = instructions + instructions_copy
        i = i + 1
    else:
        print(i)      
        
