from Engine.Simulations.simulate_game import simulate

def simulate_week(season):
    for match in season.season_schedule[season.week - 1]:
        simulate(match)

def simulate_week_playoff(season):
    for match in season.playoff_schedule[season.playoff_week - 1]:
        simulate(match)
