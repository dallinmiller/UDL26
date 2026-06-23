# League class: Stores information about the league in general, including teams and conferences
class League:
    def __init__(self, teams, conf_names=("aac", "cmc", "mnc", "owc"), div_names=("front", "back")):

        ### Teams Init: Divides league based on conferences and divisions.
        ### Currently only 4 conferences available due to seeding rules.

        self.league = teams
        self.conf_names = conf_names
        self.div_names = div_names
        
        if len(self.league) % len(conf_names) != 0:
            raise ValueError(f"league must be divisible by amount of conferences, {len(conf_names)}")
        if len(self.league) % len(div_names) != 0:
            raise ValueError(f"league must be divisible by amount of divisions, {len(div_names)}")
        
        conf_len = int((len(self.league) / len(conf_names)))
        div_len = int((len(self.league) / len(div_names)))

        self.conferences = {}
        self.divisions = {}

        for i, conf in enumerate(conf_names):
            self.conferences[conf] = self.league[conf_len * i : conf_len * (i + 1)]
        
        for i, div in enumerate(div_names):
            self.divisions[div] = self.league[div_len * i : div_len * (i + 1)]

        self.all_teams = self.league

        ### Playoffs
        self.playoff_teams = {}
        self.conference_final_teams = {}
        self.semifinal_teams = {}
        self.final_teams = []
        self.champion = None

        ### Data, Save, and Reset

        self.user_team = None             # League Tracker for User Team
        self.game_id = 0                  # League Game ID tracker: Resets each season
        self.rivalries = {}               # Rivalry Dict
        self.rivalries_added = 0          # Rivalries added throughout a season
        self.standings_sorted = True      # Boolean stating the status of the sorting of standings

        self.reset_values = {
            "rivalries_added": 0,
            "playoff_teams": {},
            "conference_final_teams": {},
            "semifinal_teams": {},
            "final_teams": [],
            "champion": None
        }

        ### Parameters

        self.rivalry_settings = RivalryParameters()
        self.match_time_settings = MatchTimeParameters(len(self.league))

        self.playoff_cutoff = 3           # How many teams can go on to the playoffs. (3 is current max due to playoff format)

    def return_game_id(self):
        self.game_id += 1
        return self.game_id

class RivalryParameters:
    def __init__(self):
        self.init_score = 40
        self.init_score_div = 55
        self.init_score_conf = 65

        self.score_differential_bonus = [15, 11, 8, 5, 4, 3, 2]
        self.overtime_bonus = 20
        self.rivalry_bonus = 5
        self.tight_race_bonus = 10
        self.playoff_implication_bonus = 10
        self.playoff_bonus = 10
        self.semifinals_bonus = 15
        self.finals_bonus = 25

class MatchTimeParameters:
    def __init__(self, league_len):
        self.prestige_rand = 0.2
        self.conference_leader_bonus = 0.25
        self.ppg_leader_bonus = 0.25
        self.oppg_leader_bonus = 0.25
        self.rivalry_bonus = 0.5
        self.tight_race_bonus = 0.5
        self.playoff_implication_bonus = 0.8

        if league_len == 16:
            self.match_times = ["6:00", "12:00", "2:30", "1:00", "4:00", "1:00", "4:00", "2:30"]
        elif league_len == 20:
            self.match_times = ["6:00", "12:00", "12:00", "2:30", "1:00", "3:00", "4:00", "1:00", "4:00", "2:30"]
        elif league_len == 24:
            self.match_times = ["6:00", "12:00", "12:00", "4:30", "2:30", "1:00", "3:00", "4:00", "1:00", "1:30", "4:00",
                           "2:30"]
        else:
            self.match_times = ["6:00", "6:00", "12:00", "12:00", "1:00", "4:30", "2:30", "1:00", "3:00", "4:00", "1:00",
                           "2:30", "1:30", "4:00", "1:00", "3:00", "4:00", "2:30", "1:30", "4:00"]