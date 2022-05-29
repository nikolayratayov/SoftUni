players = {}
while True:
    a = input()
    if a == 'Season end':
        break
    b = a.split(' -> ')
    if len(b) == 1:
        c = a.split(' vs ')
        player1 = c[0]
        player2 = c[1]
        stop = False
        if player1 in players and player2 in players:
            for pos1 in players[player1]:
                if stop:
                    break
                for pos2 in players[player2]:
                    if stop:
                        break
                    if pos1 == pos2:
                        player1_points = 0
                        player2_points = 0
                        for k, v in players[player1].items():
                            player1_points += v
                        for k, v in players[player2].items():
                            player2_points += v
                        if player1_points > player2_points:
                            del players[player2]
                        elif player2_points > player1_points:
                            del players[player1]
                        stop = True
    else:
        player = b[0]
        position = b[1]
        skill = int(b[2])
        if player not in players:
            players[player] = {position: skill}
        elif player in players and position not in players[player]:
            players[player][position] = skill
        else:
            if skill > players[player][position]:
                players[player][position] = skill

players_total_points = {}
for i in players:
    points = 0
    for k, v in players[i].items():
        points += v
    players_total_points[i] = points
players_total_points_ordered_by_name = {k: v for k, v in sorted(players_total_points.items(), key=lambda item: item[0])}
players_total_points_sorted_by_points = {k: v for k, v in sorted(players_total_points_ordered_by_name.items(),
                                                                 key=lambda item: item[1], reverse=True)}

for k, v in players_total_points_sorted_by_points.items():
    print(f'{k}: {v} skill')
    pos_skill_ordered_by_name = {i: j for i, j in sorted(players[k].items(), key=lambda item: item[0])}
    pos_skill_ordered_by_points = {i: j for i, j in sorted(pos_skill_ordered_by_name.items(),
                                                           key=lambda item:item[1], reverse=True)}
    for key, value in pos_skill_ordered_by_points.items():
        print(f'- {key} <::> {value}')
