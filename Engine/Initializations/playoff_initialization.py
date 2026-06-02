from Engine.Processes.schedule_creator import create_conference_semis_schedule
from Engine.Updates.time_update import create_times_conference_playoffs

def playoff_initialization(league, season):
    league.playoff_teams = {
        conference_name: conference[:3]
        for conference_name, conference in league.conferences.items()
    }

    create_conference_semis_schedule(league, season)
    create_times_conference_playoffs(season)

    season.playoff_week = 1

    return "playoff"
