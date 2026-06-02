from Definitions.team import Team
from History.histories import TeamHistory

# Initializes teams for a specific league.
def initialize_teams():
    alabama = Team("Alabama", "Aardvarks", "AAC", "Front")
    alaska = Team("Alaska", "Polars", "AAC", "Front")
    arizona = Team("Arizona", "Sand", "AAC", "Front")
    arkansas = Team("Arkansas", "Albatross", "AAC", "Front")
    colorado = Team("Colorado", "Crest", "CMC", "Front")
    hawaii = Team("Hawaii", "Melt", "CMC", "Front")
    louisiana = Team("Louisiana", "Gumbo", "CMC", "Front")
    missouri = Team("Missouri", "Swamp", "CMC", "Front")
    minnesota = Team("Minnesota", "Ice", "MNC", "Back")
    nevada = Team("Nevada", "Nights", "MNC", "Back")
    new_hampshire = Team("New Hampshire", "North", "MNC", "Back")
    new_jersey = Team("New Jersey", "Colonials", "MNC", "Back")
    oregon = Team("Oregon", "Outlaws", "OWC", "Back")
    rhode_island = Team("Rhode Island", "Gerbils", "OWC", "Back")
    utah = Team("Utah", "Salt", "OWC", "Back")
    wyoming = Team("Wyoming", "Wind", "OWC", "Back")

    teams = [
        alabama, alaska, arizona, arkansas, colorado, hawaii, louisiana, missouri, minnesota, nevada, new_hampshire,
        new_jersey, oregon, rhode_island, utah, wyoming
    ]

    for i, team in enumerate(teams, start=0):
        team.league_index = i
        team.team_history = TeamHistory(team.city, team.name, team.league_index)


    return teams