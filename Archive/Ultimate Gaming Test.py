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
    time.sleep(3)


# Classes and Setup

def initialize_teams(season):
    alabama = Team(season, "Alabama", "Aardvarks", "AAC", "Front")
    alaska = Team(season, "Alaska", "Polars", "AAC", "Front")
    arizona = Team(season, "Arizona", "Sand", "AAC", "Front")
    arkansas = Team(season, "Arkansas", "Albatross", "AAC", "Front")
    colorado = Team(season, "Colorado", "Crest", "CMC", "Front")
    hawaii = Team(season, "Hawaii", "Melt", "CMC", "Front")
    louisiana = Team(season, "Louisiana", "Gumbo", "CMC", "Front")
    missouri = Team(season, "Missouri", "Swamp", "CMC", "Front")
    minnesota = Team(season, "Minnesota", "Ice", "MNC", "Back")
    nevada = Team(season, "Nevada", "Nights", "MNC", "Back")
    new_hampshire = Team(season, "Mew Hampshire", "North", "MNC", "Back")
    new_jersey = Team(season, "New Jersey", "Colonials", "MNC", "Back")
    oregon = Team(season, "Oregon", "Outlaws", "OWC", "Back")
    rhode_island = Team(season, "Rhode Island", "Gerbils", "OWC", "Back")
    utah = Team(season, "Utah", "Salt", "OWC", "Back")
    wyoming = Team(season, "Wyoming", "Wind", "OWC", "Back")

    teams = [
        alabama, alaska, arizona, arkansas, colorado, hawaii, louisiana, missouri, minnesota, nevada, new_hampshire,
        new_jersey, oregon, rhode_island, utah, wyoming
    ]

    return teams


def initialize_league():
    season = Season()
    teams = initialize_teams(season)
    league = League(teams, season)

    return teams, league


def initialize_game():
    pass


class Season:
    def __init__(self):
        self.week = 0
        self.season_number = 1

    def return_week(self):
        return self.week

    def increase_week(self):
        self.week += 1

    def reset_week(self):
        self.week = 0

    def return_season_number(self):
        return self.season_number

    def increase_season_number(self):
        self.season_number += 1


