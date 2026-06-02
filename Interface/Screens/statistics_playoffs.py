from Interface.utility_functions import get_continue, clear_screen
from Engine.Processes.general_processes import *
from Engine.Processes.statistic_calculation import *
from tabulate import tabulate

stat_names = ["Team", "W", "L", "P", "PPG", "OP", "OPPG", "PD"]

def single_team_stats_playoff(team, league):
    a, b, c, d, e, f, g = team.return_playoff_stats()
    stats_table = [[f"{team.city} {team.name}", a, b, c, d, e, f, g]]

    print(tabulate(stats_table, headers=stat_names, tablefmt="grid"))
    print("\n\n")


    get_continue()
    return "playoff_stats"

def master_stats_playoff(league, sorting_index):
    stats_table = master_stats_return_playoff(league)

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


def master_stats_menu_playoff(league):
    master_stats_playoff(league, 0)
    while True:
        options = ["Wins", "Losses", "Points", "PPG", "Opponent Points",
                   "Opponent PPG", "Point Differential", "Back"]  # Update with Game
        choice = create_menu("Sort?", options)
        clear_screen()
        if choice < 8:
            master_stats_playoff(league, choice)
        elif choice == 8:
            return "playoff_stats"
        else:
            print("Invalid Response: Retry")
