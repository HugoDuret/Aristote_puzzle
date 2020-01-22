# Made by HugoDuret
# Started on January, 22, 2020

# Main functions to resolve the Aristote puzzle.

# The game set is represented by a list of 19 objects, starting from top left at 0, going left to right
# going back at the left side for each row

import common

# set the debug to verbose (V) or very verbose (VV)
DEBUG_V = True
DEBUG_VV = False

def main():
    nb_tries = 0
    game_set = common.init_random_game_set()
    game_set_heuristic_value = common.sum_diff_heuristic(game_set)

    print('\tSTARTING game_set')
    common.display_game(game_set)
    print(f'\theuristic value: : {game_set_heuristic_value}')

    min_h_v = 1000

    while ( (nb_tries < common.MAX_TRIES) and (common.sum_diff_heuristic(game_set) > 0) ):
        nb_tries += 1
        print(f"nb_tries: {nb_tries}")

        game_set, game_set_heuristic_value = next_game_set(game_set, game_set_heuristic_value)

        if game_set_heuristic_value < min_h_v:
            min_h_v = game_set_heuristic_value

        if DEBUG_V == True:
            print('\tNEW BEST GAME')
            print(f'\tGame set new heuristic value: {game_set_heuristic_value}')
            common.display_game(game_set)

        if game_set_heuristic_value == 0:
            print('\tSOLUTION FOUND')
            common.display_game(game_set)
            return

    if nb_tries == common.MAX_TRIES:
        print(f' No solution found after {common.MAX_TRIES} tries.')
        print(f'Best heuristic value: {min_h_v}')
    return


# Determines the best next game_set obtainable from the current game_set by switching two numbers.
# Returns this best next game_set and its heuristic value
def next_game_set(game_set, game_set_heuristic_value):
    best_game_set = game_set
    best_heuristic_value = game_set_heuristic_value

    # for each game_set obtainable by switching two numbers
    # we compute the heuristic obtained for this new game_set
    # we keep the game_set with the minimum heuristic
    for i in range(0, 19):
        for j in range(i+1, 19):
            new_game_set = best_game_set

            new_game_set = swap_in_game_set(new_game_set, i, j)

            if DEBUG_VV == True:
                print('\tCURRENT GAME')
                common.display_game(new_game_set)

            # if the new obtained game_set has a better heuristic value than the current one
            # it becomes the best game_set
            new_game_set_heuristic_value = common.sum_diff_heuristic(new_game_set)
            if new_game_set_heuristic_value < best_heuristic_value:
                best_game_set = new_game_set
                best_heuristic_value = new_game_set_heuristic_value
                print(' A NEW BEST GAME_SET HAS BEEN FOUND')
                print(best_game_set)
                print(best_heuristic_value)
            if best_heuristic_value == 0:
                return best_game_set, best_heuristic_value
        
    # shuffle if stuck, TO REMOVE
    if game_set == best_game_set and best_heuristic_value > 0:
        best_game_set = common.init_random_game_set()
        best_heuristic_value = common.sum_diff_heuristic(best_game_set)
    return best_game_set, best_heuristic_value
            
def swap_in_game_set(game_set, i, j):
    new_game_set = game_set
    # swap two numbers
    temp = new_game_set[i]
    new_game_set[i] = new_game_set[j]
    new_game_set[j] = temp

    return new_game_set

main()