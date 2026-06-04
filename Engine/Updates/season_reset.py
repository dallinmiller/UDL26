from Engine.Processes.schedule_creator import create_schedule
from Engine.Updates.time_update import create_times

def reset_league(league):
    for var_name, default_value in league.reset_values.items():
        setattr(league, var_name, default_value)
    
def reset_season(league, season):
    season.season_number += 1
    season.week = 1
    season.season_schedule = create_schedule(league, season)
    create_times(season)

    season.season_results = []
    season.playoff_schedule = []
    season.playoff_results = []
    season.playoff = False
    season.complete = False
    season.playoff_week = 0
    
def reset_team(team):
    for var_name, default_value in team.reset_values.items():
        setattr(team, var_name, default_value)
    