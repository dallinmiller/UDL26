from tabulate import tabulate
from Interface.utility_functions import get_continue

def print_rivalries(league, controlled=True, UI_next="archive"):
    rivalry_scores = []

    for i in range(15):
        team_rivalry_scores = [league.all_teams[i].city]
        for completed in range(i):
            team_rivalry_scores.append("|||")
        for j in range(i + 1, 15):
            key = tuple(sorted((i, j)))
            team_rivalry_scores.append(league.rivalries[key])
        rivalry_scores.append(team_rivalry_scores)

    headers = ["Rivalries"]
    for team in league.all_teams[1:]:
        headers.append(team.city)
    print(tabulate(rivalry_scores, headers=headers, tablefmt="grid"))

    if controlled:
        print("\n\n")
        get_continue()

    return UI_next