class League:
    def __init__(self, teams, season):
        self.league = teams
        self.team_names = [team.return_city() for team in self.league]

        self.aac = self.team_names[:4]
        self.cmc = self.team_names[4:8]
        self.mnc = self.team_names[8:12]
        self.owc = self.team_names[12:16]

        self.front = [self.aac + self.cmc]
        self.back = [self.mnc + self.owc]

        self.season = season
        self.schedule = []

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
        even = self.season.return_season_number() // 2 == 0
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

    def print_schedule(self):
        for week_number, week in enumerate(self.schedule, start=1):
            week_table = []
            for match in week:
                week_table.append(["", match[0], "vs", match[1]])

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
            week_table.append(["", match[0], "vs", match[1]])

        headers = [f"Week {week}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))
        print("\n\n")

        get_continue()

    def find_schedule(self, team_name):
        team_schedule = []
        for i in range(len(self.schedule)):
            for j in range(len(self.schedule[i])):
                if team_name in self.schedule[i][j]:
                    team_schedule.append(self.schedule[i][j])
        return team_schedule

    def print_match(self, team_name):
        week = get_int("What week would you like to see? ")
        while week < 1 or week > 14:
            week = get_int("Enter a valid week number. ")
            clear_screen()

        week_table = []

        for match in self.schedule[week - 1]:
            if match[0] == team_name or match[1] == team_name:
                week_table.append(["", match[0], "vs", match[1]])

        headers = [f"Week {week}", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

        print("\n\n")

        get_continue()

    def print_team(self, team_name):
        week_table = []
        team_schedule = self.find_schedule(team_name)

        for week_number, match in enumerate(team_schedule):
            week_table.append([f"Week {week_number + 1}", match[0], "vs", match[1]])

        headers = ["Week", "Home Team", "", "Away Team"]
        print(tabulate(week_table, headers=headers, tablefmt="grid"))

        print("\n\n")

        get_continue()


class Team:
    def __init__(self, season, city_name, team_name, conference, division, user=False):
        self.user = user
        self.season = season
        self.city_name = city_name
        self.team_name = team_name
        self.conference = conference
        self.division = division
        self.season_status = "calm"
        self.game_status = "calm"
        self.wins = 0
        self.losses = 0
        self.total_points = 0
        self.scores = 0
        self.callahan = 0
        self.total_yards = 0
        self.turnovers = 0
        self.opponent_points = 0
        self.opponent_yards = 0
        self.players = []

    def return_city(self):
        return self.city_name

    def return_status(self):
        return self.season_status

    def return_conference(self):
        return self.conference

    def return_win_loss(self):
        win_loss = self.wins - self.losses
        return win_loss

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
                self.season_status = "defeated"
            elif win_loss_difference <= -3:
                self.season_status = "desperate"
            elif win_loss_difference <= 0:
                self.season_status = "anxious"
            elif win_loss_difference <= 3:
                self.season_status = "calm"
            else:
                self.season_status = "confident"
        elif current_week >= 7:
            if win_loss_difference <= -7:
                self.season_status = "defeated"
            elif win_loss_difference <= -3:
                self.season_status = "desperate"
            elif win_loss_difference <= 0:
                self.season_status = "anxious"
            elif win_loss_difference <= 3:
                self.season_status = "calm"
            else:
                self.season_status = "confident"
        else:
            if win_loss_difference <= -5:
                self.season_status = "desperate"
            elif win_loss_difference <= -3:
                self.season_status = "anxious"
            elif win_loss_difference <= 3:
                self.season_status = "calm"
            else:
                self.season_status = "confident"


class UserGame:
    def __init__(self, season, user, team_2, home, match_time, rivalry, tight_race):
        self.season = season
        self.match_time = match_time
        self.rivalry = rivalry
        self.tight_race = tight_race
        self.user = user
        self.opponent = team_2
        self.home = home
        self.user_name = self.user.return_city()
        self.opponent_name = self.opponent.return_city()
        self.score_u = 0
        self.score_o = 0
        self.possession = 1
        self.time = 10.00
        self.quarter = 1
        self.timeouts_u = 3
        self.timeouts_o = 3
        self.penalties_u = 0
        self.penalties_o = 0

    def game_intro(self):
        potential_prompts = []
        if self.season.return_week() == 1:
            dialogue("Welcome to a new season of this year's UFL!")
        elif self.season.return_week() == 14:
            dialogue("Well folks, we have made it to the last game of the season.")
        else:
            potential_prompts = [
                f"It is {self.match_time} and time for a great game of the UFL"
            ]

        if self.match_time == "6:30":
            potential_prompts.append("What a wonderful night for some UFL action!")
        if self.match_time in ["12:00", "1:30", "3:00", "4:30"]:
            potential_prompts.append("Good afternoon everyone, and welcome to the UFL!")

        dialogue(random.choice(potential_prompts))

        potential_prompts = [
            f"It's game-time here in {self.user_name if self.home else self.opponent_name}"
        ]

        if self.rivalry:
            potential_prompts.extend([
                "We are excited for what should be another statement game of this rivalry."
            ])
        if self.tight_race:
            potential_prompts.extend([
                "Two teams at the top of their divisions trying to make the final leap into the playoffs.",
                ""
            ])

    def coin_flip(self):
        dialogue("Kickoff is around the corner...")
        if not self.home:
            while True:
                coin_choice = input("Choose heads or tails. (h/t) ").strip().lower()
                if coin_choice in ["h", "t"]:
                    break
                print("Invalid input. Please enter 'y' or 'n'.")
        else:
            dialogue(f"{self.opponent_name} is the away team, and selects heads or tails.")
            coin_choice = random.randint(0, 1)
            dialogue(f"{self.opponent_name} selects {'heads' if coin_choice == 0 else 'tails'}")
            if coin_choice == 0:
                coin_choice = "h"
            else:
                coin_choice = "t"
        coin = random.randint(0, 1)
        if coin == 0:
            coin = "h"
        else:
            coin = "t"
        if coin == coin_choice and not self.home or coin != coin_choice and self.home:
            self.possession = 1
            dialogue("You won the kickoff!")
        else:
            self.possession = 2
            dialogue("You lost the kickoff.")
        time.sleep(3.5)


def schedule_menu(user_name, league):
    while True:
        options = ["Season Schedule", "Week Schedule", "Team Game for Week", "Team Schedule", "Quit"]
        choice = create_menu("Select an Option", options)
        clear_screen()
        if choice == 1:
            league.print_schedule()
        elif choice == 2:
            league.print_week()
        elif choice == 3:
            league.print_match(user_name)
        elif choice == 4:
            league.print_team(user_name)
        elif choice == 5:
            break
        else:
            print("Invalid Response: Retry")
        clear_screen()


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


if __name__ == "__main__":
    season_1 = Season()
    ufl_teams, ufl = initialize_league()
    ufl.create_schedule()
    user_team = initialization(ufl_teams)
    user_team_city = user_team.return_city()

    schedule_menu(user_team_city, ufl)
