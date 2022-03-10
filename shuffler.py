import random


def shuffler(password_list):
    for i in range(5):
        random.shuffle(password_list)
    password = "".join(password_list)
    print(password)
