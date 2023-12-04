with open('input.txt', 'r') as file:

    total_points = 0

    for line in file:
        line = line.split(':')[1]
        winning_numbers = line.strip().split('|')[0].split()
        game_numbers = line.strip().split('|')[1].split()


        power = -1
        for number in game_numbers:
            if number in winning_numbers:
                power += 1

        if power != -1:
            total_points += 2**power
    
    print(total_points)