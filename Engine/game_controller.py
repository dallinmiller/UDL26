from Interface.utility_functions import clear_screen
from Interface.menus import *
from Interface.Screens.schedules import *
from Interface.Screens.standings import *

def game_control(league, season):
    menus = {
        "main": lambda: main_menu(),
        "schedule": lambda: schedule_menu(),
        "admin": lambda: admin_menu(),
        "standings": lambda: standings_menu()
    }

    schedule_screens = {
        "season_schedule": lambda: print_schedule(season),
        "week_schedule": lambda: print_week(season),
        "team_schedule": lambda: print_team(season, league.user_team),
        "results": lambda: print_results(season)
    }

    standings_screens = {
        "full_standings": lambda: print_standings(league),
        "division_standings": lambda: print_division_standings(league),
        "conference_standings": lambda: print_conference_standings(league)
    }

    all_paths = [menus, schedule_screens, standings_screens]

    UI_state = "main"
    path_exists = False
    processing = False

    while True:
        for path in all_paths:
            if UI_state in path:
                path_exists = True
                UI_state = path[UI_state]()
        if UI_state == "quit":
            break
        if not path_exists:
            raise ValueError("Path not found")

        path_exists = False



