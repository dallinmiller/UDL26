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


class Season:
    def __init__(self):
        self.week = 0
        self.playoff_week = -1
        self.season_number = 1
        self.season_results = []
        self.playoff = False

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