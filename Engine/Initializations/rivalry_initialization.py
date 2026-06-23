from itertools import combinations

def init_rivalries(league):
    rivalries = {}

    for team_1, team_2 in combinations(league.league, 2):

        key = tuple(sorted((team_1.league_index, team_2.league_index)))

        # base score
        if team_1.conference == team_2.conference:
            score = league.rivalry_settings.init_score_conf
        elif team_1.division == team_2.division:
            score = league.rivalry_settings.init_score_div
        else:
            score = league.rivalry_settings.init_score

        rivalries[key] = score

    league.rivalries = rivalries
