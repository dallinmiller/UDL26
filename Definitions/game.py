# Game class: Stores data about a game
class Game:
    def __init__(self, home_team, away_team, game_id):
        self.home_team = home_team
        self.away_team = away_team
        self.game_id = game_id
        self.prestige = 0
        self.rivalry = False
        self.tight_race = False
        self.playoff_implication = False
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

        self.scoring_settings = ScoringParameters()

class ScoringParameters:
    def __init__(self):
        self.home_base_score = 16
        self.home_base_variation = 3
        self.away_base_score = 15
        self.away_base_variation = 3

        self.min_score = 5

        self.confident_scoring = [2, 0]
        self.calm_scoring = [0, 0]
        self.anxious_scoring = [-2, 4]
        self.desperate_scoring = [-4, 7]
        self.defeated_scoring = [-5, 2]
        self.primetime_variation_bonus = 1
        self.noon_variation_bonus = 0.5