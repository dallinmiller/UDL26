from Assets.Text.Headlines import *
from Interface.utility_functions import *
from History.histories import league_histories
import random
from difflib import SequenceMatcher

def headline_harvest(season):
    headlines = []
    return_type = "game"

    if season.week == 1 and season.season_number != 1:
        return_type = "team"
        headlines.append(first_week_headlines())
        headlines.append(first_week_headlines(league_histories[season.season_number - 2].champion, 1))
        for team in league_histories[season.season_number - 2].playoff_teams:
            if team[0] != league_histories[season.season_number - 2].champion[0]:
                headlines.append(first_week_headlines(team, 2))

        return headlines, return_type

    if season.week == 1:
        return_type = "none"
        headlines = first_week_headlines()[0]

        return headlines, return_type

    if season.week == 2:
        headlines.append(second_week_headlines())
    if season.week == 3:
        headlines.append(third_week_headlines())
    if season.week == 4:
        headlines.append(fourth_week_headlines())
    if season.week == 14:
        headlines.append(final_week_headlines())

    for game in season.season_results[season.week - 2]:
        game_winner = game.home_team if game.winner == "home" else game.away_team
        game_loser = game.home_team if game.winner == "away" else game.away_team

        teams = [game_winner, game_loser]

        team_status = ["None", "None"]

        if 3 <= season.week < 6:
            for team_index, team in enumerate(teams):
                if team.standing <= 8:
                    team_status[team_index] = "contender"
                else:
                    team_status[team_index] = "middler"

        elif season.week >= 6:
            for team_index, team in enumerate(teams):
                if team.standing <= 3:
                    team_status[team_index] = "top_team"
                elif team.standing <= 7:
                    team_status[team_index] = "contender"
                elif team.standing <= 12:
                    team_status[team_index] = "middler"
                else:
                    team_status[team_index] = "bottom"


        if team_status[0] == "top_team":
            headlines.append(top_team_headlines(game, 0))
            if abs(game.score_home - game.score_away) <= 2:
                headlines.append(top_team_headlines(game, 1))
            if team_status[1] == "contender":
                if abs(game.score_home - game.score_away) <= 2:
                    headlines.append(contender_headlines(game, 3))
            if team_status[1] == "middler":
                if abs(game.score_home - game.score_away) <= 2:
                    headlines.append(middler_headlines(game, 1))
                    headlines.append(close_game_headlines(game, 2))
            if team_status[1] == "bottom":
                if abs(game.score_home - game.score_away) <= 2:
                    headlines.append(close_game_headlines(game, 2))
        if team_status[1] == "top_team":
            if team_status[0] == "contender":
                headlines.append(contender_headlines(game, 0))
            if team_status[0] == "middler" or team_status[0] == "bottom":
                headlines.append(top_team_headlines(game, 2))
                if team_status[0] == "middler":
                    headlines.append(middler_headlines(game, 0))
                if team_status[0] == "bottom":
                    headlines.append(bottom_feeder_headlines(game, 1))
                if abs(game.score_home - game.score_away) >= 8:
                    headlines.append(blowout_headlines(game, 2))
        if team_status[0] == "contender":
            if game_winner.win_streak == 4:
                headlines.append(contender_headlines(game, 2))
        if team_status[1] == "contender":
            if team_status[0] == "middler" or team_status[0] == "bottom":
                headlines.append(contender_headlines(game, 1))
                if team_status[0] == "bottom":
                    headlines.append(bottom_feeder_headlines(game, 1))
                    if abs(game.score_home - game.score_away) >= 8:
                        headlines.append(blowout_headlines(game, 2))
        if team_status[0] == "middler":
            if game_winner.win_streak == 3:
                headlines.append(middler_headlines(game, 2))
        if team_status[1] == "middler":
            if abs(game.score_home - game.score_away) >= 8:
                if team_status[0] == "top_team":
                    headlines.append(blowout_headlines(game, 1))
            if game_winner.playoff_near_eliminated:
                headlines.append(middler_headlines(game, 3))
        if team_status[0] == "bottom":
            if game_winner.win_streak == 3:
                headlines.append(bottom_feeder_headlines(game, 2))
        if team_status[1] == "bottom":
            headlines.append(bottom_feeder_headlines(game, 0))
            if abs(game.score_home - game.score_away) >= 8:
                if team_status[0] == "contender" or team_status[0] == "top_team":
                    headlines.append(blowout_headlines(game, 1))
            if game_loser.playoff_eliminated:
                headlines.append(bottom_feeder_headlines(game, 3))

        if abs(game.score_home - game.score_away) <= 2:
            headlines.append(close_game_headlines(game, 0))
            if game.rivalry:
                headlines.append(rivalry_headlines(game, 1))
            if game.tight_race:
                headlines.append(tight_race_headlines(game, 1))
            if season.playoff:
                headlines.append(playoff_headlines(game, 0))
        if game.overtime:
            headlines.append(close_game_headlines(game, 1))
            if game.rivalry:
                headlines.append(rivalry_headlines(game, 2))
            if game.tight_race:
                headlines.append(tight_race_headlines(game, 2))
        if abs(game.score_home - game.score_away) >= 8:
            headlines.append(blowout_headlines(game, 0))
            if game.rivalry:
                headlines.append(rivalry_headlines(game, 3))
            if game.tight_race:
                headlines.append(tight_race_headlines(game, 3))
            if season.playoff:
                headlines.append(playoff_headlines(game, 1))
        if game.rivalry:
            if season.playoff:
                headlines.append(playoff_headlines(game, 2))

        if season.week == 2:
            headlines.append(second_week_headlines(game, 1))
            headlines.append(second_week_headlines(game, 2))
        if season.week == 3:
            if game_winner.win_streak == 2:
                headlines.append(third_week_headlines(game, 1))
            if game_winner.lose_streak == 2:
                headlines.append(third_week_headlines(game, 2))
        if season.week == 4:
            if game_winner.win_streak == 3:
                headlines.append(fourth_week_headlines(game, 1))
            if game_winner.lose_streak == 3:
                headlines.append(fourth_week_headlines(game, 2))
        ### TODO: Test pre-playoff conditions
        if season.week >= 9 and not season.playoff:
            if team_status[0] == "contender" or team_status[0] == "top_team":
                headlines.append(down_the_stretch_headlines(game, 1))
            if team_status[0] == "middler" and not game_winner.playoff_eliminated:
                headlines.append(down_the_stretch_headlines(game, 2))
        if season.week == 14 and not season.playoff:
            if game_loser.playoff_near_eliminated:
                headlines.append(final_week_headlines(game, 2))
        if season.playoff_week == 1 and season.playoff:
            if game_winner.playoff_near_eliminated and game_winner.playoff_clinched:
                headlines.append(final_week_headlines(game, 1))
            if game_winner.playoff_clinched:
                headlines.append(conference_semis_headlines(game, 1))
            if game_loser.playoff_eliminated:
                headlines.append(conference_semis_headlines(game, 2))
            if game_winner.playoff_clinched and not game_winner.playoff_semis:
                headlines.append(conference_semis_headlines(game, 3))

    if not season.playoff:
        for game in season.season_schedule[season.week - 1]:
            game_home = game.home_team
            game_away = game.away_team

            teams = [game_home, game_away]

            team_status = ["None", "None"]

            if 3 <= season.week < 6:
                for team_index, team in enumerate(teams):
                    if team.standing <= 8:
                        team_status[team_index] = "contender"
                    else:
                        team_status[team_index] = "middler"

            elif season.week >= 6:
                for team_index, team in enumerate(teams):
                    if team.standing <= 3:
                        team_status[team_index] = "top_team"
                    elif team.standing <= 7:
                        team_status[team_index] = "contender"
                    elif team.standing <= 12:
                        team_status[team_index] = "middler"
                    else:
                        team_status[team_index] = "bottom"

            if game.rivalry:
                print(f"{game_home.city} rivalry with {game_away.city}")
                get_continue()
                headlines.append(rivalry_headlines(game, 0))
            if game.tight_race:
                headlines.append(tight_race_headlines(game, 0))
            if season.week >= 9 and not season.playoff:
                if team_status == ["top_team", "top_team"] or set(team_status) == {"top_team", "contender"}:
                    headlines.append(down_the_stretch_headlines(game, 0))
            if season.week == 14:
                if (not game_home.playoff_eliminated and not game_home.playoff_clinched and not
                game_away.playoff_eliminated and not game_away.playoff_clinched):
                    headlines.append(final_week_headlines(game, 1))

    if season.playoff and season.playoff_week != 0:
        for game in season.playoff_results[season.playoff_week - 2]:
            game_winner = game.home_team if game.winner == "home" else game.away_team
            game_loser = game.home_team if game.winner == "away" else game.away_team

            if season.playoff_week == 2:
                headlines.append(conference_finals_headlines(game, 1))
                headlines.append(conference_finals_headlines(game, 2))
                if game_winner.standing + game_loser.standing < 14:
                    headlines.append(conference_finals_headlines(game, 0))

            if season.playoff_week == 3:
                headlines.append(semifinals_headlines(game, 1))
                headlines.append(semifinals_headlines(game, 2))
                if game_winner.standing + game_loser.standing < 12:
                    headlines.append(semifinals_headlines(game, 0))

            if season.playoff_week == 4:
                headlines.append(finals_headlines(game, 1))
                headlines.append(finals_headlines(game, 2))
                headlines.append(finals_headlines(game, 0))

        for game in season.playoff_schedule[season.playoff_week - 1]:
            if season.playoff_week == 1:
                headlines.append(conference_semis_headlines(game, 4))
            if season.playoff_week == 2:
                headlines.append(conference_finals_headlines(game, 3))
            if season.playoff_week == 3:
                headlines.append(semifinals_headlines(game, 3))
            if season.playoff_week == 4:
                headlines.append(finals_headlines(game, 3))


    return headlines, return_type

