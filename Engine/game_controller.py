from Interface.utility_functions import clear_screen
from Interface.menus import *
from Interface.Screens.schedules import *

def game_control(league, season):
    menus = {
        "main": lambda: main_menu(),
        "schedule": lambda: schedule_menu(),
        "admin": lambda: admin_menu()
    }

    schedule_screens = {
        "season_schedule": lambda: print_schedule(season),
        "week_schedule": lambda: print_week(season),
        "team_schedule": lambda: print_team(season, league.user_team),
        "results": lambda: print_results(season)
    }

    all_paths = [menus, schedule_screens]

    UI_state = "main"
    processing = False

    while True:
        for path in all_paths:
            if UI_state in path:
                UI_state = path[UI_state]
            else:
                raise ValueError("Unidentified path")
