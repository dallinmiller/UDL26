# Game class: Stores data about a game
class Game:
    def __init__(self, home_team, away_team, game_id):
        self.home_team = home_team
        self.away_team = away_team
        self.game_id = game_id
        self.prestige = 0
        self.rivalry = False
        self.tight_race = False
        self.playoff = False
        self.match_time = "Time not set"
        self.score_home = 0
        self.score_away = 0
        self.possession = "None"
        self.time = 0
        self.quarter = 0
        self.timeouts_u = 3
        self.timeouts_o = 3
        self.penalties_u = 0
        self.penalties_o = 0
        self.overtime = False
        self.played = "False"
        self.winner = "None"
