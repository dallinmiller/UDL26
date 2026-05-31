# League class: Stores information about the league in general, including teams and conferences
class League:
    def __init__(self, teams):
        self.league = teams
        self.user_team = None
        self.game_id = 0
        
        self.conferences = {
            "aac": self.league[:4],
            "cmc": self.league[4:8],
            "mnc": self.league[8:12],
            "owc": self.league[12:16]
        }
        
        self.divisions = {
            "front": self.conferences["aac"] + self.conferences["cmc"],
            "back": self.conferences["mnc"] + self.conferences["owc"],
        }

        self.all_teams = self.divisions["front"] + self.divisions["back"]

        self.playoff_teams = []
        self.p_c_s = []  # Shortened For Readability: Playoff Conference Semis
        self.p_c_s_w = "___", "___", "___", "___"  # Playoff Conference Semis Winners
        self.p_c_f_w = "___", "___", "___", "___"  # Playoff Conference Finals Winners
        self.p_s_w = "___", "___"  # Playoff Semi Winners
        self.p_f_w = "___"

        self.standings = []

    def return_game_id(self):
        self.game_id += 1
        return self.game_id