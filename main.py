# the program guesses a number from 1 to 100
# and outputs how many attempts the number was guessed

import numpy as np


def game_core(number):
    """First, set any random number, and then reduce it
       or increase it depending on whether it is more or less than the desired one.
       The function takes a hidden number and returns the number of attempts
    """
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Run the game 1000 times to find out how fast the game guesses the number"""
    count_ls = []
    np.random.seed(1)  # fixing the RANDOM SEED so that your experiment is reproducible!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
