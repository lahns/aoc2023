with open("input.txt", 'r') as file:

    sum_id = 0

    for line in file:
        info = line.split(':')
        id = info[0].split(' ')[1]
        games = info[1].split(';')

        is_game_ok = True

        for game in games:
            round = game.split(',')
            colors = {'red' : 0, 'blue': 0, 'green': 0}
            for roll in round:
                roll = roll.strip().split(' ')
                colors[roll[1]] = int(roll[0])
            
            if colors["red"] > 12 or colors["blue"] > 14 or colors["green"] > 13:
                is_game_ok = False

        
        if is_game_ok:
            sum_id += int(id)

    print(sum_id)