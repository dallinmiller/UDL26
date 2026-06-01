from Interface.utility_functions import clear_screen, create_menu

def main_menu():
    options = [
        ("Schedule Menu", "schedule"),
        ("Admin Menu", "admin"),
        ("Standings", "standings"),
        ("Statistics", "statistics"),
        ("Next Game", "next_game"),
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
        ("Week Schedule", "week_schedule"),
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
