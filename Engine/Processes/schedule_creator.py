import random
from Definitions.game import Game

### Schedules for a season are created here based on league criteria.


# Conference schedule is created here. Each team plays each conference opponent twice: Once at home, once away.
def conference_round_robin(conference_key, league):
    teams = league.conferences[conference_key][:]
    random.shuffle(teams)

    n = len(teams)
    weeks = []

    for round_num in range(n - 1):
        week = []

        for i in range(n // 2):
            home = teams[i]
            away = teams[n - 1 - i]

            week.append(Game(home, away, league.return_game_id()))

        weeks.append(week)

        teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    reverse_weeks = []
    for week in weeks:
        reverse_week = []
        for game in week:
            reverse_week.append(
                Game(game.away_team, game.home_team, league.return_game_id())
            )
        reverse_weeks.append(reverse_week)

    return weeks + reverse_weeks


# Non-conference schedule is created here. Each team plays a non-conference opponent once, however every team has an
# equal amount of home and away games.
def inter_conference_round_robin(conference_1_key, conference_2_key, league):
    teams_1 = league.conferences[conference_1_key][:]
    teams_2 = league.conferences[conference_2_key][:]
    
    random.shuffle(teams_1)
    random.shuffle(teams_2)

    n = len(teams_1)

    weeks = [[] for _ in range(n)]

    for week_num in range(n):
        for i in range(n):
            team_1 = teams_1[i]
            team_2 = teams_2[(i + week_num) % n]

            if week_num % 2 == 0:
                weeks[week_num].append(
                    Game(team_1, team_2, league.return_game_id())
                )
            else:
                weeks[week_num].append(
                    Game(team_2, team_1, league.return_game_id())
                )

    return weeks


# The schedule is created here. Conference schedules are created, and then inter-division non-conference schedules are
# created. Each conference plays one non-division conference which alternates each year. The non-division schedules are
# created. The schedule is shuffled randomly by week, and then packaged as a single schedule.
#
# Schedules can be called as follows:
# schedule[Week_num][Game(class)]

def create_schedule(league, season):
    schedule = []
    inter_weeks = None

    even = season.season_number % 2 == 0

    conference_weeks = []

    for conf_key in league.conferences:
        conference_weeks.append(
            conference_round_robin(conf_key, league)
        )

    num_conf_weeks = len(conference_weeks[0])

    for week_index in range(num_conf_weeks):
        week = []
        for conf in conference_weeks:
            week += conf[week_index]
        schedule.append(week)

    pairs_1 = [("aac", "cmc"), ("mnc", "owc")]
    pairs_2 = [("aac", "owc"), ("cmc", "mnc")] if even else [("aac", "mnc"), ("cmc", "owc")]

    for conf_a, conf_b in pairs_1:
        inter_weeks = inter_conference_round_robin(conf_a, conf_b, league)
        for i in range(len(inter_weeks)):
            if len(schedule) <= num_conf_weeks + i:
                schedule.append([])
            schedule[num_conf_weeks + i] += inter_weeks[i]

    base_index = num_conf_weeks + len(inter_weeks)

    for conf_a, conf_b in pairs_2:
        inter_weeks = inter_conference_round_robin(conf_a, conf_b, league)
        for i in range(len(inter_weeks)):
            if len(schedule) <= base_index + i:
                schedule.append([])
            schedule[base_index + i] += inter_weeks[i]

    random.shuffle(schedule)

    return schedule

def conference_division_locater(league, team, conf_or_div="conf"):
    if conf_or_div == "conf":
        if team in league.conferences["aac"]:
            return 0
        elif team in league.conferences["cmc"]:
            return 1
        elif team in league.conferences["mnc"]:
            return 2
        elif team in league.conferences["owc"]:
            return 3
        else:
            raise ValueError(f"Unknown team {team.city}")
    else:
        if team in league.divisions["front"]:
            return 0
        elif team in league.divisions["back"]:
            return 1
        else:
            raise ValueError(f"Unknown team {team.city}")

def create_conference_semis_schedule(league, season):
    conference_semis_schedule = []

    for conference in league.playoff_teams.values():
        conference_semis_schedule.append(
            Game(conference[1], conference[2], league.return_game_id())
        )

    for game in conference_semis_schedule:
        game.playoff = True
        game.home_team.playoff_semis = True
        game.away_team.playoff_semis = True

    season.playoff_schedule.append(conference_semis_schedule)

def create_conference_finals_schedule(league, season):
    conference_finals_schedule = []
    conference_semifinal_winners = []

    for game in season.playoff_schedule[0]:
        if game.winner == "home":
            conference_semifinal_winners.append([game.home_team, conference_division_locater(league, game.home_team)])
        else:
            conference_semifinal_winners.append([game.away_team, conference_division_locater(league, game.home_team)])

    conference_semifinal_winners.sort(key=lambda x: x[1])

    league.conference_final_teams = league.playoff_teams
    league.conference_final_teams["aac"] = [league.playoff_teams["aac"][0], conference_semifinal_winners[0][0]]
    league.conference_final_teams["cmc"] = [league.playoff_teams["cmc"][0], conference_semifinal_winners[1][0]]
    league.conference_final_teams["mnc"] = [league.playoff_teams["mnc"][0], conference_semifinal_winners[2][0]]
    league.conference_final_teams["owc"] = [league.playoff_teams["owc"][0], conference_semifinal_winners[3][0]]
    
    for conference in league.conference_final_teams.values():
        conference_finals_schedule.append(
            Game(conference[0], conference[1], league.return_game_id())
        )
    
    for game in conference_finals_schedule:
        game.playoff = True
        
    season.playoff_schedule.append(conference_finals_schedule)
    
def create_semifinals_schedule(league, season):
    semifinals_schedule = []
    conference_final_winners = []

    for game in season.playoff_schedule[1]:
        if game.winner == "home":
            conference_final_winners.append([game.home_team, conference_division_locater(league, game.home_team)])
        else:
            conference_final_winners.append([game.away_team, conference_division_locater(league, game.home_team)])

    conference_final_winners.sort(key=lambda x: x[1])
            
    league.semifinal_teams = {
        "front": [conference_final_winners[0][0], conference_final_winners[1][0]],
        "back": [conference_final_winners[2][0], conference_final_winners[3][0]]
    }
    
    for division in league.semifinal_teams.values():
        if division[0].wins == division[1].wins:
            if (division[0].total_points - division[0].opponent_points) > (division[1].total_points - division[1].opponent_points):
                semifinals_schedule.append(
                    Game(division[0], division[1], league.return_game_id())
                )
            else:
                semifinals_schedule.append(
                    Game(division[1], division[0], league.return_game_id())
                )
        elif division[0].wins > division[1].wins:
            semifinals_schedule.append(
                Game(division[0], division[1], league.return_game_id())
            )
        else:
            semifinals_schedule.append(
                Game(division[1], division[0], league.return_game_id())
            )

    for game in semifinals_schedule:
        game.playoff = True

    season.playoff_schedule.append(semifinals_schedule)
    
def create_finals_schedule(league, season):
    final_game = []
    conference_finals_winners = []
    
    for game in season.playoff_schedule[2]:
        if game.winner == "home":
            conference_finals_winners.append(game.home_team)
        else:
            conference_finals_winners.append(game.away_team)

    league.final_teams = conference_finals_winners

    if league.final_teams[0].wins == league.final_teams[1].wins:
        if (league.final_teams[0].total_points - league.final_teams[0].opponent_points) > (
                league.final_teams[1].total_points - league.final_teams[1].opponent_points):
            final_game.append(
                Game(league.final_teams[0], league.final_teams[1], league.return_game_id())
            )
        else:
            final_game.append(
                Game(league.final_teams[1], league.final_teams[0], league.return_game_id())
            )
    elif league.final_teams[0].wins > league.final_teams[1].wins:
        final_game.append(
            Game(league.final_teams[0], league.final_teams[1], league.return_game_id())
        )
    else:
        final_game.append(
            Game(league.final_teams[1], league.final_teams[0], league.return_game_id())
        )

    potential_times = ["4:00", "5:00", "6:00", "7:00"]

    final_game[0].match_time = random.choice(potential_times)

    season.playoff_schedule.append(final_game)

def crown_champion(league, season):
    if season.playoff_schedule[3][0].winner == "home":
        league.champion = season.playoff_schedule[3][0].home_team
    else:
        league.champion = season.playoff_schedule[3][0].away_team
