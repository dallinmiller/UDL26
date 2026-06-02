from Interface.utility_functions import clear_screen, create_menu

def main_menu():
    options = [
        ("Schedule Menu", "schedule"),
        ("Admin Menu", "admin"),
        ("Standings", "standings"),
        ("Statistics", "stats"),
        ("Next Game", "sim_week"),
        ("Archive", "archive"),
        ("Quit", "quit")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def schedule_menu():
    options = [
        ("Season Schedule", "season_schedule"),
        ("Upcoming Week", "upcoming_schedule"),
        ("Choose a Week", "week_schedule"),
        ("Team Schedule", "team_schedule"),
        ("Results", "results"),
        ("Back", "main")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def admin_menu():
    options = [
        ("Season Status", "season_status"),
        ("Back", "main")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def standings_menu(UI_next="main"):
    options = [
        ("Full Standings", "full_standings"),
        ("Division Standings", "division_standings"),
        ("Conference Standings", "conference_standings"),
        ("Back", UI_next)
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    if UI_next == "main":
        return options[choice - 1][1]
    elif UI_next == "playoff":
        if options[choice - 1][0] == "Back":
            return UI_next
        else:
            return options[choice - 1][1] + "_playoff"
    else:
        raise ValueError("Invalid UI_next")

def stats_menu(UI_next="main"):
    options = [
        ("User Stats", "user_stats"),
        ("Full Stats", "full_stats"),
        ("Single Team Stats", "single_team_stats"),
        ("Back", "main")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    if UI_next == "main":
        return options[choice - 1][1]
    elif UI_next == "playoff":
        if options[choice - 1][0] == "Back":
            return UI_next
        else:
            return options[choice - 1][1] + "_playoff"
    else:
        raise ValueError("Invalid UI_next")

def archive_menu(UI_next="main"):
    options = [
        ("Back", UI_next)
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    if UI_next == "main":
        return options[choice - 1][1]
    elif UI_next == "playoff":
        if options[choice - 1][0] == "Back":
            return UI_next
        else:
            return options[choice - 1][1] + "_playoff"
    else:
        raise ValueError("Invalid UI_next")

def playoff_menu():
    options = [
        ("Schedule Menu", "playoff_schedule"),
        ("Admin Menu", "playoff_admin"),
        ("Standings", "playoff_standings"),
        ("Statistics", "playoff_stats_branch"),
        ("Next Game", "sim_week_playoff"),
        ("Archive", "playoff_archive"),
        ("Quit", "quit")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def playoff_schedule_menu():
    options = [
        ("Playoff Schedule", "print_schedule_playoff"),
        ("Upcoming Week", "upcoming_schedule_playoff"),
        ("Playoff Results", "playoff_results"),
        ("Season Schedule", "season_schedule_playoff"),
        ("Choose a Week", "week_schedule_playoff"),
        ("Team Schedule", "team_schedule_playoff"),
        ("Season Results", "results_playoff"),
        ("Back", "playoff")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def playoff_admin_menu():
    options = [
        ("Season Status", "season_status_playoff"),
        ("Back", "playoff")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def playoff_stats_branch_menu():
    options = [
        ("Regular Season", "playoff_stats_reg"),
        ("Playoffs", "playoff_stats"),
        ("Back", "playoff")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def playoff_stats_menu():
    options = [
        ("User Stats", "playoff_user_stats"),
        ("Full Stats", "playoff_full_stats"),
        ("Back", "playoff")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()
    return options[choice - 1][1]
