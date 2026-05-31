# Game class: Stores data about a game
class Game:
    def __init__(self, home_team, away_team, game_id):
        self.home_team = home_team
        self.away_team = away_team
        self.game_id = game_id
        self.rivalry = False
        self.tight_race = False
        self.match_time = 0
        self.score_u = 0
        self.score_o = 0
        self.possession = 0
        self.time = 0
        self.quarter = 0
        self.timeouts_u = 0
        self.timeouts_o = 0
        self.penalties_u = 0
        self.penalties_o = 0