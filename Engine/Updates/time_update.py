import random

def create_times(season):
    for match in season.season_schedule[season.week - 1]:
        match_prestige = match.home_team.prestige + match.away_team.prestige
        match_prestige *= random.normalvariate(1, 0.08)
        match.prestige = match_prestige

    season.season_schedule[season.week - 1].sort(key=lambda game: game.prestige, reverse=True)

    season.season_schedule[season.week - 1][0].match_time = "6:00"
    season.season_schedule[season.week - 1][1].match_time = "12:00"
    season.season_schedule[season.week - 1][2].match_time = "2:30"
    season.season_schedule[season.week - 1][3].match_time = "1:00"
    season.season_schedule[season.week - 1][4].match_time = "4:00"
    season.season_schedule[season.week - 1][5].match_time = "1:00"
    season.season_schedule[season.week - 1][6].match_time = "4:00"
    season.season_schedule[season.week - 1][7].match_time = "2:30"
