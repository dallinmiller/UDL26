from Interface.utility_functions import get_yes_no
from Interface.menus import *
from Interface.Screens.schedules import *
from Interface.Screens.admin import *
from Interface.Screens.standings import *
from Interface.Screens.statistics import *
from Interface.Screens.schedules_playoffs import *
from Interface.Screens.statistics_playoffs import *
from Engine.Initializations.playoff_initialization import *
from Engine.Initializations.initialize_new_season import *
from Engine.Processes.general_processes import *
from Engine.Updates.weekly_update import weekly_update
from Engine.Updates.playoff_update import *

def game_control(league, season):
    menus = {
        "main": lambda: main_menu(league, season),
        "schedule": lambda: schedule_menu(),
        "admin": lambda: admin_menu(),
        "standings": lambda: standings_menu(),
        "stats": lambda: stats_menu(),
        "archive": lambda: archive_menu(),
        "playoff": lambda: playoff_menu(league, season),
        "playoff_schedule": lambda: playoff_schedule_menu(),
        "playoff_standings": lambda: standings_menu("playoff"),
        "playoff_admin": lambda: playoff_admin_menu(),
        "playoff_stats_branch": lambda: playoff_stats_branch_menu(),
        "playoff_stats_reg": lambda: stats_menu("playoff"),
        "playoff_stats": lambda: playoff_stats_menu(),
        "playoff_archive": lambda: archive_menu("playoff")
    }

    schedule_screens = {
        "season_schedule": lambda: print_schedule(season),
        "upcoming_schedule": lambda: upcoming_week(season),
        "week_schedule": lambda: print_week(season),
        "team_schedule": lambda: print_team(season, league.user_team),
        "results": lambda: print_results(season),
        "weekly_results": lambda: print_weekly_results(season),
        "weekly_results_new": lambda: print_weekly_results(season, "main"),
        "weekly_results_final": lambda: print_weekly_results(season, "playoff_init")
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
        "single_team_stats": lambda: single_team_stats(find_team(league)),
        "week_schedule": lambda: print_week(season),
        "team_schedule": lambda: print_team(season, league.user_team),
    }

    playoff_screens = {
        "print_schedule_playoff": lambda: print_schedule_playoff(season),
        "upcoming_schedule_playoff": lambda: print_upcoming_schedule_playoff(season),
        "playoff_results": lambda: print_results_playoff(season),
        "season_schedule_playoff": lambda: print_schedule(season, "playoff_schedule"),
        "week_schedule_playoff": lambda: print_week(season, "playoff_schedule"),
        "team_schedule_playoff": lambda: print_team(season, league.user_team, "playoff_schedule"),
        "results_playoff": lambda: print_results(season, "playoff_schedule"),
        "playoff_results_new": lambda: print_weekly_results_playoff(season, "playoff"),
        "playoff_results_final": lambda:print_weekly_results_playoff(season, "champion_page"),
        "champion_page": lambda:print_champion(league, "end_season")
    }

    playoff_admin_screens = {
        "season_status_playoff": lambda:season_status(league.user_team, "playoff_admin")
    }

    playoff_standings_screens = {
        "full_standings_playoff": lambda: print_standings(league, "playoff_standings"),
        "division_standings_playoff": lambda: print_division_standings(league, "playoff_standings"),
        "conference_standings_playoff": lambda: print_conference_standings(league, "playoff_standings")
    }

    playoff_stats_screens = {
        "user_stats_playoff": lambda: single_team_stats(league.user_team, "playoff_stats_reg"),
        "full_stats_playoff": lambda: master_stats_menu(league, "playoff_stats_reg"),
        "single_team_stats_playoff": lambda: single_team_stats(find_team(league), "playoff_stats_reg"),
        "playoff_user_stats": lambda: single_team_stats_playoff(league.user_team, league),
        "playoff_full_stats": lambda: master_stats_menu_playoff(league)
    }

    processes = {
        "sim_week": lambda: weekly_update(league, season),
        "playoff_init": lambda: playoff_initialization(league, season),
        "sim_week_playoff": lambda: weekly_update_playoff(league, season),
        "end_season": lambda: initialize_new_season(league, season)
    }

    test = {
        "playoff_test": lambda:weekly_update(league, season)
    }

    all_paths = [menus, schedule_screens, admin_screens, standings_screens, statistics_screens, playoff_screens,
                 playoff_admin_screens, playoff_standings_screens, playoff_stats_screens]

    UI_state = "main"
    path_exists = False

    while True:
        for path in all_paths:
            if UI_state in path:
                path_exists = True
                UI_state = path[UI_state]()
        if UI_state in test:
            path_exists = True
        if UI_state == "quit":
            if get_yes_no("Are you sure you want to quit? y/n"):
                break
            else:
                UI_state = "main"
        if not path_exists:
            raise ValueError("Path not found")

        # Set UI_state to "playoff_test" to skip regular season
        if UI_state in test:
            if season.playoff:
                UI_state = "playoff_init"
            else:
                test[UI_state]()
                UI_state = "playoff_test"

        if UI_state in processes:
            UI_state = processes[UI_state]()

        path_exists = False
