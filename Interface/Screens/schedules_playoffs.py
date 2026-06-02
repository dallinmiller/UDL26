from Interface.utility_functions import get_continue
from tabulate import tabulate

week_names = [
        "Conference Semis",
        "Conference Finals",
        "Semifinals",
        "Finals"
    ]

def print_schedule_playoff(season, UI_next="playoff_schedule"):
    # TODO: Update to fancy screen
    for i, week in enumerate(season.playoff_schedule, start=0):
        week_table = []

        for game in week:
            week_table.append(
                [game.match_time if game.match_time != "Time not set" else "",
                 game.home_team.city, "vs", game.away_team.city]
            )

        headers = [f"{week_names[i]}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return UI_next

def print_upcoming_schedule_playoff(season):
    week_table = []

    for game in season.playoff_schedule[season.playoff_week - 1]:
        week_table.append(
            [game.match_time if game.match_time != "Time not set" else "",
             game.home_team.city, "vs", game.away_team.city]
        )

    headers = [f"{week_names[season.playoff_week - 1]}", "Home Team", "", "Away Team"]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))

    print("\n\n")
    get_continue()
    return "playoff_schedule"

def print_results_playoff(season):
    for i, week in enumerate(season.playoff_results, start=0):

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

        headers = [f"{week_names[season.playoff_week - 1]}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))
        print("\n\n")

    get_continue()
    return "playoff_schedule"

def print_weekly_results_playoff(season, UI_next="playoff_schedule"):
    week_table = []

    for game in season.playoff_results[season.playoff_week - 2]:
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

    headers = [f"{week_names[season.playoff_week - 2]}", "", "Home Team", "", "Away Team", ""]
    print(tabulate(week_table, headers=headers, tablefmt="grid"))
    print("\n\n")



    get_continue()
    return UI_next