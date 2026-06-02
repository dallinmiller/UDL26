from Interface.utility_functions import get_continue, clear_screen, get_int
from tabulate import tabulate

def print_schedule(season):
    for week_number, week in enumerate(season.season_schedule, start=1):
        week_table = []

        for game in week:
            week_table.append(
                [game.match_time if game.match_time != "Time not set" else "",
                 game.home_team.city, "vs", game.away_team.city]
            )

        headers = [f"Week {week_number}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return "schedule"

    
def print_week(season):
    week = get_int("What week would you like to see? ")

    while week < 1 or week > len(season.season_schedule):
        week = get_int("Enter a valid week number. ")
        clear_screen()

    week_table = []

    for game in season.season_schedule[week - 1]:
        week_table.append(
            [game.match_time if game.match_time != "Time not set" else "",
             game.home_team.city, "vs", game.away_team.city]
        )

    headers = [f"Week {week}", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return "schedule"

def upcoming_week(season):
    week_table = []

    for game in season.season_schedule[season.week - 1]:
        week_table.append(
            [game.match_time if game.match_time != "Time not set" else "",
             game.home_team.city, "vs", game.away_team.city]
        )

    headers = [f"Week {season.week}", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return "schedule"

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
                [game.match_time if game.match_time != "Time not set" else "",
                 game.home_team.city, "vs", game.away_team.city]
            )

    headers = [f"Week {week}", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return "schedule"


def print_team(season, team):
    week_table = []

    for week_number, week in enumerate(season.season_schedule, start=1):
        for game in week:
            if game.home_team == team or game.away_team == team:
                week_table.append(
                    [game.match_time if game.match_time != "Time not set" else "",
                     game.home_team.city, "vs", game.away_team.city]
                )

    headers = ["Week", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return "schedule"

def print_results(season):
    for week_number, week in enumerate(season.season_results, start=1):

        week_table = []

        for game in week:
            if game.played:
                week_table.append([
                    game.match_time if game.match_time != "Time not set" else "",
                    f"{game.score_home}",
                    game.home_team.city,
                    "vs",
                    game.away_team.city,
                    f"{game.score_away}"
                ])
            else:
                week_table.append([
                    game.match_time if game.match_time != "Time not set" else "",
                    "-",
                    game.home_team.city,
                    "vs",
                    game.away_team.city,
                    "-"
                ])

        headers = [f"Week {week_number}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))
        print("\n\n")

    get_continue()
    return "schedule"

def print_weekly_results(season, UI_next="schedule"):
    week_table = []

    for game in season.season_results[season.week - 2]:
        if game.played:
            week_table.append([
                game.match_time if game.match_time != "Time not set" else "",
                f"{game.score_home}",
                game.home_team.city,
                "vs",
                game.away_team.city,
                f"{game.score_away}"
            ])
        else:
            week_table.append([
                game.match_time if game.match_time != "Time not set" else "",
                "-",
                game.home_team.city,
                "vs",
                game.away_team.city,
                "-"
            ])

    headers = [f"Week {season.week - 1}", "", "Home Team", "", "Away Team", ""]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))
    print("\n\n")

    get_continue()
    return UI_next
