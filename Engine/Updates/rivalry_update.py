def update_rivalry(league, season):
    if season.playoff:
        schedule = season.playoff_schedule[season.playoff_week - 1]
    else:
        schedule = season.season_schedule[season.week - 1]

    for game in schedule:
        team_id_1 = game.home_team.league_index
        team_id_2 = game.away_team.league_index
        score = 0

        score_differential_scores = [15, 11, 8, 5, 4, 3, 2]

        if game.overtime:
            score += 20
        elif abs(game.score_home - game.score_away) <= 7:
            score += score_differential_scores[abs(game.score_home - game.score_away) - 1]

        if game.rivalry:
            score += 5
        if game.tight_race:
            score += 10
        if game.playoff_implication:
            score += 10

        if season.playoff:
            score += 10
            if season.playoff_week == 3:
                score += 5
            elif season.playoff_week == 4:
                score += 15

        key = tuple(sorted((team_id_1, team_id_2)))
        league.rivalries[key] += score
        league.rivalries_added += score

def update_rivalry_week(league, season):
    if season.week <= 14 and not season.playoff:
        for game in season.season_schedule[season.week - 1]:
            home_id = game.home_team.league_index
            away_id = game.away_team.league_index
            key = tuple(sorted((home_id, away_id)))
            if league.rivalries[key] > 150:
                game.rivalry = True
    else:
        if season.playoff:
            for game in season.playoff_schedule[season.playoff_week - 1]:
                home_id = game.home_team.league_index
                away_id = game.away_team.league_index
                key = tuple(sorted((home_id, away_id)))
                if league.rivalries[key] > 150:
                    game.rivalry = True

def rivalry_reset(league):
    for rivalry_key in league.rivalries:
        league.rivalries[rivalry_key] *= 0.9
