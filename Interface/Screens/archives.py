from tabulate import tabulate
from Interface.utility_functions import get_continue

def print_rivalries(league, controlled=True, UI_next="archive"):
    num_teams = len(league.league)
    rivalry_scores = []

    for i in range(num_teams):
        row = [league.league[i].city]

        for _ in range(i):
            row.append("—")

        for j in range(i + 1, num_teams):
            key = tuple(sorted((i, j)))
            row.append(round(league.rivalries.get(key, 0), 3))

        rivalry_scores.append(row)

    headers = ["Team"]
    headers.extend(team.city for team in league.league[1:])

    print(tabulate(rivalry_scores, headers=headers, tablefmt="grid"))

    if controlled:
        print()
        get_continue()

    return UI_next