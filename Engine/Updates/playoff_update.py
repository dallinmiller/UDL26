from Engine.Simulations.simulate_week import simulate_week_playoff
from Engine.Updates.time_update import *
from Engine.Processes.schedule_creator import *
from Engine.Processes.headline_processor import update_headlines

def team_updates_playoff(game):
    if game.winner == "home":
        game.home_team.playoff_wins += 1
        game.away_team.playoff_losses += 1
    else:
        game.home_team.playoff_losses += 1
        game.away_team.playoff_wins += 1

    game.home_team.playoff_total_points += game.score_home
    game.home_team.playoff_scores += game.score_home
    game.home_team.playoff_opponent_points += game.score_away
    game.away_team.playoff_total_points += game.score_away
    game.away_team.playoff_scores += game.score_away
    game.away_team.playoff_opponent_points += game.score_home

def season_update_playoff(season):
    if season.playoff_week < 4:
        season.playoff_results.append(season.playoff_schedule[season.playoff_week - 1])
        season.playoff_week += 1
    else:
        season.playoff_results.append(season.playoff_schedule[season.playoff_week - 1])
        season.playoff_week += 1
        season.complete = True

def weekly_update_playoff(league, season):
    simulate_week_playoff(season)
    for game in season.playoff_schedule[season.playoff_week - 1]:
        team_updates_playoff(game)
    season_update_playoff(season)
    if not season.complete:
        if season.playoff_week == 2:
            create_conference_finals_schedule(league, season)
            create_times_conference_playoffs(season, 1)
        elif season.playoff_week == 3:
            create_semifinals_schedule(league, season)
            create_times_semifinals_playoffs(season)
        elif season.playoff_week == 4:
            create_finals_schedule(league, season)
        else:
            raise IndexError("Season Week out of range, did not complete season.")
        update_headlines(season)
        return "playoff_results_new"
    else:
        crown_champion(league, season)
        return "playoff_results_final"
