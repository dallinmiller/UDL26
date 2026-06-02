from Interface.utility_functions import get_continue
from tabulate import tabulate

def print_standings(league, UI_next="standings"):
    standings_table = []
    all_teams = league.all_teams
    standings_table.append(["", "", "", "", ""])
    for team in all_teams:
        standings_table.append([all_teams.index(team) + 1, f"{team.city} {team.name}", team.wins,
                                team.losses, team.return_score_differential()])

    headers = ["League", "Team", "Wins", "Losses", "Score Differential"]
    print(tabulate(standings_table, headers=headers, tablefmt="grid"))
    print("\n\n")

    get_continue()
    return UI_next


def print_division_standings(league, UI_next="standings"):
    standings_table = []
    divisions = [league.divisions["front"], league.divisions["back"]]
    division_names = ["Front", "Back"]
    for division in divisions:
        standings_table.append(["", "", "", "", ""])
        standings_table.append([division_names[divisions.index(division)], "", "", "", ""])
        for team in division:
            standings_table.append([division.index(team) + 1, f"{team.city} {team.name}", team.wins,
                                    team.losses, team.return_score_differential()])

    headers = ["Division", "Team", "Wins", "Losses", "Score Differential"]
    print(tabulate(standings_table, headers=headers, tablefmt="grid"))
    print("\n\n")

    get_continue()
    return UI_next


def print_conference_standings(league, UI_next="standings"):
    standings_table = []
    conferences = [league.conferences["aac"], league.conferences["cmc"], league.conferences["mnc"],
                   league.conferences["owc"]]
    conference_names = ["AAC", "CMC", "MNC", "OWC"]
    for conference in conferences:
        standings_table.append(["", "", "", "", ""])
        standings_table.append([conference_names[conferences.index(conference)], "", "", "", ""])
        for team in conference:
            standings_table.append([conference.index(team) + 1, f"{team.city} {team.name}", team.wins,
                                    team.losses, team.return_score_differential()])

    headers = ["Conference", "Team", "Wins", "Losses", "Score Differential"]
    print(tabulate(standings_table, headers=headers, tablefmt="grid"))
    print("\n\n")

    get_continue()
    return UI_next
