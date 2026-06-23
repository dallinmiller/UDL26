from Interface.utility_functions import create_menu

# Assigns user to team
def initialize_user(league):
    team_names = []
    for team in league.league:
        team_names.append(f"{team.city} {team.name}")
    team_choice = create_menu("Select a Team", team_names)
    league.league[team_choice - 1].user = True
    league.user_team = league.league[team_choice - 1]
