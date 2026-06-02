def master_stats_return(league):
    stats_table = []
    for team in league.all_teams:
        a, b, c, d, e, f, g = team.return_stats()
        stats_table.append([f"{team.city} {team.name}", a, b, c, d, e, f, g])

    return stats_table


def master_stats_return_team(league):
    stats_table = []
    for team in league.all_teams:
        a, b, c, d, e, f, g = team.return_stats()
        stats_table.append([team, a, b, c, d, e, f, g])

    return stats_table

def master_stats_return_playoff(league):
    stats_table = []
    for team in league.all_teams:
        a, b, c, d, e, f, g = team.return_playoff_stats()
        stats_table.append([f"{team.city} {team.name}", a, b, c, d, e, f, g])

    return stats_table
