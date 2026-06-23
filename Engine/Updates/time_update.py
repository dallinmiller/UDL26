import random

def create_times(league, season):
    for match in season.season_schedule[season.week - 1]:
        match_prestige = match.home_team.prestige + match.away_team.prestige
        if match.rivalry:
            match_prestige += league.match_time_settings.rivalry_bonus
        if match.tight_race:
            match_prestige += league.match_time_settings.tight_race_bonus
        if match.playoff_implication:
            match_prestige += league.match_time_settings.playoff_implication_bonus
        match_prestige *= random.normalvariate(1, league.match_time_settings.prestige_rand)
        match.prestige = match_prestige

    season.season_schedule[season.week - 1].sort(key=lambda game: game.prestige, reverse=True)

    for i, game in enumerate(season.season_schedule[season.week - 1]):
        game.match_time = league.match_time_settings.match_times[i]

def create_times_conference_playoffs(league, season, week_index=0):
    for match in season.playoff_schedule[week_index]:
        match_prestige = match.home_team.prestige + match.away_team.prestige
        if match.rivalry:
            match_prestige += league.match_time_settings.rivalry_bonus
        match_prestige *= random.normalvariate(1, league.match_time_settings.prestige_rand)
        match.prestige = match_prestige

    season.playoff_schedule[week_index].sort(key=lambda game: game.prestige, reverse=True)

    season.playoff_schedule[week_index][0].match_time = "6:00"
    season.playoff_schedule[week_index][1].match_time = "12:00"
    season.playoff_schedule[week_index][2].match_time = "4:00"
    season.playoff_schedule[week_index][3].match_time = "1:00"

def create_times_semifinals_playoffs(league, season):
    for match in season.playoff_schedule[2]:
        match_prestige = match.home_team.prestige + match.away_team.prestige
        if match.rivalry:
            match_prestige += league.match_time_settings.rivalry_bonus
        match_prestige *= random.normalvariate(1, league.match_time_settings.prestige_rand)
        match.prestige = match_prestige

    season.playoff_schedule[2].sort(key=lambda game: game.prestige, reverse=True)

    season.playoff_schedule[2][0].match_time = "6:00"
    season.playoff_schedule[2][1].match_time = "3:00"
