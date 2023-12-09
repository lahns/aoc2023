from functools import reduce

with open('input.txt', 'r') as file:
    races = {}
    times = list(map(int, file.readline().split(":")[1].strip().split()))
    distances = list(map(int, file.readline().split(":")[1].strip().split()))
    for i in range(0, len(times)):
        races[times[i]] = distances[i]
        
    total_ways = []

    for key in races:
        i = 0
        won_runs = []
        while i <= key:
            time_left = key - i
            reach = time_left * i 
            if reach > races[key]:
                won_runs.append(reach)
            i = i + 1

        total_ways.append(len(won_runs))

    print(reduce((lambda x,y : x*y), total_ways))
