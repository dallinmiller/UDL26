from Interface.utility_functions import get_continue

def season_status(user_team):
    print(f"{user_team.city} {user_team.name} current status: {user_team.season_status}")

    get_continue()
    return "admin"
