import random


class NumberGame:
    def __init__(self, score, correct_num, guess, diff, difff):
        self.score = score
        self.correct_num = correct_num
        self.guess = guess
        self.diff = diff
        self.difff = difff

    def choose_diff(self):
        print('\033[34m')
        self.diff = input("To get started, choose a difficulty (easy, medium, or hard): ").lower()
        if self.diff == "hard":
            self.difff = "Hard"
            self.diff = 150
        elif self.diff == "medium":
            self.difff = "Medium"
            self.diff = 125
        else:
            self.difff = "Easy"
            self.diff = 100

    def print_diff(self):
        if self.diff == 150:
            return "150"
        elif self.diff == 125:
            return "125"
        else:
            return "100"

    def set_num(self):
        self.correct_num = random.randint(0, self.diff)

    def update_score(self):
        if self.guess != self.correct_num:
            self.score = self.score - 13

    def make_guess(self):
        print('\033[39m')
        self.guess = input("Enter your whole number guess: ")
        if self.guess.isnumeric():
            self.guess = int(self.guess)
        else:
            while not self.guess.isnumeric():
                print('\033[31m')
                self.guess = input("INVALID INPUT, please enter a WHOLE NUMBER guess: ")
            self.guess = int(self.guess)

    def evaluate_guess(self):
        if self.guess == self.correct_num:
            print('\033[32m')
            print("YOU WIN! YOUR SCORE IS " + str(self.difff) + "-" + str(self.score) + "!")
            quit()
        elif self.guess > self.correct_num:
            print('\033[34m')
            print("TOO HIGH!")
        else:
            print('\033[34m')
            print("TOO LOW!")

    def loss(self):
        if self.score <= 0:
            return True
        else:
            return False
