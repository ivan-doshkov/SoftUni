cards = input().split()

players_list = []

team_a = 11
team_b = 11

for player in cards:
    if player not in players_list:
        players_list.append(player)
        if player[0] == "A":
            team_a -= 1
        elif player[0] == "B":
            team_b -= 1
    if team_a < 7 or team_b < 7:
        print(f"Team A - {team_a}; Team B - {team_b}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {team_a}; Team B - {team_b}")
