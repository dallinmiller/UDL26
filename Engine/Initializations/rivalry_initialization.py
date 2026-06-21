from itertools import combinations

def init_rivalries(league):
    rivalries = {}

    for team_1, team_2 in combinations(league.all_teams, 2):

        key = tuple(sorted((team_1.league_index, team_2.league_index)))

        # base score
        if team_1.division == team_2.division:
            score = 65
            if team_1.conference == team_2.conference:
                score += 55
        else:
            score = 40

        rivalries[key] = score

    league.rivalries = rivalries
