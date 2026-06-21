from Engine.Updates.history_update import *
from Engine.Updates.season_reset import *
from Engine.Updates.rivalry_update import rivalry_reset
from Engine.Processes.headline_processor import update_headlines

def initialize_new_season(league, season):
    league_history_update(league)
    season_history_update(season)
    for team in league.all_teams:
        team_history_update(team)

    rivalry_reset(league)
    reset_league(league)
    reset_season(league, season)
    for team in league.all_teams:
        reset_team(team)

    update_headlines(season)

    return "main"
