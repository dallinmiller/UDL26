import os
import time
import random
from tabulate import tabulate


# Functions for Usability

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["y", "n"]:
            return answer == "y"
        print("Invalid input. Please enter 'y' or 'n'.")


def get_float(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            try:
                return float(value)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Input cannot be empty. Please enter a valid number.")


def get_continue():
    while True:
        continuing = input("Press enter to continue.")
        if continuing == "":
            break
        else:
            print("Invalid option: Try again.")


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            try:
                return int(value)
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        else:
            print("Input cannot be empty. Please enter a valid number.")


def create_menu(prompt, options_array):
    while True:
        print("\nOption:".ljust(20) + "Select:".rjust(20))
        print()
        selections = []
        for i in range(len(options_array)):
            selections.append(str(i + 1))
        for i in range(len(options_array)):
            print(options_array[i].ljust(20) + selections[i].rjust(20))

        choice = get_int(f"\n{prompt} ")

        clear_screen()

        for i in range(len(options_array)):
            if choice == int(selections[i]):
                return int(selections[i])

        print("Invalid Selection: Try again.")


def get_key(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None


def dialogue(prompt):
    print(prompt)
    time.sleep(2)


# Classes and Setup

def initialize_teams(season):
    alabama = Team(season, "Alabama", "Aardvarks", "AAC", "Front", "ALB")
    alaska = Team(season, "Alaska", "Polars", "AAC", "Front", "ALK")
    arizona = Team(season, "Arizona", "Sand", "AAC", "Front", "ARI")
    arkansas = Team(season, "Arkansas", "Albatross", "AAC", "Front", "ARK")
    colorado = Team(season, "Colorado", "Crest", "CMC", "Front", "COL")
    hawaii = Team(season, "Hawaii", "Melt", "CMC", "Front", "HAW")
    louisiana = Team(season, "Louisiana", "Gumbo", "CMC", "Front", "LOU")
    missouri = Team(season, "Missouri", "Torrent", "CMC", "Front", "MIZ")
    minnesota = Team(season, "Minnesota", "Ice", "MNC", "Back", "MIN")
    nevada = Team(season, "Nevada", "Nights", "MNC", "Back", "NEV")
    new_hampshire = Team(season, "New Hampshire", "North", "MNC", "Back", "NHM")
    new_jersey = Team(season, "New Jersey", "Colonials", "MNC", "Back", "NJR")
    oregon = Team(season, "Oregon", "Outlaws", "OWC", "Back", "ORE")
    rhode_island = Team(season, "Rhode Island", "Gerbils", "OWC", "Back", "RHO")
    utah = Team(season, "Utah", "Salt", "OWC", "Back", "UTA")
    wyoming = Team(season, "Wyoming", "Wind", "OWC", "Back", "WYO")

    teams = [
        alabama, alaska, arizona, arkansas, colorado, hawaii, louisiana, missouri, minnesota, nevada, new_hampshire,
        new_jersey, oregon, rhode_island, utah, wyoming
    ]

    return teams


def initialize_history():
    alabama = TeamHistory("Alabama", "Aardvarks")
    alaska = TeamHistory("Alaska", "Polars")
    arizona = TeamHistory("Arizona", "Sand")
    arkansas = TeamHistory("Arkansas", "Albatross")
    colorado = TeamHistory("Colorado", "Crest")
    hawaii = TeamHistory("Hawaii", "Melt")
    louisiana = TeamHistory("Louisiana", "Gumbo")
    missouri = TeamHistory("Missouri", "Torrent")
    minnesota = TeamHistory("Minnesota", "Ice")
    nevada = TeamHistory("Nevada", "Nights")
    new_hampshire = TeamHistory("New Hampshire", "North")
    new_jersey = TeamHistory("New Jersey", "Colonials")
    oregon = TeamHistory("Oregon", "Outlaws")
    rhode_island = TeamHistory("Rhode Island", "Gerbils")
    utah = TeamHistory("Utah", "Salt")
    wyoming = TeamHistory("Wyoming", "Wind")

    team_history = [
        alabama, alaska, arizona, arkansas, colorado, hawaii, louisiana, missouri, minnesota, nevada, new_hampshire,
        new_jersey, oregon, rhode_island, utah, wyoming
    ]

    return team_history


def initialize_league():
    season = Season()
    teams = initialize_teams(season)
    league = League(teams, season, teams[1])

    return teams, league


class Season:
    def __init__(self):
        self.week = 0
        self.playoff_week = -1
        self.season_number = 1
        self.season_results = []
        self.playoff = False

    def return_week(self):
        return self.week

    def increase_week(self):
        if self.week == 13:
            self.playoff = True
            self.playoff_week += 1
        else:
            self.week += 1

    def increase_playoff_week(self):
        self.playoff_week += 1

    def is_playoffs(self):
        return self.playoff

    def return_playoff_week(self):
        return self.playoff_week

    def reset_season(self):
        self.week = 0
        self.playoff = False

    def return_season_number(self):
        return self.season_number

    def increase_season_number(self):
        self.season_number += 1

    def append_week_results(self, results):
        self.season_results.append(results)


class League:
    def __init__(self, teams, season, user):
        self.league = teams
        self.team_names = teams
        self.user = user
        self.all_results = []
        self.playoffs = False
        self.finished = False
        self.stat_names = ["Team", "W", "L", "P", "PPG", "OP", "OPPG", "PD"]  # Update with game

        self.aac = self.team_names[:4]
        self.cmc = self.team_names[4:8]
        self.mnc = self.team_names[8:12]
        self.owc = self.team_names[12:16]

        self.front = self.aac + self.cmc
        self.back = self.mnc + self.owc

        self.all_teams = self.front + self.back

        self.season = season
        self.schedule = []

        self.playoff_teams = []
        self.p_c_s = []  # Shortened For Readability: Playoff Conference Semis
        self.p_c_s_w = "___", "___", "___", "___"  # Playoff Conference Semis Winners
        self.p_c_f_w = "___", "___", "___", "___"  # Playoff Conference Finals Winners
        self.p_s_w = "___", "___"  # Playoff Semi Winners
        self.p_f_w = "___"

    # Initialization

    def update_user(self, user):
        self.user = user

    def conference_round_robin(self, conference_name):
        if conference_name == "aac":
            conference = self.aac
        elif conference_name == "cmc":
            conference = self.cmc
        elif conference_name == "mnc":
            conference = self.mnc
        else:
            conference = self.owc

        week_1 = [[conference[0], conference[1]], [conference[2], conference[3]]]
        week_2 = [[conference[0], conference[2]], [conference[1], conference[3]]]
        week_3 = [[conference[1], conference[0]], [conference[3], conference[2]]]
        week_4 = [[conference[0], conference[3]], [conference[1], conference[2]]]
        week_5 = [[conference[2], conference[0]], [conference[3], conference[1]]]
        week_6 = [[conference[3], conference[0]], [conference[2], conference[1]]]
        return week_1, week_2, week_3, week_4, week_5, week_6

    def inter_conference_round_robin(self, conference_1_name, conference_2_name):
        if conference_1_name == "aac":
            conference_1 = self.aac
        elif conference_1_name == "cmc":
            conference_1 = self.cmc
        elif conference_1_name == "mnc":
            conference_1 = self.mnc
        else:
            conference_1 = self.owc
        if conference_2_name == "aac":
            conference_2 = self.aac
        elif conference_2_name == "cmc":
            conference_2 = self.cmc
        elif conference_2_name == "mnc":
            conference_2 = self.mnc
        else:
            conference_2 = self.owc
        week_1 = []
        week_2 = []
        week_3 = []
        week_4 = []
        for i in range(4):
            week_1.append([conference_1[i], conference_2[i]])
        for i in range(3):
            week_2.append([conference_2[i + 1], conference_1[i]])
        week_2.append([conference_2[0], conference_1[3]])
        for i in range(2):
            week_3.append([conference_1[i], conference_2[i + 2]])
        for i in range(2):
            week_3.append([conference_1[i + 2], conference_2[i]])
        week_4.append([conference_2[3], conference_1[0]])
        for i in range(3):
            week_4.append([conference_2[i], conference_1[i + 1]])
        return week_1, week_2, week_3, week_4

    def create_schedule(self):
        even = self.season.return_season_number() % 2 == 0
        season = []
        aac_random = self.aac[:]
        cmc_random = self.cmc[:]
        mnc_random = self.mnc[:]
        owc_random = self.owc[:]
        random.shuffle(aac_random)
        random.shuffle(cmc_random)
        random.shuffle(mnc_random)
        random.shuffle(owc_random)

        aac_1, aac_2, aac_3, aac_4, aac_5, aac_6 = self.conference_round_robin("aac")
        cmc_1, cmc_2, cmc_3, cmc_4, cmc_5, cmc_6 = self.conference_round_robin("cmc")
        mnc_1, mnc_2, mnc_3, mnc_4, mnc_5, mnc_6 = self.conference_round_robin("mnc")
        owc_1, owc_2, owc_3, owc_4, owc_5, owc_6 = self.conference_round_robin("owc")

        front_1, front_2, front_3, front_4 = self.inter_conference_round_robin("aac", "cmc")
        back_1, back_2, back_3, back_4 = self.inter_conference_round_robin("mnc", "owc")

        if even:
            ooc1_1, ooc1_2, ooc1_3, ooc1_4 = self.inter_conference_round_robin("aac", "owc")
            ooc2_1, ooc2_2, ooc2_3, ooc2_4 = self.inter_conference_round_robin("cmc", "mnc")
        else:
            ooc1_1, ooc1_2, ooc1_3, ooc1_4 = self.inter_conference_round_robin("aac", "mnc")
            ooc2_1, ooc2_2, ooc2_3, ooc2_4 = self.inter_conference_round_robin("cmc", "owc")

        season.append(aac_1 + cmc_1 + mnc_1 + owc_1)
        season.append(aac_2 + cmc_2 + mnc_2 + owc_2)
        season.append(aac_3 + cmc_3 + mnc_3 + owc_3)
        season.append(aac_4 + cmc_4 + mnc_4 + owc_4)
        season.append(aac_5 + cmc_5 + mnc_5 + owc_5)
        season.append(aac_6 + cmc_6 + mnc_6 + owc_6)
        season.append(front_1 + back_1)
        season.append(front_2 + back_2)
        season.append(front_3 + back_3)
        season.append(front_4 + back_4)
        season.append(ooc1_1 + ooc2_1)
        season.append(ooc1_2 + ooc2_2)
        season.append(ooc1_3 + ooc2_3)
        season.append(ooc1_4 + ooc2_4)

        random.shuffle(season)

        self.schedule = season

    def initialize_playoff_teams(self):
        conferences = [self.aac, self.cmc, self.mnc, self.owc]
        for conference in conferences:
            self.playoff_teams.append([conference[0], conference[1], conference[2]])
            self.p_c_s.append([conference[0], conference[1], conference[2]])

    def create_conference_semis(self):
        conference_matches = []
        for conference in self.playoff_teams:
            conference_matches.append([conference[1], conference[2]])
            conference[0].update_playoffs(0)
            conference[0].update_playoffs(2)
            conference[1].update_playoffs(0)
            conference[1].update_playoffs(1)
            conference[2].update_playoffs(1)
            conference[2].update_playoffs(0)
        return conference_matches

    def create_conference_finals(self, c_f_winners):
        conference_matches = []
        for i in range(len(self.playoff_teams)):
            conference_matches.append([self.playoff_teams[i][0], c_f_winners[i]])

        return conference_matches

    def create_semis(self):
        semi_matches = [[self.playoff_teams[0], self.playoff_teams[3]], [self.playoff_teams[1], self.playoff_teams[2]]]

        return semi_matches

    def create_finals(self):
        print(self.playoff_teams)
        teams = []
        for i in self.playoff_teams:
            teams.append(i)
        self.update_process_finals(teams[0], teams[1])
        final = [self.playoff_teams[0], self.playoff_teams[1]]

        return final

    # Schedule Printing

    def print_schedule(self):
        for week_number, week in enumerate(self.schedule, start=1):
            week_table = []
            for match in week:
                week_table.append(["", match[0].return_city(), "vs", match[1].return_city()])

            headers = [f"Week {week_number}", "Home Team", "", "Away Team"]
            print(tabulate(week_table, headers=headers, tablefmt="grid"))

        print("\n\n")

        get_continue()

    def print_week(self):
        week = get_int("What week would you like to see? ")
        while week < 1 or week > 14:
            week = get_int("Enter a valid week number. ")
            clear_screen()

        week_table = []
        for match in self.schedule[week - 1]:
            week_table.append(["", match[0].return_city(), "vs", match[1].return_city()])

        headers = [f"Week {week}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()

    def find_schedule(self, team):
        team_schedule = []
        for i in range(len(self.schedule)):
            for j in range(len(self.schedule[i])):
                if team in self.schedule[i][j]:
                    team_schedule.append(self.schedule[i][j])
        return team_schedule

    def print_match(self, team):
        week = get_int("What week would you like to see? ")
        while week < 1 or week > 14:
            week = get_int("Enter a valid week number. ")
            clear_screen()

        week_table = []

        for match in self.schedule[week - 1]:
            if match[0] == team or match[1] == team:
                week_table.append(["", match[0].return_city(), "vs", match[1].return_city()])

        headers = [f"Week {week}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

        print("\n\n")

        get_continue()

    def print_team(self, team):
        week_table = []
        team_schedule = self.find_schedule(team)

        for week_number, match in enumerate(team_schedule):
            week_table.append([f"Week {week_number + 1}", match[0].return_city(), "vs", match[1].return_city()])

        headers = ["Week", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

        print("\n\n")

        get_continue()

    def print_results(self):
        for j in range(len(self.all_results)):
            headers = [f"Week {j + 1}", "", "Home Team", "", "Away Team", ""]
            print(tabulate(self.all_results[j], headers=headers, tablefmt="grid"))
            print("\n\n")

        get_continue()

    def schedule_menu(self, users_team):
        while True:
            options = ["Season Schedule", "Week Schedule", "Team Game for Week", "Team Schedule", "Results", "Back"]
            choice = create_menu("Select an Option", options)
            clear_screen()
            if choice == 1:
                self.print_schedule()
            elif choice == 2:
                self.print_week()
            elif choice == 3:
                self.print_match(users_team)
            elif choice == 4:
                self.print_team(users_team)
            elif choice == 5:
                self.print_results()
            elif choice == 6:
                break
            else:
                print("Invalid Response: Retry")
            clear_screen()

    def print_playoffs(self):
        ac1 = f" {self.p_c_s[0][0].code} "
        ac2 = f" {self.p_c_s[0][1].code} "
        ac3 = f" {self.p_c_s[0][2].code} "
        cc1 = f" {self.p_c_s[1][0].code} "
        cc2 = f" {self.p_c_s[1][1].code} "
        cc3 = f" {self.p_c_s[1][2].code} "
        mc1 = f" {self.p_c_s[2][0].code} "
        mc2 = f" {self.p_c_s[2][1].code} "
        mc3 = f" {self.p_c_s[2][2].code} "
        oc1 = f" {self.p_c_s[3][0].code} "
        oc2 = f" {self.p_c_s[3][1].code} "
        oc3 = f" {self.p_c_s[3][2].code} "
        if isinstance(self.p_c_s_w[0], str):
            ac4 = f" {self.p_c_s_w[0]} "
            cc4 = f" {self.p_c_s_w[1]} "
            mc4 = f" {self.p_c_s_w[2]} "
            oc4 = f" {self.p_c_s_w[3]} "
        else:
            ac4 = f" {self.p_c_s_w[0].code} "
            cc4 = f" {self.p_c_s_w[1].code} "
            mc4 = f" {self.p_c_s_w[2].code} "
            oc4 = f" {self.p_c_s_w[3].code} "
        if isinstance(self.p_c_f_w[0], str):
            fi1 = f" {self.p_c_f_w[0]} "
            fi2 = f" {self.p_c_f_w[1]} "
            fi3 = f" {self.p_c_f_w[2]} "
            fi4 = f" {self.p_c_f_w[3]} "
        else:
            fi1 = f" {self.p_c_f_w[0].code} "
            fi2 = f" {self.p_c_f_w[1].code} "
            fi3 = f" {self.p_c_f_w[2].code} "
            fi4 = f" {self.p_c_f_w[3].code} "
        if isinstance(self.p_s_w[0], str):
            fi5 = f" {self.p_s_w[0]} "
            fi6 = f" {self.p_s_w[1]} "
        else:
            fi5 = f" {self.p_s_w[0].code} "
            fi6 = f" {self.p_s_w[1].code} "
        if isinstance(self.p_f_w[0], str):
            win = f" {self.p_f_w[0]} "
        else:
            win = f" {self.p_f_w[0].code} "

        print(f"""
                                                          {win}  
          {ac2}                                   ─────────────────────                                   {mc2}
        |───────|                                        Champion                                       |───────|
            2   | {ac4}           |───────────────|                   |───────────────|           {mc4} |   2
    AAC         |───────|         |     {fi1}     |                   |     {fi2}     |         |───────|        MNC      
          {ac3} |       |         |               |                   |               |         |       | {mc3}    
        |───────|       |───────  |───────────────|                   |───────────────|  ───────|       |───────|
            3     {ac1} |                 1                                   2       |         | {mc1}     3
                |───────|                 |                                   |       |         |───────|
                    1                     |      {fi5}              {fi6}     |       |             1
                                          |────────────────    ───────────────|       | 
                  {cc1}                   |                                   |       |           {oc1}
                |───────|                 |                                   |       |         |───────|
          {cc2}     1   |                 |                                   |       |         |   1     {oc2}
        |───────|       |───────  |───────────────|                   |───────────────|  ───────|       |───────|
            2   | {cc4} |         |     {fi4}     |                   |     {fi3}     |         | {oc4} |   2
    CMC         |───────|         |               |                   |               |         |───────|        OWC
          {cc3} |                 |───────────────|                   |───────────────|                 | {oc3}
        |───────|                         4                                   3                         |───────|
            3                                                                                               3
        
        """
              )

        get_continue()

    def playoff_schedule_menu(self, users_team):
        while True:
            options = ["Season Schedule", "Week Schedule", "Team Game for Week", "Team Schedule", "Results",
                       "Playoff Schedule", "Back"]
            choice = create_menu("Select an Option", options)
            clear_screen()
            if choice == 1:
                self.print_schedule()
            elif choice == 2:
                self.print_week()
            elif choice == 3:
                self.print_match(users_team)
            elif choice == 4:
                self.print_team(users_team)
            elif choice == 5:
                self.print_results()
            elif choice == 6:
                self.print_playoffs()
            elif choice == 7:
                break
            else:
                print("Invalid Response: Retry")
            clear_screen()

    # Admin

    def print_season_status(self):
        print(f"Current Status: {self.user.season_status}")
        print("\n\n")

        get_continue()

    def admin_menu(self):
        while True:
            options = ["Season Status", "Back"]
            choice = create_menu("Select an Option", options)
            clear_screen()
            if choice == 1:
                self.print_season_status()
            elif choice == 2:
                break
            else:
                print("Invalid Response: Retry")
            clear_screen()

    # Standings

    @staticmethod
    def update_process(grouping):
        for group in grouping:
            for j in range(len(group)):
                for i in range(len(group) - 1):
                    if group[i + 1].wins > group[i].wins:
                        group[i], group[i + 1] = group[i + 1], group[i]
                    elif group[i + 1].wins == group[i].wins:
                        if group[i + 1].return_score_differential() > group[i].return_score_differential():
                            group[i], group[i + 1] = group[i + 1], group[i]
                        elif group[i + 1].return_score_differential() == group[i].return_score_differential():
                            if group[i + 1].total_points > group[i].total_points:
                                group[i], group[i + 1] = group[i + 1], group[i]

    @staticmethod
    def update_process_semifinals(group):
        for j in range(len(group)):
            for i in range(len(group) - 1):
                if group[i + 1].wins > group[i].wins:
                    group[i], group[i + 1] = group[i + 1], group[i]
                elif group[i + 1].wins == group[i].wins:
                    if group[i + 1].return_score_differential() > group[i].return_score_differential():
                        group[i], group[i + 1] = group[i + 1], group[i]
                    elif group[i + 1].return_score_differential() == group[i].return_score_differential():
                        if group[i + 1].total_points > group[i].total_points:
                            group[i], group[i + 1] = group[i + 1], group[i]

    def update_process_finals(self, team_0, team_1):
        switch = False
        if team_1.wins > team_0.wins:
            switch = True
        elif team_1.wins == team_0.wins:
            if team_1.return_score_differential() > team_0.return_score_differential():
                switch = True
            elif team_1.return_score_differential() == team_0.return_score_differential():
                if team_1.total_points > team_0.total_points:
                    switch = True

        if switch:
            self.playoff_teams = [team_1, team_0]
        else:
            self.playoff_teams = [team_0, team_1]

    def update_standings(self):
        conferences = [self.aac, self.cmc, self.mnc, self.owc]
        self.update_process(conferences)
        divisions = [self.front, self.back]
        self.update_process(divisions)
        whole_league = [self.all_teams]
        self.update_process(whole_league)

    def get_prestige_info(self, team):
        league_rank = self.all_teams.index(team) + 1

        conferences = [self.aac, self.cmc, self.mnc, self.owc]
        conference_leader = False

        for conference in conferences:
            if team in conference:
                if conference.index(team) == 0:
                    conference_leader = True
                else:
                    conference_leader = False

        ppg_leader = False
        oppg_leader = False
        stats_table = self.master_stats_return_team()
        sorting_index = 3

        for i in range(len(stats_table)):
            for j in range(len(stats_table) - 1):
                if stats_table[j][sorting_index] < stats_table[j + 1][sorting_index]:
                    stats_table[j], stats_table[j + 1] = stats_table[j + 1], stats_table[j]

        if stats_table[0][0] == team:
            ppg_leader = True

        sorting_index = 5
        for i in range(len(stats_table)):
            for j in range(len(stats_table) - 1):
                if stats_table[j][sorting_index] < stats_table[j + 1][sorting_index]:
                    stats_table[j], stats_table[j + 1] = stats_table[j + 1], stats_table[j]

        if stats_table[15][0] == team:
            oppg_leader = True

        return league_rank, conference_leader, ppg_leader, oppg_leader

    def print_standings(self):
        standings_table = []
        all_teams = self.all_teams
        standings_table.append(["", "", "", "", ""])
        for team in all_teams:
            standings_table.append([all_teams.index(team) + 1, f"{team.city_name} {team.team_name}", team.wins,
                                    team.losses, team.return_score_differential()])

        headers = ["League", "Team", "Wins", "Losses", "Score Differential"]
        print(tabulate(standings_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()

    def print_division_standings(self):
        standings_table = []
        divisions = [self.front, self.back]
        division_names = ["Front", "Back"]
        for division in divisions:
            standings_table.append(["", "", "", "", ""])
            standings_table.append([division_names[divisions.index(division)], "", "", "", ""])
            for team in division:
                standings_table.append([division.index(team) + 1, f"{team.city_name} {team.team_name}", team.wins,
                                        team.losses, team.return_score_differential()])

        headers = ["Division", "Team", "Wins", "Losses", "Score Differential"]
        print(tabulate(standings_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()

    def print_conference_standings(self):
        standings_table = []
        conferences = [self.aac, self.cmc, self.mnc, self.owc]
        conference_names = ["AAC", "CMC", "MNC", "OWC"]
        for conference in conferences:
            standings_table.append(["", "", "", "", ""])
            standings_table.append([conference_names[conferences.index(conference)], "", "", "", ""])
            for team in conference:
                standings_table.append([conference.index(team) + 1, f"{team.city_name} {team.team_name}", team.wins,
                                        team.losses, team.return_score_differential()])

        headers = ["Conference", "Team", "Wins", "Losses", "Score Differential"]
        print(tabulate(standings_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()

    def standings_menu(self):
        while True:
            options = ["Full Standings", "Division Standings", "Conference Standings", "Back"]
            choice = create_menu("Select an Option", options)
            clear_screen()
            if choice == 1:
                self.print_standings()
            elif choice == 2:
                self.print_division_standings()
            elif choice == 3:
                self.print_conference_standings()
            elif choice == 4:
                break
            else:
                print("Invalid Response: Retry")
            clear_screen()

    # Statistics

    def find_team(self):
        team_names = []
        for i in self.league:
            team_names.append(f"{i.city_name} {i.team_name}")
        team_number = create_menu("Select a Team", team_names)
        team_choice = self.league[team_number - 1]
        return team_choice

    def single_team_stats(self, team):
        a, b, c, d, e, f, g = team.return_stats()
        stats_table = [[f"{team.city_name} {team.team_name}", a, b, c, d, e, f, g]]

        print(tabulate(stats_table, headers=self.stat_names, tablefmt="grid"))
        print("\n\n")

        get_continue()

    def master_stats_return(self):
        stats_table = []
        for team in self.all_teams:
            a, b, c, d, e, f, g = team.return_stats()
            stats_table.append([f"{team.city_name} {team.team_name}", a, b, c, d, e, f, g])

        return stats_table

    def master_stats_return_team(self):
        stats_table = []
        for team in self.all_teams:
            a, b, c, d, e, f, g = team.return_stats()
            stats_table.append([team, a, b, c, d, e, f, g])

        return stats_table

    def master_stats(self, sorting_index):
        stats_table = self.master_stats_return()

        if sorting_index == 0:
            print(tabulate(stats_table, headers=self.stat_names, tablefmt="grid"))
            print("\n\n")
        else:
            for i in range(len(stats_table)):
                for j in range(len(stats_table) - 1):
                    if stats_table[j][sorting_index] < stats_table[j + 1][sorting_index]:
                        stats_table[j], stats_table[j + 1] = stats_table[j + 1], stats_table[j]

            print(tabulate(stats_table, headers=self.stat_names, tablefmt="grid"))
            print("\n\n")

    def master_stats_menu(self):
        self.master_stats(0)
        while True:
            options = ["Wins", "Losses", "Points", "PPG", "Opponent Points",
                       "Opponent PPG", "Point Differential", "Back"]  # Update with Game
            choice = create_menu("Sort?", options)
            clear_screen()
            if choice < 8:
                self.master_stats(choice)
            elif choice == 8:
                break
            else:
                print("Invalid Response: Retry")

    def stats_menu(self):
        while True:
            options = ["User Stats", "Full Stats", "Single Team Stats", "Back"]
            choice = create_menu("Select an Option", options)
            clear_screen()
            if choice == 1:
                self.single_team_stats(self.user)
            elif choice == 2:
                self.master_stats_menu()
            elif choice == 3:
                chosen_team = self.find_team()
                self.single_team_stats(chosen_team)
            elif choice == 4:
                break
            else:
                print("Invalid Response: Retry")
            clear_screen()

    # Game Continuation

    # Note: Schedule[Week[Match[Team 1, Team 2, Match Prestige, Match Time]]]

    def update_league_prestige(self):
        for team in self.all_teams:
            rank, conference_l, ppg_l, oppg_l = self.get_prestige_info(team)
            team.update_prestige(rank, conference_l, ppg_l, oppg_l)

    def create_times(self, week_schedule, week_number):
        for match in week_schedule:
            match_prestige = match[0].prestige + match[1].prestige
            match_prestige *= random.normalvariate(1, 0.08)
            match.append(match_prestige)

        for i in range(len(week_schedule)):
            for j in range(len(week_schedule) - 1):
                if week_schedule[j][2] < week_schedule[j + 1][2]:
                    week_schedule[j], week_schedule[j + 1] = week_schedule[j + 1], week_schedule[j]

        week_schedule[0].append("6:00")
        week_schedule[1].append("12:00")
        week_schedule[2].append("2:30")
        week_schedule[3].append("1:00")
        week_schedule[4].append("4:00")
        week_schedule[5].append("1:00")
        week_schedule[6].append("4:00")
        week_schedule[7].append("2:30")

        updated_week = [week_schedule[1], week_schedule[3], week_schedule[5], week_schedule[2], week_schedule[7],
                        week_schedule[4], week_schedule[6], week_schedule[0]]
        self.schedule[week_number] = updated_week

    def week_through(self):
        week_score_table = []
        week = self.season.return_week()
        self.create_times(self.schedule[week], week)
        for match in self.schedule[week]:
            if match[0] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 1, False)
                winner, home_score, away_score = game.simulate()
            elif match[1] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 2, False)
                winner, home_score, away_score = game.simulate()
            else:
                game = Game(self.season, match[0], match[1], match[3], False, False, 0, False)
                winner, home_score, away_score = game.simulate()
            if winner == 0:
                week_score_table.append([f"{match[3]}", home_score, f"|{match[0].city_name}|",
                                         "vs", match[1].city_name, away_score])
            else:
                week_score_table.append([f"{match[3]}", home_score, match[0].city_name,
                                         "vs", f"|{match[1].city_name}|", away_score])
            match[0].update_season_status()
            match[1].update_season_status()

        headers = [f"Week {week + 1}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(week_score_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()

        self.season.increase_week()
        self.season.append_week_results(week_score_table)
        self.all_results.append(week_score_table)
        self.update_standings()
        self.update_league_prestige()

        if self.season.is_playoffs():
            self.playoffs = True
            self.initialize_playoff_teams()

    @staticmethod
    def create_times_c(week_schedule):
        for match in week_schedule:
            match_prestige = match[0].prestige + match[1].prestige
            match_prestige *= random.normalvariate(1, 0.08)
            match.append(match_prestige)

        for i in range(len(week_schedule)):
            for j in range(len(week_schedule) - 1):
                if week_schedule[j][2] < week_schedule[j + 1][2]:
                    week_schedule[j], week_schedule[j + 1] = week_schedule[j + 1], week_schedule[j]

        week_schedule[0].append("6:00")
        week_schedule[1].append("12:00")
        week_schedule[2].append("4:00")
        week_schedule[3].append("1:00")

        updated_week = [week_schedule[1], week_schedule[3], week_schedule[2], week_schedule[0]]
        return updated_week

    def playoff_c_semis(self):
        c_s_score_table = []
        winners = []
        week = "Conference Semis"
        matches = self.create_times_c(self.create_conference_semis())
        for match in matches:
            if match[0] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 1, True)
                winner, home_score, away_score = game.simulate()
            elif match[1] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 2, True)
                winner, home_score, away_score = game.simulate()
            else:
                game = Game(self.season, match[0], match[1], match[3], False, False, 0, True)
                winner, home_score, away_score = game.simulate()
            if winner == 0:
                c_s_score_table.append([f"{match[3]}", home_score, f"|{match[0].city_name}|",
                                        "vs", match[1].city_name, away_score])
                winners.append(match[0])
            else:
                c_s_score_table.append([f"{match[3]}", home_score, match[0].city_name,
                                        "vs", f"|{match[1].city_name}|", away_score])
                winners.append(match[1])

        winners_fixed = ["", "", "", ""]
        for winner in winners:
            if winner.conference == "AAC":
                winners_fixed[0] = winner
            if winner.conference == "CMC":
                winners_fixed[1] = winner
            if winner.conference == "MNC":
                winners_fixed[2] = winner
            if winner.conference == "OWC":
                winners_fixed[3] = winner
            winner.update_playoffs(2)

        self.p_c_s_w = winners_fixed

        headers = [f"{week}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(c_s_score_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()
        clear_screen()

        self.print_playoffs()

        clear_screen()

        self.season.increase_playoff_week()
        self.season.append_week_results(c_s_score_table)
        self.all_results.append(c_s_score_table)

    def playoff_c_finals(self):
        c_f_score_table = []
        winners = []
        week = "Conference Finals"
        matches = self.create_times_c(self.create_conference_finals(self.p_c_s_w))
        for match in matches:
            if match[0] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 1, True)
                winner, home_score, away_score = game.simulate()
            elif match[1] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 2, True)
                winner, home_score, away_score = game.simulate()
            else:
                game = Game(self.season, match[0], match[1], match[3], False, False, 0, True)
                winner, home_score, away_score = game.simulate()
            if winner == 0:
                c_f_score_table.append([f"{match[3]}", home_score, f"|{match[0].city_name}|",
                                        "vs", match[1].city_name, away_score])
                winners.append(match[0])
            else:
                c_f_score_table.append([f"{match[3]}", home_score, match[0].city_name,
                                        "vs", f"|{match[1].city_name}|", away_score])
                winners.append(match[1])

        self.p_c_f_w = winners
        self.playoff_teams = winners
        self.update_process_semifinals(self.playoff_teams)
        for winner in winners:
            winner.update_playoffs(3)

        headers = [f"{week}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(c_f_score_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()
        clear_screen()

        self.print_playoffs()

        clear_screen()

        self.season.increase_playoff_week()
        self.season.append_week_results(c_f_score_table)
        self.all_results.append(c_f_score_table)

    @staticmethod
    def create_times_s(week_schedule):
        switch = False

        for match in week_schedule:
            match_prestige = match[0].prestige + match[1].prestige
            match_prestige *= random.normalvariate(1, 0.08)
            match.append(match_prestige)

        for i in range(len(week_schedule)):
            for j in range(len(week_schedule) - 1):
                if week_schedule[j][2] < week_schedule[j + 1][2]:
                    week_schedule[j], week_schedule[j + 1] = week_schedule[j + 1], week_schedule[j]
                    switch = True

        week_schedule[0].append("6:00")
        week_schedule[1].append("3:00")

        updated_week = [week_schedule[1], week_schedule[0]]
        return updated_week, switch

    def playoff_semis(self):
        s_score_table = []
        winners = []
        week = "Semifinals"
        matches, switch = self.create_times_s(self.create_semis())
        for match in matches:
            if match[0] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 1, True)
                winner, home_score, away_score = game.simulate()
            elif match[1] == self.user:
                game = Game(self.season, match[0], match[1], match[3], False, False, 2, True)
                winner, home_score, away_score = game.simulate()
            else:
                game = Game(self.season, match[0], match[1], match[3], False, False, 0, True)
                winner, home_score, away_score = game.simulate()
            if winner == 0:
                s_score_table.append([f"{match[3]}", home_score, f"|{match[0].city_name}|",
                                      "vs", match[1].city_name, away_score])
                winners.append(match[0])
            else:
                s_score_table.append([f"{match[3]}", home_score, match[0].city_name,
                                      "vs", f"|{match[1].city_name}|", away_score])
                winners.append(match[1])

        self.p_s_w = winners
        self.playoff_teams = winners
        for winner in winners:
            winner.update_playoffs(4)

        if not switch:
            self.p_s_w[0], self.p_s_w[1] = self.p_s_w[1], self.p_s_w[0]

        headers = [f"{week}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(s_score_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()
        clear_screen()

        self.print_playoffs()

        clear_screen()

        self.season.increase_playoff_week()
        self.season.append_week_results(s_score_table)
        self.all_results.append(s_score_table)

    def playoff_finals(self):
        f_score_table = []
        winners = []
        week = "Finals"
        match = self.create_finals()
        match.append(0)
        match.append("5:00")
        if match[0] == self.user:
            game = Game(self.season, match[0], match[1], match[3], False, False, 1, True)
            winner, home_score, away_score = game.simulate()
        elif match[1] == self.user:
            game = Game(self.season, match[0], match[1], match[3], False, False, 2, True)
            winner, home_score, away_score = game.simulate()
        else:
            game = Game(self.season, match[0], match[1], match[3], False, False, 0, True)
            winner, home_score, away_score = game.simulate()
        if winner == 0:
            f_score_table.append([f"{match[3]}", home_score, f"|{match[0].city_name}|",
                                  "vs", match[1].city_name, away_score])
            winners.append(match[0])
        else:
            f_score_table.append([f"{match[3]}", home_score, match[0].city_name,
                                  "vs", f"|{match[1].city_name}|", away_score])
            winners.append(match[1])

        self.p_f_w = winners
        self.playoff_teams = winners

        for winner in winners:
            winner.update_playoffs(5)

        headers = [f"{week}", "", "Home Team", "", "Away Team", ""]
        print(tabulate(f_score_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()
        clear_screen()

        self.print_playoffs()

        clear_screen()

        self.season.increase_playoff_week()
        self.season.append_week_results(f_score_table)
        self.all_results.append(f_score_table)

    def playoff_week_through(self):
        if self.season.playoff_week == 0:
            self.playoff_c_semis()
        elif self.season.playoff_week == 1:
            self.playoff_c_finals()
        elif self.season.playoff_week == 2:
            self.playoff_semis()
        elif self.season.playoff_week == 3:
            self.playoff_finals()
            print("Yeah")
        else:
            self.season_reset()

    def next_game(self):
        if not self.playoffs:
            self.week_through()
        else:
            self.playoff_week_through()

    # TODO Archiving and Re-Initializing

    def season_reset(self):
        pass

    def archive_menu(self):
        pass


class History:
    def __init__(self, team_history):
        self.team_histories = team_history
        self.seasons = []

    def add_season(self, new_season):
        self.seasons.append(new_season)


class TeamHistory:
    def __init__(self, city_name, team_name):
        self.city_name = city_name
        self.team_name = team_name
        self.playoffs = 0
        self.conference_semis = 0
        self.conference_finals = 0
        self.semifinals = 0
        self.finals = 0
        self.championships = 0
        self.wins = 0
        self.losses = 0
        self.total_games = 0
        self.total_points = 0
        self.breaks = 0
        self.callahan = 0
        self.total_yards = 0
        self.turnovers = 0
        self.opponent_points = 0
        self.opponent_yards = 0
        self.points_per_game = 0
        self.opponent_points_per_game = 0
        self.differential = 0
        self.team_history = []

    def update_stats(self, team):
        attributes = team.return_attributes
        self.team_history.append(attributes)
        numerical_attributes = [self.wins,
                                self.losses,
                                self.total_games,
                                self.total_points,
                                self.breaks,
                                self.callahan,
                                self.total_yards,
                                self.turnovers,
                                self.opponent_points,
                                self.opponent_yards,
                                self.points_per_game,
                                self.opponent_points_per_game,
                                self.differential
                                ]
    
        for i in range(13):
            numerical_attributes[i] += attributes[i]

        if attributes[13]:
            self.playoffs += 1
        if attributes[14]:
            self.conference_semis += 1
        if attributes[15]:
            self.conference_finals += 1
        if attributes[16]:
            self.semifinals += 1
        if attributes[17]:
            self.finals += 1
        if attributes[18]:
            self.championships += 1


class Team:
    def __init__(self, season, city_name, team_name, conference, division, code, user=False):
        self.user = user
        self.season = season
        self.city_name = city_name
        self.team_name = team_name
        self.code = code
        self.conference = conference
        self.division = division
        self.season_status = "calm"
        self.game_status = "calm"
        self.prestige = 0
        self.wins = 0
        self.losses = 0
        self.total_games = 0
        self.total_points = 0
        self.breaks = 0
        self.callahan = 0
        self.total_yards = 0
        self.turnovers = 0
        self.opponent_points = 0
        self.opponent_yards = 0
        self.points_per_game = 0
        self.opponent_points_per_game = 0
        self.differential = 0
        self.playoffs = False
        self.conference_semis = False
        self.conference_finals = False
        self.semifinals = False
        self.finals = False
        self.champion = False
        self.players = []

    def return_city(self):
        return self.city_name

    def return_status(self):
        return self.season_status

    def return_conference(self):
        return self.conference

    def update_stats(self, win, points, op_points):
        if win:
            self.wins += 1
        else:
            self.losses += 1
        self.total_games += 1
        self.total_points += points
        self.opponent_points += op_points
        self.points_per_game = self.total_points / self.total_games
        self.opponent_points_per_game = self.opponent_points / self.total_games

    def return_stats(self):
        return self.wins, self.losses, self.total_points, self.points_per_game, self.opponent_points, \
            self.opponent_points_per_game, self.differential  # Update as game updates

    def return_win_loss(self):
        win_loss = self.wins - self.losses
        return win_loss

    def return_score_differential(self):
        self.differential = self.total_points - self.opponent_points
        return self.differential

    def select_as_user(self):
        self.user = True

    def deselect_as_user(self):
        self.user = False

    def return_division(self):
        return self.division

    def update_season_status(self):
        win_loss_difference = self.return_win_loss()
        current_week = self.season.return_week()
        if current_week >= 9:
            if win_loss_difference <= -5:
                self.season_status = "Defeated"
            elif win_loss_difference <= -3:
                self.season_status = "Desperate"
            elif win_loss_difference <= 0:
                self.season_status = "Anxious"
            elif win_loss_difference <= 3:
                self.season_status = "Calm"
            else:
                self.season_status = "Confident"
        elif current_week >= 7:
            if win_loss_difference <= -7:
                self.season_status = "Defeated"
            elif win_loss_difference <= -3:
                self.season_status = "Desperate"
            elif win_loss_difference <= 0:
                self.season_status = "Anxious"
            elif win_loss_difference <= 3:
                self.season_status = "Calm"
            else:
                self.season_status = "Confident"
        else:
            if win_loss_difference <= -5:
                self.season_status = "Desperate"
            elif win_loss_difference <= -3:
                self.season_status = "Anxious"
            elif win_loss_difference <= 3:
                self.season_status = "Calm"
            else:
                self.season_status = "Confident"

    def update_prestige(self, rank, d_leader, ppg_leader, oppg_leader):
        #  Main Designator
        if rank <= 8:
            prestige = 4 - (1 / 8) * rank
        else:
            prestige = 3 - (3 / 64) * (rank - 8) ** 2

        if d_leader:
            prestige += 0.5
        if ppg_leader:
            prestige += 0.5
        if oppg_leader:
            prestige += 0.5

        self.prestige = prestige

    def update_playoffs(self, playoff_round):
        # Note: 0 - playoff bound; 1 - csf; 2 - cf; 3 - sf; 4 - f; 5 - champs
        if playoff_round == 0:
            self.playoffs = True
        if playoff_round == 1:
            self.conference_semis = True
        if playoff_round == 2:
            self.conference_finals = True
        if playoff_round == 3:
            self.semifinals = True
        if playoff_round == 4:
            self.finals = True
        if playoff_round == 5:
            self.champion = True
            
    def return_attributes(self):
        attributes = [self.wins,
                      self.losses,
                      self.total_games,
                      self.total_points,
                      self.breaks,  
                      self.callahan,  
                      self.total_yards,  
                      self.turnovers,  
                      self.opponent_points,  
                      self.opponent_yards,  
                      self.points_per_game,  
                      self.opponent_points_per_game,  
                      self.differential,  
                      self.playoffs,  
                      self.conference_semis,  
                      self.conference_finals,  
                      self.semifinals,  
                      self.finals,  
                      self.champion]
        return attributes


class Game:
    def __init__(self, season, team_0, team_1, start_time, rivalry, tight_race, user, playoff):
        self.season = season
        self.start_time = start_time
        self.rivalry = rivalry
        self.tight_race = tight_race
        self.playoff = playoff
        self.team_h = team_0
        self.team_a = team_1
        self.score_u = 0
        self.score_o = 0
        self.possession = 1
        self.time = 10.00
        self.quarter = 1
        self.timeouts_u = 3
        self.timeouts_o = 3
        self.penalties_u = 0
        self.penalties_o = 0
        self.user = user  # 1 user home, 2 user away, 0 no user

    def rating_variation(self):
        teams = [self.team_h, self.team_a]
        variations = []
        for team in teams:
            if team.season_status == "Confident":
                variations.append([2, 0])
            elif team.season_status == "Calm":
                variations.append([0, 0])
            elif team.season_status == "Anxious":
                variations.append([-2, 4])
            elif team.season_status == "Desperate":
                variations.append([-4, 7])
            else:
                variations.append([-5, 2])

        if self.start_time == "6:00":
            for team in variations:
                team[1] += 1

        elif self.start_time == "12:00":
            for team in variations:
                team[1] += 0.5

        return variations

    def simulate_prep(self):
        variation = self.rating_variation()
        home_rating = 15.2 + variation[0][0]
        home_variability = 3 + variation[0][1]
        away_rating = 15 + variation[1][0]
        away_variability = 3 + variation[1][1]

        return home_rating, home_variability, away_rating, away_variability

    def simulate(self):
        h_r, h_v, a_r, a_v = self.simulate_prep()
        home_points = random.normalvariate(h_r, h_v)
        away_points = random.normalvariate(a_r, a_v)
        if home_points > away_points:
            winner = 0
        else:
            winner = 1
        home_points = round(home_points)
        away_points = round(away_points)
        if home_points < 5:
            home_points = 5
        if away_points < 5:
            away_points = 5
        if home_points == away_points:
            if winner == 0:
                home_points += 1
            else:
                away_points += 1

        if not self.playoff:
            self.team_h.update_stats(True if winner == 0 else False, home_points, away_points)
            self.team_a.update_stats(False if winner == 0 else True, away_points, home_points)

        return winner, home_points, away_points  # 0 = Home Win, 1 = Away Win





def initialization(teams):
    team_names = []
    for team in teams:
        team_names.append(f"{team.return_city()} {team.team_name}")
    team_choice = create_menu("Select a Team", team_names)
    teams[team_choice - 1].select_as_user()
    user_choice = teams[team_choice - 1]
    user_name = team_names[team_choice - 1]
    print(user_name)
    return user_choice
def menu(users_team, league):
    while True:
        options = ["Schedule Menu", "Admin Menu", "Standings", "Statistics", "Next Game", "Archive", "Quit"]
        choice = create_menu("Select an Option", options)

        clear_screen()

        if choice == 1:
            if not league.playoffs:
                league.schedule_menu(users_team)
            else:
                league.playoff_schedule_menu(users_team)
        elif choice == 2:
            league.admin_menu()
        elif choice == 3:
            league.standings_menu()
        elif choice == 4:
            league.stats_menu()
        elif choice == 5:
            league.next_game()
        elif choice == 6:
            league.archive_menu()
        elif choice == 7:
            sure = get_yes_no("Sure? (y/n)")
            if sure:
                return "Quit"
        elif league.finished:
            return "New Season"
        else:
            print("Invalid Response: Retry")
        clear_screen()

if __name__ == "__main__":
    team_histories = initialize_history()
    history = History(team_histories)
    ufl_teams, ufl = initialize_league()
    ufl.create_schedule()
    user_team = initialization(ufl_teams)
    user_team_city = user_team.return_city()
    ufl.update_user(user_team)

    while True:
        next_step = menu(user_team, ufl)

        if next_step == "Quit":
            save = get_yes_no("Save? (y/n)")

            if save:
                print("Unable to Save: Not Yet Enabled")
                get_continue()
                break
        else:
            history.add_season(ufl)
            