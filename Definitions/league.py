# League class: Stores information about the league in general, including teams and conferences
class League:
    def __init__(self, teams):
        self.league = teams
        self.user_team = None
        self.game_id = 0
        self.playoff_cutoff = 3
        
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

        self.rivalries = {}
        self.rivalries_added = 0

        self.standings_sorted = True

        self.playoff_teams = {}
        self.conference_final_teams = {}
        self.semifinal_teams = {}
        self.final_teams = []
        self.champion = None

        self.reset_values = {
            "rivalries_added": 0,
            "playoff_teams": {},
            "conference_final_teams": {},
            "semifinal_teams": {},
            "final_teams": [],
            "champion": None
        }

    def return_game_id(self):
        self.game_id += 1
        return self.game_id