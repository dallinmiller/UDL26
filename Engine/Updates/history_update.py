from History.histories import *

def league_history_update(league):
    all_teams_list = []
    playoff_teams_list = []
    conference_finals_list = []
    semifinals_list = []
    finals_list = []
    
    history_lists = [playoff_teams_list, conference_finals_list, semifinals_list]
    
    conference_lists = [league.playoff_teams, league.conference_final_teams, league.semifinal_teams]
    
    for team in league.all_teams:
        all_teams_list.append([team.city, team.name, team.wins, team.losses, team.total_points, team.opponent_points])
    
    for i, league_list in enumerate(conference_lists):
        for conf_div in league_list.values():
            for team in conf_div:
                history_lists[i].append([team.city, team.name])

    for team in league.final_teams:
        finals_list.append([team.city, team.name])

    champion = [league.champion.city, league.champion.name]
    
    league_histories.append(LeagueHistory(all_teams_list, playoff_teams_list, conference_finals_list, semifinals_list, 
                                          finals_list, champion))
    
def season_history_update(season):
    season_number = season.season_number
    
    season_results_history = []
    playoff_results_history = []
    
    for week in season.season_results:
        week_history = []
        for game in week:
            week_history.append(game)
        season_results_history.append(week_history)
    
    for week in season.playoff_results:
        week_history = []
        for game in week:
            week_history.append(game)
        playoff_results_history.append(week_history)
        
    season_histories.append(SeasonHistory(season_number, season_results_history, playoff_results_history))
            
def team_history_update(team):
    team.team_history.wins += team.wins
    team.team_history.losses += team.losses
    team.team_history.win_loss = team.team_history.wins - team.team_history.losses
    team.team_history.total_points += team.total_points
    team.team_history.scores += team.scores
    team.team_history.callahan += team.callahan
    team.team_history.total_yards += team.total_yards
    team.team_history.turnovers += team.turnovers
    team.team_history.opponent_points += team.opponent_points
    team.team_history.opponent_yards += team.opponent_yards

    if team.playoff_semis:
        team.team_history.conference_semis_appearances += 1
        if team.playoff_wins >= 1:
            team.team_history.conference_final_appearances += 1
        if team.playoff_wins >= 2:
            team.team_history.playoff_semis_appearances += 1
        if team.playoff_wins >= 3:
            team.team_history.playoff_final_appearances += 1
        if team.playoff_wins == 4:
            team.team_history.league_champion += 1
    elif team.playoff_wins + team.playoff_losses > 1:
        team.team_history.conference_final_appearances += 1
        if team.playoff_wins >= 1:
            team.team_history.playoff_semis_appearances += 1
        if team.playoff_wins >= 2:
            team.team_history.playoff_final_appearances += 1
        if team.playoff_wins >= 3:
            team.team_history.league_champion += 1

    team.team_history.playoff_wins += team.playoff_wins
    team.team_history.playoff_losses += team.playoff_losses
    team.team_history.playoff_total_points += team.playoff_total_points
    team.team_history.playoff_scores += team.playoff_scores
    team.team_history.playoff_callahan += team.playoff_callahan
    team.team_history.playoff_total_yards += team.playoff_total_yards
    team.team_history.playoff_turnovers += team.playoff_turnovers
    team.team_history.playoff_opponent_points += team.playoff_opponent_points
    team.team_history.playoff_opponent_yards += team.playoff_opponent_yards