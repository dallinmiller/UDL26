from Interface.utility_functions import create_menu

# Assigns user to team
def initialize_user(league):
    team_names = []
    for team in league.all_teams:
        team_names.append(f"{team.city} {team.name}")
    team_choice = create_menu("Select a Team", team_names)
    league.all_teams[team_choice - 1].user = True
    league.user_team = league.all_teams[team_choice - 1]
