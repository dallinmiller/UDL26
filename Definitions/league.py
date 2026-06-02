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

        self.standings_sorted = True

        self.playoff_teams = {}
        self.conference_final_teams = {}
        self.semifinal_teams = {}
        self.final_teams = []
        self.champion = None

    def return_game_id(self):
        self.game_id += 1
        return self.game_id