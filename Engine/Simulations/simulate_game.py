import random

def rating_variation(game):
    teams = [game.home_team, game.away_team]
    variations = []
    for team in teams:
        if team.season_status == "Confident":
            variations.append(game.scoring_settings.confident_scoring)
        elif team.season_status == "Calm":
            variations.append(game.scoring_settings.calm_scoring)
        elif team.season_status == "Anxious":
            variations.append(game.scoring_settings.anxious_scoring)
        elif team.season_status == "Desperate":
            variations.append(game.scoring_settings.desperate_scoring)
        else:
            variations.append(game.scoring_settings.defeated_scoring)

    if game.match_time == "6:00":
        for team in variations:
            team[1] += game.scoring_settings.primetime_variation_bonus

    elif game.match_time == "12:00":
        for team in variations:
            team[1] += game.scoring_settings.noon_variation_bonus

    return variations

def simulate_prep(game):
    variation = rating_variation(game)
    home_rating = game.scoring_settings.home_base_score + variation[0][0]
    home_variability = game.scoring_settings.home_base_variation + variation[0][1]
    away_rating = game.scoring_settings.away_base_score + variation[1][0]
    away_variability = game.scoring_settings.away_base_variation + variation[1][1]

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
    if game.score_home < game.scoring_settings.min_score:
        game.score_home = game.scoring_settings.min_score
    if game.score_away < game.scoring_settings.min_score:
        game.score_away = game.scoring_settings.min_score
    if game.score_home == game.score_away:
        game.overtime = True
        if game.winner == "home":
            game.score_home += 1
        else:
            game.score_away += 1
    game.played = True
