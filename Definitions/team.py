# Team class: Stores players and team information
class Team:
    def __init__(self, city_name, team_name, conference, division, user=False):
        self.user = user
        self.city = city_name
        self.name = team_name
        self.conference = conference
        self.division = division
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
        self.players = []

    def update_win_loss(self):
        self.win_loss = self.wins - self.losses

    def return_score_differential(self):
        return self.total_points - self.opponent_points

    def update_stats(self, win, points, op_points):
        if win:
            self.wins += 1
        else:
            self.losses += 1
        self.total_points += points
        self.opponent_points += op_points

    def return_stats(self):
        total_games = self.wins + self.losses
        return (self.wins, self.losses, self.total_points, (self.total_points/total_games if total_games > 0 else 0),
                self.opponent_points, (self.opponent_points/total_games if total_games > 0 else 0),
                self.total_points - self.opponent_points)
