from Interface.utility_functions import get_continue

def season_status(user_team, UI_next="admin"):
    print(f"{user_team.city} {user_team.name} current status: {user_team.season_status}")

    get_continue()
    return UI_next
