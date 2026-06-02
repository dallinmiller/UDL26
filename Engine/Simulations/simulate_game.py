import random

def rating_variation(game):
    teams = [game.home_team, game.away_team]
    variations = []
    for team in teams:
        if team.season_status == "Confident":
            variations.append([2, 0])
        elif team.season_status == "Calm":
            variations.append([0, 0])
        elif team.season_status == "Anxious":
            variations.append([-2, 4])
        elif team.season_status == "Desperate":
            variations.append([-4, 7])
        else:
            variations.append([-5, 2])

    if game.match_time == "6:00":
        for team in variations:
            team[1] += 1

    elif game.match_time == "12:00":
        for team in variations:
            team[1] += 0.5

    return variations

def simulate_prep(game):
    variation = rating_variation(game)
    home_rating = 15.2 + variation[0][0]
    home_variability = 3 + variation[0][1]
    away_rating = 15 + variation[1][0]
    away_variability = 3 + variation[1][1]

    return home_rating, home_variability, away_rating, away_variability

def simulate(game):
    home_rating, home_variation, away_rating, away_variation = simulate_prep(game)
    game.score_home = random.normalvariate(home_rating, home_variation)
    game.score_away = random.normalvariate(away_rating, away_variation)
    if game.score_home > game.score_away:
        game.winner = "home"
    else:
        game.winner = "away"
    game.score_home = round(game.score_home)
    game.score_away = round(game.score_away)
    if game.score_home < 5:
        game.score_home = 5
    if game.score_away < 5:
        game.score_away = 5
    if game.score_home == game.score_away:
        game.overtime = True
        if game.winner == "home":
            game.score_home += 1
        else:
            game.score_away += 1
    game.played = True
