# Create a function that returns Georgia Tech's football record against the desired team.
def all_time_record(team):
    # Open text file
    input_file = open("season2016.txt", "r")
    # Get a list of the games
    list_of_games = []
    for line in input_file:
        list_of_games.append(line.strip())
    list_of_games = list_of_games[1:]

    # Make a dictionary of lists for teams and game scores
    team_dict = {}
    for i in range(0, len(list_of_games)):
        current_list = list_of_games[i].split(",")
        del current_list[0]
        del current_list[1]
        current_team = current_list[0]
        current_score = [int(current_list[1]), int(current_list[2])]
        if current_team not in team_dict:
            team_dict[current_team] = [current_score]
        else:
            team_dict[current_team].append(current_score)
    team_to_check = team_dict[team]

    # Return the record against the team
    gt_wins = 0
    gt_losses = 0
    ties = 0
    for game in team_to_check:
        if game[0] > game[1]:
            gt_wins += 1
        elif game[0] < game[1]:
            gt_losses += 1
        else:
            ties += 1
    return str(gt_wins) + "-" + str(gt_losses) + "-" +str(ties)
