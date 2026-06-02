class LeagueHistory:
    def __init__(self, all_teams, playoff_teams, conference_final_teams, semifinal_teams,
                 final_teams, champion):
        self.all_teams = all_teams
        self.playoff_teams = playoff_teams
        self.conference_final_teams = conference_final_teams
        self.semifinal_teams = semifinal_teams
        self.final_teams = final_teams
        self.champion = champion

class SeasonHistory:
    def __init__(self, season_number, season_results, playoff_results):
        self.season_number = season_number
        self.season_results = season_results
        self.playoff_results = playoff_results

class TeamHistory:
    def __init__(self, city, name, league_index):
        self.city = city
        self.name = name
        self.league_index = league_index
        self.prestige = 1
        self.rivalries = []

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

        self.conference_semis_appearances = 0
        self.conference_final_appearances = 0
        self.playoff_semis_appearances = 0
        self.playoff_final_appearances = 0
        self.league_champion = 0

        self.playoff_wins = 0
        self.playoff_losses = 0
        self.playoff_total_points = 0
        self.playoff_scores = 0
        self.playoff_callahan = 0
        self.playoff_total_yards = 0
        self.playoff_turnovers = 0
        self.playoff_opponent_points = 0
        self.playoff_opponent_yards = 0


league_histories = []
season_histories = []
