import os
import time
import random


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


class UserGame:
    def __init__(self, season, user, team_2, home, match, rivalry, tight_race):
        self.season = season
        self.match = match
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
        potential_prompts = []
        if self.season.return_week() == 1:
            dialogue("Welcome to a new season of this year's UFL!")
        elif self.season.return_week() == 14:
            dialogue("Well folks, we have made it to the last game of the season.")
        else:
            potential_prompts = [
                f"It is {self.match} and time for a great game of the UFL",
                "Welcome to another edition of the UFL",
                "Thank you for joining us at the UFL",
                "It’s a beautiful day for the UFL, and the crowd is roaring with anticipation!",
                "We are moments away from another exciting match-up in the UFL!",
                "The stage is set for a thrilling showdown in the UFL!",
                "The energy is electric as we kick off another exciting game in the UFL!",
                "The teams are ready, the fans are ready, and the UFL action is about to begin!",
                "Tonight, it's all about the UFL as these two teams take the field!",
                "The atmosphere here at the UFL is electric – it’s time for some football!",
                f"Welcome to {self.user_name if self.home else self.opponent_name}, where the UFL action never stops!",
                "The countdown is on! It’s game-time, and we’ve got an amazing match-up for you today!",
                "Hold onto your seats, because this is going to be one wild ride of UFL action!"
            ]
        if self.match == "6:30":
            potential_prompts.append("What a wonderful night for some UFL action!")
        if self.match in ["12:00", "1:30", "3:00", "4:30"]:
            potential_prompts.append("Good afternoon everyone, and welcome to the UFL!")

        dialogue(random.choice(potential_prompts))

        potential_prompts = [
            "We have an exciting match-up for you today!",
            "We should have a great game in our midst today",
            "The energy is electric as we get ready for an intense match-up between two powerhouse teams."
            "The teams are ready, the fans are ready, and we are here to bring you the excitement!"
            f"It's game-time here in {self.user_name if self.home else self.opponent_name}"
        ]

        if self.rivalry:
            potential_prompts.extend([
                "The battle lines have been drawn between these two historic teams.",
                "You can feel the rivalry in the air!",
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
