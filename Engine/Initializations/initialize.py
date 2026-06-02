from Definitions.league import League
from Definitions.season import Season
from Engine.Initializations.team_initialization import initialize_teams
from Engine.Initializations.user_initialization import initialize_user
from Engine.Processes.schedule_creator import create_schedule
from Engine.Updates.time_update import create_times

# Initializes simulator by starting a season, league, assigns user, and creates the first schedule.
def initialization():
    season = Season()
    league = League(initialize_teams())
    initialize_user(league)
    season.season_schedule = create_schedule(league, season)
    create_times(season)
    return league, season
