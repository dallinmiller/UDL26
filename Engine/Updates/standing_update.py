def update_process(grouping):
    for group in grouping:
        for j in range(len(group)):
            for i in range(len(group) - 1):
                if group[i + 1].wins > group[i].wins:
                    group[i], group[i + 1] = group[i + 1], group[i]
                elif group[i + 1].wins == group[i].wins:
                    if group[i + 1].return_score_differential() > group[i].return_score_differential():
                        group[i], group[i + 1] = group[i + 1], group[i]
                    elif group[i + 1].return_score_differential() == group[i].return_score_differential():
                        if group[i + 1].total_points > group[i].total_points:
                            group[i], group[i + 1] = group[i + 1], group[i]

def update_standings(league):
    conferences = [league.conferences["aac"], league.conferences["cmc"], league.conferences["mnc"],
                   league.conferences["owc"]]
    update_process(conferences)
    divisions = [league.divisions["front"], league.divisions["back"]]
    update_process(divisions)
    whole_league = [league.all_teams]
    update_process(whole_league)
