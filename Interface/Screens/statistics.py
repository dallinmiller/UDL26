from Interface.utility_functions import create_menu, get_continue, clear_screen
from tabulate import tabulate

stat_names = ["Team", "W", "L", "P", "PPG", "OP", "OPPG", "PD"]

def find_team(league):
    names = []
    for i in league.league:
        names.append(f"{i.city} {i.name}")
    team_number = create_menu("Select a Team", names)
    team_choice = league.league[team_number - 1]
    return team_choice


def single_team_stats(team):
    a, b, c, d, e, f, g = team.return_stats()
    stats_table = [[f"{team.city} {team.name}", a, b, c, d, e, f, g]]

    print(tabulate(stats_table, headers=stat_names, tablefmt="grid"))
    print("\n\n")

    get_continue()
    return "stats"


def master_stats_return(league):
    stats_table = []
    for team in league.all_teams:
        a, b, c, d, e, f, g = team.return_stats()
        stats_table.append([f"{team.city} {team.name}", a, b, c, d, e, f, g])

    return stats_table


def master_stats_return_team(league):
    stats_table = []
    for team in league.all_teams:
        a, b, c, d, e, f, g = team.return_stats()
        stats_table.append([team, a, b, c, d, e, f, g])

    return stats_table


def master_stats(league, sorting_index):
    stats_table = master_stats_return(league)

    if sorting_index == 0:
        print(tabulate(stats_table, headers=stat_names, tablefmt="grid"))
        print("\n\n")
    else:
        for i in range(len(stats_table)):
            for j in range(len(stats_table) - 1):
                if stats_table[j][sorting_index] < stats_table[j + 1][sorting_index]:
                    stats_table[j], stats_table[j + 1] = stats_table[j + 1], stats_table[j]

        print(tabulate(stats_table, headers=stat_names, tablefmt="grid"))
        print("\n\n")


def master_stats_menu(league):
    master_stats(league, 0)
    while True:
        options = ["Wins", "Losses", "Points", "PPG", "Opponent Points",
                   "Opponent PPG", "Point Differential", "Back"]  # Update with Game
        choice = create_menu("Sort?", options)
        clear_screen()
        if choice < 8:
            master_stats(league, choice)
        elif choice == 8:
            return "stats"
        else:
            print("Invalid Response: Retry")
