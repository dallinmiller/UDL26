# Season class: Stores specific season information.
class Season:
    def __init__(self):
        self.season_number = 1
        self.week = 1
        self.season_schedule = []
        self.season_results = []
        self.playoff_schedule = []
        self.playoff_results = []
        self.playoff = False
        self.complete = False
        self.playoff_week = 0
