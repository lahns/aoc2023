from functools import reduce

with open('input.txt', 'r') as file:
    races = {}
    time =  int(reduce((lambda x, y : x + y),file.readline().split(":")[1].strip().split()))
    distance =  int(reduce((lambda x, y : x + y),file.readline().split(":")[1].strip().split()))
       

    i = 0
    won_runs = []
    while i <= time:
        time_left = time - i
        reach = time_left * i
        if reach > distance:
            won_runs.append(reach)
        i = i + 1

    print(len(won_runs))
