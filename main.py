# the program guesses a number from 1 to 100
# and outputs how many attempts the number was guessed

import numpy as np


def attempt_counter():
    """The function returns the arithmetic mean of the number
    of attempts to guess the number at 1000 repetitions
    """
    # generating a random number from 1 to 100
    number = np.random.randint(1, 101)
    # creating a function repetition counter
    replay_func = 0
    # creating an empty list to store the results of the function execution
    attempts = []
    # Repeat the function 1000 times
    while replay_func < 1001:
        replay_func += 1
        attempts.append(game_core_v1(number))

    # calculate the arithmetic mean number of repetitions
    arithmetic_mean = round(np.mean(attempts))
    return arithmetic_mean


def game_core_v1(hidden_number):
    """Function finds the hidden number"""
    # set the second number to calculate the middle of the
    # interval in which the hidden number is located
    limiting_number = 100
    # creating the starting value
    number = 50
    # creating a counter of attempts to guess the number
    number_attempts = 0

    # find the hidden number
    while True:
        # increasing the counter
        number_attempts += 1
        # find the midpoints of the intervals in which the
        # hidden number can be found
        midpoint = abs(limiting_number - number) // 2
        if number == hidden_number:
            return number_attempts
        elif number < hidden_number:
            # Reducing the search interval for the hidden number
            # with an offset in the smaller direction
            limiting_number = number
            number = number + midpoint
        else:
            # We reduce the search interval for the hidden number
            # with an offset in the larger direction
            limiting_number = number
            number = number - midpoint


print(f"Всреднем число угадывается за {attempt_counter()} попыток.")
