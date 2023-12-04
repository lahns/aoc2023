with open('input.txt', 'r') as file:

    total_scratchcards = 0
    lines = file.readlines()
    lines = list(map(str.strip, lines))

    scratches = {}

    for index, line in enumerate(lines):
        if index not in scratches:
            scratches[index] = 1
        line = line.split(':')[1]
        winning_numbers = line.strip().split('|')[0].split()
        game_numbers = line.strip().split('|')[1].split()
        
        matching_numbers = sum(q in winning_numbers for q in game_numbers)

        for next in range(index + 1, index + matching_numbers + 1):
            scratches[next] = scratches.get(next, 1) + scratches[index]
        


    print(sum(scratches.values()))
