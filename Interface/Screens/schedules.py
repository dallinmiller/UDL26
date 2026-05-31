from Interface.utility_functions import get_continue, clear_screen, get_int
from tabulate import tabulate

def print_schedule(season):
    for week_number, week in enumerate(season.season_schedule, start=1):
        week_table = []

        for game in week:
            week_table.append(
                ["", game.home_team, "vs", game.away_team]
            )

        headers = [f"Week {week_number}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()

    
def print_week(season):
    week = get_int("What week would you like to see? ")

    while week < 1 or week > len(season.season_schedule):
        week = get_int("Enter a valid week number. ")
        clear_screen()

    week_table = []

    for game in season.season_schedule[week - 1]:
        week_table.append(
            ["", game.home_team, "vs", game.away_team]
        )

    headers = [f"Week {week}", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()


def find_schedule(season, team):
    team_schedule = []

    for week in season.season_schedule:
        for game in week:
            if game.home_team == team or game.away_team == team:
                team_schedule.append(game)

    return team_schedule

def print_match(season, team):
    week = get_int("What week would you like to see? ")

    while week < 1 or week > len(season.season_schedule):
        week = get_int("Enter a valid week number. ")
        clear_screen()

    week_table = []

    for game in season.season_schedule[week - 1]:
        if game.home_team == team or game.away_team == team:
            week_table.append(
                ["", game.home_team, "vs", game.away_team]
            )

    headers = [f"Week {week}", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()


def print_team(schedule, team):
    week_table = []

    for week_number, week in enumerate(schedule, start=1):
        for game in week:
            if game.home_team == team or game.away_team == team:
                week_table.append(
                    [f"Week {week_number}", game.home_team, "vs", game.away_team]
                )

    headers = ["Week", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()

def print_results(season):
    for week_number, week in enumerate(season.all_results, start=1):

        week_table = []

        for game in week:
            if game.played:
                week_table.append([
                    "",
                    f"{game.home_score}",
                    game.home_team,
                    "vs",
                    game.away_team,
                    f"{game.away_score}"
                ])
            else:
                week_table.append([
                    "",
                    "-",
                    game.home_team,
                    "vs",
                    game.away_team,
                    "-"
                ])

        headers = [f"Week {week_number}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))
        print("\n\n")

    get_continue()

