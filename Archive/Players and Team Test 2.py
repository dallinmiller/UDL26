import os
import time
import random
from tabulate import tabulate
import numpy as np
from faker import Faker
fake = Faker()


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


class Player:
    def __init__(self):
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.position = ""
        self.overall = 0
        self.xp = 0
        self.level = 0
        self.age = 0
        self.condition = 100
        self.longevity = 0
        self.potential = 0
        self.general_stamina = 0
        self.throw_power = 0
        self.throw_accuracy = 0
        self.throw_stamina = 0
        self.curve_accuracy = 0
        self.disc_security = 0
        self.agility = 0
        self.speed = 0
        self.speed_stamina = 0
        self.catching = 0
        self.layout = 0
        self.marking = 0
        self.ground_defense = 0
        self.air_defense = 0
        self.great_attributes = []
        self.good_attributes = []
        self.bad_attributes = []
        self.terrible_attributes = []
        self.unchanging_attributes = []
        self.great_attributes_init = []
        self.good_attributes_init = []
        self.bad_attributes_init = []
        self.terrible_attributes_init = []

    def initialize_player(self):
        self.first_name = fake.first_name_male()
        self.last_name = fake.last_name()
        self.name = f"{self.first_name} {self.last_name}"
        position_list = ["AH", "PH", "RH", "SH", "DH", "HY", "IC", "CC", "HC", "DC", "AC"]
        self.position = random.choice(position_list)
        self.age = random.randint(19, 23)
        self.initialize_attributes()

    def initialize_attributes(self):
        if self.position == "AH":
            self.great_attributes_init = [
                "longevity", "throw_power", "general_stamina", "throw_stamina"
            ]
            self.good_attributes_init = [
                "curve_accuracy", "throw_accuracy", "disc_security", "marking", "potential"
            ]
            self.bad_attributes_init = [
                "catching", "speed_stamina", "speed", "agility"
            ]
            self.terrible_attributes_init = [
                "layout", "ground_defense", "air_defense"
            ]

        elif self.position == "PH":
            self.great_attributes_init = [
                "throw_power", "throw_stamina", "throw_accuracy", "curve_accuracy"
            ]
            self.good_attributes_init = [
                "disc_security", "potential", "marking", "general_stamina", "longevity"
            ]
            self.bad_attributes_init = [
                "catching", "speed", "layout", "agility"
            ]
            self.terrible_attributes_init = [
                "ground_defense", "speed_stamina", "air_defense"
            ]

        elif self.position == "RH":
            self.great_attributes_init = [
                "throw_accuracy", "curve_accuracy", "catching", "agility"
            ]
            self.good_attributes_init = [
                "disc_security", "longevity", "marking", "throw_stamina", "speed"
            ]
            self.bad_attributes_init = [
                "layout", "potential", "throw_power", "general_stamina"
            ]
            self.terrible_attributes_init = [
                "ground_defense", "speed_stamina", "air_defense"
            ]

        elif self.position == "SH":
            self.great_attributes_init = [
                "throw_power", "throw_accuracy", "speed", "layout"
            ]
            self.good_attributes_init = [
                "disc_security", "general_stamina", "curve_accuracy", "catching", "agility"
            ]
            self.bad_attributes_init = [
                "throw_stamina", "potential", "speed_stamina", "longevity"
            ]
            self.terrible_attributes_init = [
                "ground_defense", "air_defense", "marking"
            ]

        elif self.position == "DH":
            self.great_attributes_init = [
                "marking", "agility", "throw_accuracy", "speed"
            ]
            self.good_attributes_init = [
                "curve_accuracy", "disc_security", "ground_defense", "layout", "speed_stamina"
            ]
            self.bad_attributes_init = [
                "throw_power", "throw_stamina", "potential", "air_defense"
            ]
            self.terrible_attributes_init = [
                "catching", "general_stamina", "longevity"
            ]

        elif self.position == "HY":
            self.great_attributes_init = [
                "catching", "agility", "layout", "throw_accuracy"
            ]
            self.good_attributes_init = [
                "potential", "throw_power", "throw_stamina", "speed", "curve_accuracy"
            ]
            self.bad_attributes_init = [
                "marking", "longevity", "ground_defense", "air_defense"
            ]
            self.terrible_attributes_init = [
                "disc_security", "speed_stamina", "general_stamina"
            ]

        elif self.position == "IC":
            self.great_attributes_init = [
                "catching", "agility", "layout", "throw_stamina"
            ]
            self.good_attributes_init = [
                "speed_stamina", "general_stamina", "speed", "throw_accuracy", "air_defense"
            ]
            self.bad_attributes_init = [
                "marking", "longevity", "throw_power", "potential"
            ]
            self.terrible_attributes_init = [
                "ground_defense", "disc_security", "curve_accuracy"
            ]

        elif self.position == "CC":
            self.great_attributes_init = [
                "speed_stamina", "catching", "throw_stamina", "air_defense"
            ]
            self.good_attributes_init = [
                "ground_defense", "agility", "layout", "speed", "throw_accuracy"
            ]
            self.bad_attributes_init = [
                "marking", "longevity", "potential", "general_stamina"
            ]
            self.terrible_attributes_init = [
                "throw_power", "disc_security", "curve_accuracy"
            ]

        elif self.position == "HC":
            self.great_attributes_init = [
                "catching", "agility", "layout", "speed"
            ]
            self.good_attributes_init = [
                "speed_stamina", "general_stamina", "air_defense", "throw_stamina", "potential"
            ]
            self.bad_attributes_init = [
                "ground_defense", "marking", "longevity", "throw_power"
            ]
            self.terrible_attributes_init = [
                "throw_accuracy", "disc_security", "curve_accuracy"
            ]

        elif self.position == "DC":
            self.great_attributes_init = [
                "catching", "agility", "layout", "air_defense"
            ]
            self.good_attributes_init = [
                 "marking", "ground_defense", "speed_stamina", "general_stamina", "speed"
            ]
            self.bad_attributes_init = [
                "longevity", "throw_stamina", "potential", "throw_accuracy"
            ]
            self.terrible_attributes_init = [
               "disc_security", "throw_power", "curve_accuracy"
            ]

        elif self.position == "AC":
            self.great_attributes_init = [
                "general_stamina", "speed", "agility", "layout"
            ]
            self.good_attributes_init = [
                "catching", "speed_stamina", "throw_accuracy", "air_defense", "throw_stamina"
            ]
            self.bad_attributes_init = [
                "ground_defense", "longevity", "throw_power", "potential"
            ]
            self.terrible_attributes_init = [
                "marking", "disc_security", "curve_accuracy"
            ]

        for attribute in self.great_attributes_init:
            value = np.random.normal(75, 8)
            if attribute == "potential" or attribute == "longevity":
                value = np.random.normal(75, 12)
            if value > 100:
                value = 99
            elif value < 0:
                value = 0
            setattr(self, attribute, value)
        for attribute in self.good_attributes_init:
            value = np.random.normal(70, 5)
            if attribute == "potential" or attribute == "longevity":
                value = np.random.normal(65, 15)
            if value > 100:
                value = 99
            elif value < 0:
                value = 0
            setattr(self, attribute, value)
        for attribute in self.bad_attributes_init:
            value = np.random.normal(65, 4)
            if value > 100:
                value = 99
            elif value < 0:
                value = 0
            setattr(self, attribute, value)
        for attribute in self.terrible_attributes_init:
            value = np.random.normal(50, 12)
            if value > 100:
                value = 99
            elif value < 0:
                value = 0
            setattr(self, attribute, value)

            self.great_attributes = self.great_attributes_init
            self.good_attributes = self.good_attributes_init
            self.bad_attributes = self.bad_attributes_init
            self.terrible_attributes = self.terrible_attributes_init

        attribute_lists = [self.great_attributes, self.good_attributes, self.bad_attributes,
                           self.terrible_attributes
                           ]

        for lists in attribute_lists:
            if "longevity" in lists:
                lists.remove("longevity")
            if "potential" in lists:
                lists.remove("potential")

        self.update_overall()

    def update_attributes(self):
        if self.xp >= 1000:
            self.xp -= 1000
            self.level += 1
            possible_potential = (0.25 * (self.longevity ** ((5 + self.level) / self.level))) - (self.longevity / 20)

            if possible_potential > 40 + .06 * self.level:
                if self.potential < 40:
                    bonus = (np.random.normal(1.0, 0.5) * 0.0001) + 1
                elif self.potential < 60:
                    bonus = (np.random.normal(2.3, 0.6) * 0.0001) + 1
                elif self.potential < 80:
                    bonus = (np.random.normal(3.5, 0.7) * 0.0001) + 1
                elif self.potential < 90:
                    bonus = (np.random.normal(5.2, 0.8) * 0.0001) + 1
                else:
                    bonus = (np.random.normal(6.5, 1) * 0.0001) + 1
            elif possible_potential > 25 + .06 * self.level:
                if self.potential < 40:
                    bonus = (np.random.normal(0.5, 0.3) * 0.0001) + 1
                elif self.potential < 60:
                    bonus = (np.random.normal(1.6, 0.4) * 0.001) + 1
                elif self.potential < 80:
                    bonus = (np.random.normal(2.9, 0.5) * 0.0001) + 1
                elif self.potential < 90:
                    bonus = (np.random.normal(3.5, 0.6) * 0.0001) + 1
                else:
                    bonus = (np.random.normal(4, 1) * 0.0001) + 1
            elif possible_potential > 14 + .06 * self.level:
                if self.potential < 40:
                    bonus = (np.random.normal(-1.3, 0.2) * 0.0001) + 1
                elif self.potential < 60:
                    bonus = (np.random.normal(-0.5, 0.3) * 0.0001) + 1
                elif self.potential < 80:
                    bonus = (np.random.normal(0.2, 0.4) * 0.0001) + 1
                elif self.potential < 90:
                    bonus = (np.random.normal(0.7, 0.5) * 0.0001) + 1
                else:
                    bonus = (np.random.normal(1, 0.8) * 0.0001) + 1
            elif possible_potential > 8 + .06 * self.level:
                if self.potential < 40:
                    bonus = (np.random.normal(-3, 0.5) * 0.0001) + 1
                elif self.potential < 60:
                    bonus = (np.random.normal(-2, 0.6) * 0.0001) + 1
                elif self.potential < 80:
                    bonus = (np.random.normal(-1.5, 0.7) * 0.0001) + 1
                elif self.potential < 90:
                    bonus = (np.random.normal(-1, 0.8) * 0.0001) + 1
                elif self.potential < 97:
                    bonus = (np.random.normal(-0.5, 0.5) * 0.0001) + 1
                else:
                    bonus = (np.random.normal(-0.1, 0.8) * 0.0001) + 1
            else:
                if self.potential < 40:
                    bonus = (np.random.normal(-7, 1) * 0.0001) + 1
                elif self.potential < 60:
                    bonus = (np.random.normal(-6, 1.3) * 0.0001) + 1
                elif self.potential < 80:
                    bonus = (np.random.normal(-4, 1.4) * 0.0001) + 1
                elif self.potential < 90:
                    bonus = (np.random.normal(-3.5, 1.5) * 0.0001) + 1
                elif self.potential < 97:
                    bonus = (np.random.normal(-3, 1.6) * 0.0001) + 1
                else:
                    bonus = (np.random.normal(-2.5, 1.8) * 0.0001) + 1

            for attribute in self.great_attributes:
                setattr(self, attribute, getattr(self, attribute) * bonus)
            for attribute in self.good_attributes:
                setattr(self, attribute, getattr(self, attribute) * (bonus - 0.00003))
            for attribute in self.bad_attributes:
                setattr(self, attribute, getattr(self, attribute) * (bonus - 0.00006))
            for attribute in self.terrible_attributes:
                setattr(self, attribute, getattr(self, attribute) * (bonus - 0.00008))

            for attribute in (self.great_attributes + self.good_attributes + self.bad_attributes +
                              self.terrible_attributes):
                value = getattr(self, attribute)
                setattr(self, attribute, min(max(value, 0), 99))

        self.update_overall()

    def update_overall(self):
        great_average = 0
        good_average = 0
        bad_average = 0
        terrible_average = 0
        for i in self.great_attributes:
            great_average += getattr(self, i)
        for i in self.good_attributes:
            good_average += getattr(self, i)
        for i in self.bad_attributes:
            bad_average += getattr(self, i)
        for i in self.terrible_attributes:
            terrible_average += getattr(self, i)
        great_average /= len(self.great_attributes)
        good_average /= len(self.good_attributes)
        bad_average /= len(self.bad_attributes)
        terrible_average /= len(self.terrible_attributes)

        self.overall = great_average * 0.6 + good_average * 0.25 + bad_average * 0.10 + terrible_average * 0.05

    def update_xp(self, xp_earned):
        self.xp += xp_earned

    def update_age(self):
        self.age += 1

    def return_attributes(self):
        att_list = {
            "overall": self.overall,
            "level": self.level,
            "age": self.age,
            "condition": self.condition,
            "longevity": self.longevity,
            "potential": self.potential,
            "general_stamina": self.general_stamina,
            "throw_power": self.throw_power,
            "throw_accuracy": self.throw_accuracy,
            "throw_stamina": self.throw_stamina,
            "curve_accuracy": self.curve_accuracy,
            "disc_security": self.disc_security,
            "agility": self.agility,
            "speed": self.speed,
            "speed_stamina": self.speed_stamina,
            "catching": self.catching,
            "layout": self.layout,
            "marking": self.marking,
            "ground_defense": self.ground_defense,
            "air_defense": self.air_defense
        }
        return att_list

    def return_name(self):
        return self.name

    def return_position(self):
        return self.position


