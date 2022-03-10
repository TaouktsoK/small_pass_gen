import random


class KeyGenSelector:
    def __init__(self, full_char):
        self.lower_letters = full_char[0]
        self.upper_letters = full_char[1]
        self.numbers = full_char[2]
        self.special = full_char[3]

    def lower_pick(self):
        global lett
        lett = random.choice(self.lower_letters)
        return lett

    def upper_pick(self):
        global lett
        lett = random.choice(self.upper_letters)
        return lett

    def number_pick(self):
        global lett
        lett = random.choice(self.numbers)
        return lett

    def special_pick(self):
        global lett
        lett = random.choice(self.special)
        return lett


