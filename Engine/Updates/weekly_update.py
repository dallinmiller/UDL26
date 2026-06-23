from Engine.Simulations.simulate_week import simulate_week
from Engine.Updates.standing_update import update_standings
from Engine.Updates.time_update import create_times
from Engine.Updates.rivalry_update import update_rivalry, update_rivalry_week
from Engine.Processes.statistic_calculation import master_stats_return_team
from Engine.Processes.headline_processor import update_headlines
from Interface.utility_functions import *

def get_prestige_info(league, team):
    conference_leader = False

    for conference in league.conferences.values():
        if team in conference:
            if conference.index(team) == 0:
                conference_leader = True
            else:
                conference_leader = False

    ppg_leader = False
    oppg_leader = False
    stats_table = master_stats_return_team(league)
    sorting_index = 3

    for i in range(len(stats_table)):
        for j in range(len(stats_table) - 1):
            if stats_table[j][sorting_index] < stats_table[j + 1][sorting_index]:
                stats_table[j], stats_table[j + 1] = stats_table[j + 1], stats_table[j]

    if stats_table[0][0] == team:
        ppg_leader = True

    sorting_index = 5
    for i in range(len(stats_table)):
        for j in range(len(stats_table) - 1):
            if stats_table[j][sorting_index] < stats_table[j + 1][sorting_index]:
                stats_table[j], stats_table[j + 1] = stats_table[j + 1], stats_table[j]

    if stats_table[15][0] == team:
        oppg_leader = True

    return conference_leader, ppg_leader, oppg_leader

def prestige_update(league):
    for team in league.all_teams:
        conference_leader, ppg_leader, oppg_leader = get_prestige_info(league, team)
        if team.standing <= len(league.league) / 3:
            prestige = 4 - 3 * team.standing / len(league.league)
        else:
            pres_A = 27 / (2 * len(league.league) ** 3)
            pres_B = -99 / (4 * len(league.league) ** 2)
            pres_C = 9 / len(league.league)
            pres_D = 9 / 4

            prestige = pres_A * team.standing ** 3 + pres_B * team.standing ** 2 + pres_C * team.standing + pres_D

        if conference_leader:
            prestige += league.match_time_settings.conference_leader_bonus
        if ppg_leader:
            prestige += league.match_time_settings.ppg_leader_bonus
        if oppg_leader:
            prestige += league.match_time_settings.oppg_leader_bonus

        team.prestige = prestige

def playoff_implications_update(season):
    for game in season.season_schedule[season.week - 1]:
        if game.home_team.playoff_near_eliminated or game.away_team.playoff_near_eliminated:
            game.playoff_implication = True

        if season.week > 10 and abs(game.home_team.wins - game.away_team.wins) < 0 and game.home_team.conference == game.away_team.conference:
            game.tight_race = True

def playoff_standing_update(league, season):
    for team in league.all_teams:
        if team.playoff_eliminated or team.playoff_clinched:
            continue

        if team.playoff_eliminated and team.playoff_near_eliminated:
            team.playoff_near_eliminated = False

        if league.conferences[team.conference].index(team) < league.playoff_cutoff:
            if league.conferences[team.conference][league.playoff_cutoff].wins + (len(season.season_schedule) -
                                                                              len(season.season_results) - 1) < team.wins:
                team.playoff_clinched = True
                team.playoff_near_eliminated = False
        else:
            if team.wins + (len(season.season_schedule) - len(season.season_results) - 1) < league.conferences[team.conference][league.playoff_cutoff - 1].wins:
                team.playoff_eliminated = True
            if team.wins + (len(season.season_schedule) - len(season.season_results) - 1) == league.conferences[team.conference][league.playoff_cutoff - 1].wins:
                team.playoff_near_eliminated = True

        if season.week == 14:
            team.playoff_near_eliminated = False
            if league.conferences[team.conference].index(team) < league.playoff_cutoff:
                team.playoff_clinched = True
            else:
                team.playoff_eliminated = True

def team_updates(season):
    for game in season.season_schedule[season.week - 1]:
        if game.winner == "home":
            game.home_team.wins += 1
            game.home_team.win_loss += 1
            game.home_team.win_streak += 1
            game.home_team.lose_streak = 0
            game.away_team.losses += 1
            game.away_team.win_loss -= 1
            game.away_team.lose_streak += 1
            game.away_team.win_streak = 0
        else:
            game.home_team.losses += 1
            game.home_team.win_loss -= 1
            game.home_team.lose_streak += 1
            game.home_team.win_streak = 0
            game.away_team.wins += 1
            game.away_team.win_loss += 1
            game.away_team.win_streak += 1
            game.away_team.lose_streak = 0

        game.home_team.total_points += game.score_home
        game.home_team.scores += game.score_home
        game.home_team.opponent_points += game.score_away
        game.away_team.total_points += game.score_away
        game.away_team.scores += game.score_away
        game.away_team.opponent_points += game.score_home

def season_update(season):
    if season.week < len(season.season_schedule):
        season.season_results.append(season.season_schedule[season.week - 1])
        season.week += 1
    else:
        season.season_results.append(season.season_schedule[season.week - 1])
        season.week += 1
        season.playoff = True

def weekly_update(league, season):
    simulate_week(season)
    team_updates(season)
    update_rivalry(league, season)
    update_standings(league)
    prestige_update(league)
    playoff_standing_update(league, season)
    season_update(season)
    if not season.playoff:
        update_rivalry_week(league, season)
        update_headlines(season)
        create_times(league, season)

        return "weekly_results_new"
    else:
        return "weekly_results_final"
