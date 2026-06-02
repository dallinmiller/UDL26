from Engine.Initializations.initialize import initialization
from Engine.game_controller import game_control

if __name__ == "__main__":
    league, season = initialization()
    game_control(league, season)
