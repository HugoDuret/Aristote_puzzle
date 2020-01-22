# Made by HugoDuret
# Started on January, 22, 2020

# Common functions to help resolve the Aristote puzzle.

# The game set is represented by a list of 19 objects, starting from top left at 0, going left to right
# going back at the left side for each row

from random import shuffle

# CONSTANTS
MAX_TRIES = 10_000

# This function computes the sum of all differences between 38 and the combinations.
# They are:
#  - 6 combinations of length 3
#  - 6 combinations of length 4
#  - 3 combinations of length 5
def sum_diff_heuristic(game_set):
    total_difference = 0
    length3_diff = 0
    length4_diff = 0
    length5_diff = 0

    # The 6 combinations of length 3
    length3_diff += abs(38 - (game_set[0] + game_set[1] + game_set[2]) )
    length3_diff += abs(38 - (game_set[0] + game_set[3] + game_set[7]) )
    length3_diff += abs(38 - (game_set[2] + game_set[6] + game_set[11]) )
    length3_diff += abs(38 - (game_set[11] + game_set[15] + game_set[18]) )
    length3_diff += abs(38 - (game_set[16] + game_set[17] + game_set[18]) )
    length3_diff += abs(38 - (game_set[7] + game_set[12] + game_set[16]) )

    # total_difference += length3_diff

    # The 6 combinations of length 4
    length4_diff += abs(38 - (game_set[1] + game_set[4] + game_set[8] + game_set[12]) )
    length4_diff += abs(38 - (game_set[3] + game_set[4] + game_set[5] + game_set[6]) )
    length4_diff += abs(38 - (game_set[1] + game_set[5] + game_set[10] + game_set[15]) )
    length4_diff += abs(38 - (game_set[6] + game_set[10] + game_set[14] + game_set[17]) )
    length4_diff += abs(38 - (game_set[12] + game_set[13] + game_set[14] + game_set[15]) )
    length4_diff += abs(38 - (game_set[3] + game_set[8] + game_set[13] + game_set[17]) )

    total_difference += length4_diff

    # The 3 combinations of length 5
    length5_diff += abs(38 - (game_set[0] + game_set[4] + game_set[9] + game_set[14] + game_set[18]) )
    length5_diff += abs(38 - (game_set[2] + game_set[5] + game_set[9] + game_set[13] + game_set[16]) )
    length5_diff += abs(38 - (game_set[7] + game_set[8] + game_set[9] + game_set[10] + game_set[11]) )

    # total_difference += length5_diff

    return total_difference


# Creates a shuffled list of integers from 1 to 19
def init_random_game_set():
    game_set = [i + 1 for i in range(19)]
    shuffle(game_set)
    return game_set


# Display the game passed as a parameter in the console
def display_game(game_set):
    print('\n')
    print(f'\t    {game_set[0]} - {game_set[1]} - {game_set[2]}')
    print(f'\t  {game_set[3]} - {game_set[4]} - {game_set[5]} - {game_set[6]}')
    print(f'\t{game_set[7]} - {game_set[8]} - {game_set[9]} - {game_set[10]} - {game_set[11]}')
    print(f'\t  {game_set[12]} - {game_set[13]} - {game_set[14]} - {game_set[15]}')
    print(f'\t    {game_set[16]} - {game_set[17]} - {game_set[18]}')
    print('\n')