def headline_processing(season):
    potential_headlines, return_type = headline_harvest(season)
    weighted_headlines = []
    headlines = []

    if return_type == "none":
        return potential_headlines, "none"
    elif return_type == "team":
        for headline in potential_headlines:
            if headline[1] == 0:
                headline[1] = 101
                headlines.append(headline)
            else:
                weighted_headlines.append(headline)

        remaining = weighted_headlines[:]

        while len(headlines) < 4 and remaining:
            choice = random.choices(
                remaining,
                weights=[h[1] for h in remaining],
                k=1
            )[0]

            repeat = False
            if len(headlines) > 0:
                for headline in headlines:
                    if SequenceMatcher(None, headline[0].lower(), choice[0].lower()).ratio() > 0.75:
                        repeat = True

            if not repeat:
                headlines.append(choice)
                team = choice[2][0]
                remaining = [h for h in remaining if h[2][0] != team]

        return headlines, "team"
    elif return_type == "game":
        for headline in potential_headlines:
            if headline[1] == 0:
                headline[1] = 101
                headlines.append(headline)
            else:
                weighted_headlines.append(headline)

        used_teams = set()

        while len(headlines) < 6:
            eligible = [
                h for h in weighted_headlines
                if h[2].home_team not in used_teams and h[2].away_team not in used_teams
            ]

            if not eligible:
                break

            choice = random.choices(
                eligible,
                weights=[h[1] for h in eligible],
                k=1
            )[0]

            repeat = False
            if len(headlines) > 0:
                for headline in headlines:
                    if SequenceMatcher(None, headline[0].lower(), choice[0].lower()).ratio() > 0.75:
                        repeat = True

            if not repeat:
                headlines.append(choice)
                used_teams.add(choice[2].home_team)
                used_teams.add(choice[2].away_team)

            weighted_headlines.remove(choice)

        return headlines, "game"
    else:
        raise TypeError("Return type not supported")

def update_headlines(season):
    headlines, return_type = headline_processing(season)
    final_headlines = []

    if return_type == "none":
        season.headlines = [headlines]
    elif return_type == "team" or return_type == "game":
        headlines.sort(key=lambda h: h[1], reverse=True)
        for headline in headlines:
            final_headlines.append(headline[0])
        season.headlines = final_headlines
    else:
        raise TypeError("Return type not supported")