class UserGame:
    def __init__(self, season, user, team_2, home, start_time, rivalry, tight_race):
        self.season = season
        self.start_time = start_time
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
        self.time = 15.00
        self.quarter = 1
        self.timeouts_u = 3
        self.timeouts_o = 3
        self.penalties_u = 0
        self.penalties_o = 0

    def game_intro(self):
        dialogue(f"It is {self.start_time} and time for a great game of the UFL")

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
        if coin == "h":
            dialogue("The coin lands on heads...")
        else:
            dialogue("The coin lands on tails...")
        if coin == coin_choice and not self.home or coin != coin_choice and self.home:
            self.possession = 1
            dialogue("You won the kickoff!")
        else:
            self.possession = 2
            dialogue("You lost the kickoff.")
        time.sleep(3.5)


def find_good_player():
    attempt = 0
    while True:
        attempt += 1
        test = Player()
        test.initialize_player()
        att = test.return_attributes()
        print(att["throw_power"])
        if att["throw_power"] > 90:
            return test, attempt


player_1, test_attempts = find_good_player()
print(test_attempts)
time.sleep(4)
print(player_1.return_position(), player_1.return_name())
print(player_1.return_attributes())
games = 0
age = 20
for t in range(0, 300):
    time.sleep(0.1)
    games += 1
    player_1.update_xp(475)
    player_1.update_attributes()
    print(player_1.return_attributes())
    if games == 16:
        games = 0
        player_1.update_age()
