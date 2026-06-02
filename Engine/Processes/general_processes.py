from Interface.utility_functions import create_menu

def find_team(league):
    names = []
    for i in league.league:
        names.append(f"{i.city} {i.name}")
    team_number = create_menu("Select a Team", names)
    team_choice = league.league[team_number - 1]
    return team_choice