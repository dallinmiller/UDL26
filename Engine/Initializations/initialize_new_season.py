from Engine.Updates.history_update import *
from Engine.Updates.season_reset import *

def initialize_new_season(league, season):
    league_history_update(league)
    season_history_update(season)
    for team in league.all_teams:
        team_history_update(team)

    reset_league(league)
    reset_season(league, season)
    for team in league.all_teams:
        reset_team(team)

    return "main"
