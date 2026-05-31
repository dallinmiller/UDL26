from Engine.Initializations.initialize import initialization
from Engine.game_controller import game_control

season, league = initialization()
game_control(league, season)
