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

def standings_menu():
    options = [
        ("Full Standings", "full_standings"),
        ("Division Standings", "division_standings"),
        ("Conference Standings", "conference_standings"),
        ("Back", "main")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def stats_menu():
    options = [
        ("User Stats", "user_stats"),
        ("Full Stats", "full_stats"),
        ("Single Team Stats", "single_team_stats"),
        ("Back", "main")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]

def archive_menu():
    options = [
        ("Back", "main")
    ]

    labels = [label for label, _ in options]

    choice = create_menu("Select an Option", labels)

    clear_screen()

    return options[choice - 1][1]
