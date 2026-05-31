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
