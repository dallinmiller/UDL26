from Engine.Processes.schedule_creator import create_schedule
from Engine.Updates.time_update import create_times

def reset_league(league):
    league.playoff_teams = {}
    league.conference_final_teams = {}
    league.semifinal_teams = {}
    league.final_teams = []
    league.champion = None
    
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
    team.prestige = 1
    team.season_status = "calm"
    team.game_status = "calm"
    team.wins = 0
    team.losses = 0
    team.win_loss = 0
    team.total_points = 0
    team.scores = 0
    team.callahan = 0
    team.total_yards = 0
    team.turnovers = 0
    team.opponent_points = 0
    team.opponent_yards = 0

    team.playoff_semis = False
    team.playoff_wins = 0
    team.playoff_losses = 0
    team.playoff_total_points = 0
    team.playoff_scores = 0
    team.playoff_callahan = 0
    team.playoff_total_yards = 0
    team.playoff_turnovers = 0
    team.playoff_opponent_points = 0
    team.playoff_opponent_yards = 0
    
    
    