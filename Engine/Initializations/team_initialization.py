from Definitions.team import Team
from History.histories import TeamHistory

# Initializes teams for a specific league.
def initialize_teams():
    alabama = Team("Alabama", "Aardvarks", "aac", "Front")
    alaska = Team("Alaska", "Polars", "aac", "Front")
    arizona = Team("Arizona", "Sand", "aac", "Front")
    arkansas = Team("Arkansas", "Albatross", "aac", "Front")
    colorado = Team("Colorado", "Crest", "cmc", "Front")
    hawaii = Team("Hawaii", "Melt", "cmc", "Front")
    louisiana = Team("Louisiana", "Gumbo", "cmc", "Front")
    missouri = Team("Missouri", "Swamp", "cmc", "Front")
    minnesota = Team("Minnesota", "Ice", "mnc", "Back")
    nevada = Team("Nevada", "Nights", "mnc", "Back")
    new_hampshire = Team("New Hampshire", "North", "mnc", "Back")
    new_jersey = Team("New Jersey", "Colonials", "mnc", "Back")
    oregon = Team("Oregon", "Outlaws", "owc", "Back")
    rhode_island = Team("Rhode Island", "Gerbils", "owc", "Back")
    utah = Team("Utah", "Salt", "owc", "Back")
    wyoming = Team("Wyoming", "Wind", "owc", "Back")

    teams = [
        alabama, alaska, arizona, arkansas, colorado, hawaii, louisiana, missouri, minnesota, nevada, new_hampshire,
        new_jersey, oregon, rhode_island, utah, wyoming
    ]

    for i, team in enumerate(teams, start=0):
        team.league_index = i
        team.team_history = TeamHistory(team.city, team.name, team.league_index)


    return teams