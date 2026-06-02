from Interface.utility_functions import get_yes_no
from Interface.menus import *
from Interface.Screens.schedules import *
from Interface.Screens.admin import *
from Interface.Screens.standings import *
from Interface.Screens.statistics import *
from Interface.Screens.playoffs import *
from Engine.Processes.general_processes import *
from Engine.Updates.weekly_update import weekly_update

def game_control(league, season):
    menus = {
        "main": lambda: main_menu(),
        "schedule": lambda: schedule_menu(),
        "admin": lambda: admin_menu(),
        "standings": lambda: standings_menu(),
        "stats": lambda: stats_menu(),
        "archive": lambda: archive_menu()
    }

    schedule_screens = {
        "season_schedule": lambda: print_schedule(season),
        "upcoming_schedule": lambda: upcoming_week(season),
        "week_schedule": lambda: print_week(season),
        "team_schedule": lambda: print_team(season, league.user_team),
        "results": lambda: print_results(season),
        "weekly_results": lambda: print_weekly_results(season),
        "weekly_results_new": lambda: print_weekly_results(season, "main"),
        "weekly_results_final": lambda: print_weekly_results(season, "playoff")
    }

    admin_screens = {
        "season_status": lambda: season_status(league.user_team)
    }

    standings_screens = {
        "full_standings": lambda: print_standings(league),
        "division_standings": lambda: print_division_standings(league),
        "conference_standings": lambda: print_conference_standings(league)
    }

    statistics_screens = {
        "user_stats": lambda: single_team_stats(league.user_team),
        "full_stats": lambda: master_stats_menu(league),
        "single_team_stats": lambda: single_team_stats(find_team(league))
    }

    playoff_screens = {
        "playoff": lambda: print_playoff_schedule()
    }

    processes = {
        "sim_week": lambda: weekly_update(league, season)
    }

    all_paths = [menus, schedule_screens, admin_screens, standings_screens, statistics_screens, playoff_screens]

    UI_state = "main"
    path_exists = False

    while True:
        for path in all_paths:
            if UI_state in path:
                path_exists = True
                UI_state = path[UI_state]()
        if UI_state == "quit":
            if get_yes_no("Are you sure you want to quit?"):
                break
            else:
                UI_state = "main"
        if not path_exists:
            raise ValueError("Path not found")

        if UI_state in processes:
            UI_state = processes[UI_state]()


        path_exists = False



