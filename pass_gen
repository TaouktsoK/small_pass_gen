import string
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

# the above class picks letter from each category

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
special = "!@#$%^&*()-=_=,./?"
pass_length = 0
full_char = [lower_letters, upper_letters, numbers, special]

flag = True
while flag:

    print("""Recommended length for a password is at least ten characters,
    if you want longer password, press the number of characters
    else just press enter:""")

    length_choise = input("Choose the length of password: ")
    while length_choise.isdigit() == False and length_choise != "":
        print("Thats not a right password length.")
        length_choise = input("Choose again the length of password: ")
    if length_choise == "":
        pass_length = 11
    else:
        pass_length = int(length_choise)
        while pass_length < 11:
            length_choise = input("""password length is less than 10 characters
    choose a new password length: """)
            pass_length = int(length_choise)



    password_list = []
    password = ""
    lower_range = 3
    upper_range = 2
    num_range = 3
    special_range = 2
    counter = 1

    """ in case of larger than default password
    I add more characters of each category"""

    if pass_length >= 11:
        length_diff = pass_length - 10
        while length_diff > 0:
            if counter == 1:
                upper_range += 1
            elif counter == 2:
                special_range += 1
            elif counter == 3:
                num_range += 1
            else:
                lower_range += 1
            counter += 1
            length_diff -= 1


    keygen = KeyGenSelector(full_char)

    for i in range(lower_range):
        lett = keygen.lower_pick()
        password_list.append(lett)

    for i in range(num_range):
        lett = keygen.number_pick()
        password_list.append(lett)

    for i in range(upper_range):
        lett = keygen.upper_pick()
        password_list.append(lett)

    for i in range(special_range):
        lett = keygen.special_pick()
        password_list.append(lett)

    for i in range(5):
        random.shuffle(password_list)
    password = "".join(password_list)
    print(password)
    
    print("""if you want to quit, press q(and enter),
if you want another password, just press enter. """)
    if input().lower() == "q":
        flag = False
