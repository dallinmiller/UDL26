from Engine.Simulations.simulate_game import simulate

def simulate_week(season):
    for match in season.season_schedule[season.week - 1]:
        simulate(match)
