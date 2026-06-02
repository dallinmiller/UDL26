from Engine.Simulations.simulate_week import simulate_week
from Engine.Updates.standing_update import update_standings
from Engine.Updates.time_update import create_times
from Engine.Processes.statistic_calculation import master_stats_return_team

def get_prestige_info(league, team):
    league_rank = league.all_teams.index(team) + 1

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

    return league_rank, conference_leader, ppg_leader, oppg_leader

def prestige_update(league, team):
    rank, conference_leader, ppg_leader, oppg_leader = get_prestige_info(league, team)
    if rank <= 8:
        prestige = 4 - (1 / 8) * rank
    else:
        prestige = 3 - (3 / 64) * (rank - 8) ** 2

    if conference_leader:
        prestige += 0.5
    if ppg_leader:
        prestige += 0.5
    if oppg_leader:
        prestige += 0.5

    team.prestige = prestige

def team_updates(game):
    if game.winner == "home":
        game.home_team.wins += 1
        game.home_team.win_loss += 1
        game.away_team.losses += 1
        game.away_team.win_loss -= 1
    else:
        game.home_team.losses += 1
        game.home_team.win_loss -= 1
        game.away_team.wins += 1
        game.away_team.win_loss += 1

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
    for game in season.season_schedule[season.week - 1]:
        team_updates(game)
    update_standings(league)
    for team in league.all_teams:
        prestige_update(league, team)
    season_update(season)
    if not season.playoff:
        create_times(season)
        return "weekly_results_new"
    else:
        return "weekly_results_final"
