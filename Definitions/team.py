# Team class: Stores players and team information
class Team:
    def __init__(self, city_name, team_name, conference, division, user=False):
        self.team_history = None
        self.user = user
        self.city = city_name
        self.name = team_name
        self.conference = conference
        self.division = division
        self.league_index = 0
        self.prestige = 1
        self.season_status = "calm"
        self.game_status = "calm"
        self.wins = 0
        self.losses = 0
        self.win_loss = 0
        self.total_points = 0
        self.scores = 0
        self.callahan = 0
        self.total_yards = 0
        self.turnovers = 0
        self.opponent_points = 0
        self.opponent_yards = 0

        self.playoff_semis = False
        self.playoff_wins = 0
        self.playoff_losses = 0
        self.playoff_total_points = 0
        self.playoff_scores = 0
        self.playoff_callahan = 0
        self.playoff_total_yards = 0
        self.playoff_turnovers = 0
        self.playoff_opponent_points = 0
        self.playoff_opponent_yards = 0

        self.players = []

    def update_win_loss(self):
        self.win_loss = self.wins - self.losses

    def return_score_differential(self):
        return self.total_points - self.opponent_points

    def return_stats(self):
        total_games = self.wins + self.losses
        return (self.wins, self.losses, self.total_points, (self.total_points/total_games if total_games > 0 else 0),
                self.opponent_points, (self.opponent_points/total_games if total_games > 0 else 0),
                self.total_points - self.opponent_points)

    def return_playoff_stats(self):
        total_games = self.playoff_wins + self.playoff_losses
        return (self.playoff_wins, self.playoff_losses, self.playoff_total_points,
                (self.playoff_total_points/total_games if total_games > 0 else 0),
                self.playoff_opponent_points, (self.playoff_opponent_points/total_games if total_games > 0 else 0),
                self.playoff_total_points - self.playoff_opponent_points)
