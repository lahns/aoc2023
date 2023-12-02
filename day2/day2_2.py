with open("input.txt", 'r') as file:

    sum_of_minimal_colors = 0

    for line in file:
        info = line.split(':')
        id = info[0].split(' ')[1]
        games = info[1].split(';')

        is_game_ok = True
        colors = {'red' : 0, 'blue': 0, 'green': 0}
        for game in games:
            round = game.split(',')
            for roll in round:
                roll = roll.strip().split(' ')
                if colors[roll[1]] < int(roll[0]):
                    colors[roll[1]] = int(roll[0])
            

        sum_of_minimal_colors += (colors['red']*colors['green']*colors['blue'])

    print(sum_of_minimal_colors)