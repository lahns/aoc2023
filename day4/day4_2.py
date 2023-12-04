with open('input.txt', 'r') as file:

    total_scratchcards = 0
    lines = file.readlines()
    lines = list(map(str.strip, lines))

    for line in lines:
        game_number = int(line.split(':')[0].split()[1])
        line = line.split(':')[1]
        winning_numbers = line.strip().split('|')[0].split()
        game_numbers = line.strip().split('|')[1].split()
        
        winngings = []
        i = int(game_number)+1
        for number in game_numbers:
            if number in winning_numbers:
                winngings.append(i)
                i += 1
        
        for win in winngings:
            lines.append(lines[int(win)-1])


    print(len(lines))