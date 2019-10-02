import os


# systemwide functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def point_input_for_table(grid_size, message):  # checks if an input is valid within the table
    message_not_valid_place = "Please provide a valid row and column."

    while True:
        coordinates = input(message)

        try:
            if len(coordinates) < 2:
                print(message_not_valid_place)
                continue

            if len(coordinates) == 2:
                row, column = list(coordinates)

                try:
                    if row.isdigit() is False and column.isalpha() is False:
                        row, column = column, row
                    else:
                        pass
                except:
                    pass

                try:
                    if row.isdigit() is True and int(row) <= grid_size and int(row) != 0:
                        row = int(row) - 1
                        pass
                    else:  # if row.isdigit() is True and int(row) > grid_size:
                        print(message_not_valid_place)
                        continue

                except ValueError:
                    print(message_not_valid_place)
                    continue

                try:
                    if column.isalpha() is True and int(convert_char_to_digit(column)) <= grid_size-1:
                        digit_char = 0
                        digit_char = int(convert_char_to_digit(column))
                        break
                    else:
                        print(message_not_valid_place)
                except ValueError:
                    print(message_not_valid_place)
                    continue

            if len(coordinates) == 3:
                row1, row2, column = list(coordinates)

                try:
                    if row1.isdigit() is False and row2.isdigit() is True and column.isalpha() is False:
                        row1, column = column, row1
                        row = str(row2) + str(row1)
                    else:
                        row = str(row1) + str(row2)
                        pass
                except:
                    row = str(row1) + str(row2)
                    pass

                try:
                    if row.isdigit() is True and int(row) <= grid_size:
                        row = int(row) - 1
                        pass
                    else:
                        print(message_not_valid_place)
                        continue
                except ValueError:
                    print(message_not_valid_place)
                    continue

                try:
                    if column.isalpha() is True and int(convert_char_to_digit(column)) <= grid_size-1:
                        digit_char = int(convert_char_to_digit(column))
                        break
                    else:
                        print(message_not_valid_place)
                        continue
                except ValueError:
                    print(message_not_valid_place)
                    continue

            if len(coordinates) > 3:
                print(message_not_valid_place)
                continue

        except ValueError:
            print(message_not_valid_place)
            continue

    return row, digit_char  # row_num, coord_num


def convert_char_to_digit(char):
    char_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return char_char.index(char.lower())


def switch_to_battle_mode():
    input("Press enter to switch to Player1 > ")
    clear_screen()
    input("Press enter to initiate battle mode for Player1 > ")


def switch_to_player1():
    input("Press enter to switch to Player 1 > ")
    clear_screen()
    input("Press enter to initiate Player 1 > ")


def switch_to_player2():
    input("Press enter to switch to Player 2 > ")
    clear_screen()
    input("Press enter to initiate Player 2 > ")


# grid creation functions
def rows_size_input(rows):  # takes input from user to define size of field
    # define rows size
    while True:
        rows = input("Please enter the size of the table you would like to use (between 6 and 10): ")
        try:
            if int(rows) < 6 or int(rows) > 10:
                print("Please provide a rows size between 6 and 10.")
                continue
            elif int(rows) >= 6 and int(rows) <= 10:
                return int(rows)
        except ValueError:
            print("Please provide a number.")
            continue


""" Feature no longer in use since regular sized (square) boards are used

def columns_size_input(columns):  # takes input from user to define size of field
    # define columns size

    while True:
        columns = input("Please enter the number of columns you want (between 6 and 10): ")
        try:
            if int(columns) < 6 or int(columns) > 10:
                print("Please provide a column size between 6 and 10.")
                continue
            elif int(columns) >= 6 and int(columns) <= 10:
                return int(columns)
                break
        except ValueError:
            print("Please provide a number.")
            continue
"""


def create_grid(rows, columns):  # create any grid
    return [[(' ') for c in range(columns)] for r in range(rows)]


def display_grid(grid, columns):  # display mechanism for any grid
    # column labels
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:columns]
    print('    | ' + ' | '.join(column_names.upper()) + ' |')

    # row number and the grid
    for number, row in enumerate(grid):
        print(f"{str(number + 1).rjust(3)}", '| ' + ' | '.join(row) + ' |')


def draw_placement_grids(placement_grid, columns, player_name):  # summarize the display functions
    clear_screen()
    print(f"\n\t{player_name}'s ships' board:\n")
    display_grid(placement_grid, columns)
    print(f"\n\t'O' = {player_name}'s ship unharmed \n\t'@' = {player_name}'s ship where it got hit")
    print("\n\n")
    print(
            "Now's the time to place your ships as instructed below. To do so, you should choose"
            + "the begining and direction of your ship so that you:"
            + "\n\t- don't cross your own ship(s) and"
            + "\n\t- stay within the board size you choose.\n\n"
        )


def draw_play_grids(placement_grid, attack_grid, columns, player_name):  # summarize the display functions
    clear_screen()
    print(f"\n\t{player_name}'s ships' board:\n")
    display_grid(placement_grid, columns)
    print(f"\n\t'O' = {player_name}'s ship unharmed \n\t'@' = {player_name}'s ship where it got hit")
    print("\n\n")
    print(f"\t{player_name}'s attack board:\n")
    display_grid(attack_grid, columns)
    print(f"\n\t'X' = where {player_name} attacked, but did not hit")
    print(f"\t'@' = where {player_name} attacked and hit the enemy\n")


# play related functions
def place_ship_of_any_size(ship_length_to_place, current_grid_size, grid_to_modify, player):
    ship_character = "\033[32m0\033[1;m"
    message_set_origin = (
                            f"{player}, from where would you like to place your ship "
                            + f"of size {ship_length_to_place} (e.g. 1A or A1)? "
                        )
    message_direction = "In which direction should it point (up, down, left or right)? "
    message_error = "You can't place a ship there."
    message_wrong_input = "Not a valid input."

    def check_left(row, column, grid_size, ship_size, playgrid, ship_character):
        while True:
            if column - ship_size <= grid_size and column - (ship_size - 1) >= 0:
                # ship size conversion due to ship's size numbers not starting
                # from 0 but 1, but column range starts from 0, not 1
                # -1 needed for number system conversion
                pass

            else:
                return(False)

            for i in range(0, ship_size):
                if playgrid[row][column - i] == ship_character:
                    return False

                else:
                    pass

            return True

    def check_right(row, column, grid_size, ship_size, playgrid, ship_character):
        while True:
            if column + ship_size <= grid_size and column + ship_size >= 0:
                pass

            else:
                return(False)

            for i in range(0, ship_size):
                if playgrid[row][column + i] == ship_character:
                    return False

                else:
                    pass

            return True

    def check_down(row, column, grid_size, ship_size, playgrid, ship_character):
        while True:
            if row + ship_size <= grid_size and row + ship_size >= 0:
                pass

            else:
                return(False)

            for i in range(0, ship_size):
                if playgrid[row + i][column] == ship_character:
                    return False

                else:
                    pass

            return True

    def check_up(row, column, grid_size, ship_size, playgrid, ship_character):
        while True:
            if row - ship_size <= grid_size and row - (ship_size - 1) >= 0:
                # ship size conversion due to ship's size numbers not starting
                # from 0 but 1, but rows range starts from 0, not 1
                # -1 needed for number system conversion
                pass

            else:
                return(False)

            for i in range(0, ship_size):
                if playgrid[row - i][column] == ship_character:
                    return False

                else:
                    pass

            return True

    while True:
        while True:
            origin_row, origin_column = point_input_for_table(current_grid_size, message_set_origin)
            if grid_to_modify[origin_row][origin_column] == ship_character:
                print(message_error)
                continue
            else:
                break

        placement = True

        while placement is True:  # input direction and check whether it is valid
            direction = input(message_direction).lower()

            # check valid input
            if direction in ("up", "down", "right", "left"):
                pass
            else:
                print(message_wrong_input)
                continue

            # check if placement is possible in given direction
            if direction == "up":
                if check_up(origin_row,
                            origin_column,
                            current_grid_size,
                            ship_length_to_place,
                            grid_to_modify,
                            ship_character
                            ) is True:
                    break
                else:
                    print(message_error)
                    placement = False
                    continue

            elif direction == "down":
                if check_down(origin_row,
                              origin_column,
                              current_grid_size,
                              ship_length_to_place,
                              grid_to_modify,
                              ship_character
                              ) is True:
                    break
                else:
                    print(message_error)
                    placement = False
                    continue

            elif direction == "left":
                if check_left(origin_row,
                              origin_column,
                              current_grid_size,
                              ship_length_to_place,
                              grid_to_modify,
                              ship_character
                              ) is True:
                    break
                else:
                    print(message_error)
                    placement = False
                    continue

            elif direction == "right":
                if check_right(origin_row,
                               origin_column,
                               current_grid_size,
                               ship_length_to_place,
                               grid_to_modify,
                               ship_character
                               ) is True:
                    break
                else:
                    print(message_error)
                    placement = False
                    continue

            else:
                print(message_wrong_input)
                continue

        # place ships in given direction and from origin
        if placement is True:
            if direction == "up":
                for i in range(0, ship_length_to_place):
                    grid_to_modify[origin_row - i][origin_column] = ship_character
                break

            elif direction == "down":
                for i in range(0, ship_length_to_place):
                    grid_to_modify[origin_row + i][origin_column] = ship_character
                break

            elif direction == "left":
                for i in range(0, ship_length_to_place):
                    grid_to_modify[origin_row][origin_column - i] = ship_character
                break

            elif direction == "right":
                for i in range(0, ship_length_to_place):
                    grid_to_modify[origin_row][origin_column + i] = ship_character
                break
        else:
            continue


def attack_placement(row, column, current_grid_size, attack_grid_to_modify, defence_grid_to_modify):
    message = "Enter where you want to shoot (ex. 1A): "
    attack_coord_row, attack_coord_col = point_input_for_table(current_grid_size, message)
    did_it_hit(attack_coord_row, attack_coord_col, attack_grid_to_modify, defence_grid_to_modify)
    return attack_coord_row, attack_coord_col


# rewrites attack and defence grids according to the input
def did_it_hit(row_to_modify, column_to_modify, attack_grid, defence_grid):
    ship_character = "\033[32m0\033[1;m"
    hit_character = "\033[31m@\033[1;m"
    miss_character = "\033[33mX\033[1;m"

    if defence_grid[row_to_modify][column_to_modify] == ship_character:
        attack_grid[row_to_modify][column_to_modify] = hit_character

    elif defence_grid[row_to_modify][column_to_modify] == hit_character:
        defence_grid[row_to_modify][column_to_modify] = hit_character
        attack_grid[row_to_modify][column_to_modify] = hit_character

    else:
        attack_grid[row_to_modify][column_to_modify] = miss_character


def say_it_if_did_hit(row_to_modify, column_to_modify, attack_grid, defence_grid, player_hit_counter):
    ship_character = "\033[32m0\033[1;m"
    hit_character = "\033[31m@\033[1;m"

    if defence_grid[row_to_modify][column_to_modify] == ship_character:
        print("You hit something...")
        defence_grid[row_to_modify][column_to_modify] = hit_character
        player_hit_counter = player_hit_counter + 1
        return player_hit_counter

    if defence_grid[row_to_modify][column_to_modify] == hit_character:
        print("You already hit something there...")
        return player_hit_counter

    else:
        print("You missed.")
        return player_hit_counter


# main game functions
def main():
    # set variables --------------------------

    # grid size variables
    rows = 0
    columns = 0

    # lists for player 1
    player1_ship_grid = []
    player1_attack_grid = []
    player1_hit_counter = 0

    # lists for player 2
    player2_ship_grid = []
    player2_attack_grid = []
    player2_hit_counter = 0

    # attack related variables
    attack_row = 0
    attack_column = ""
    wincheck_amount = 0

    # -------------------------------------------
    # board size phase --------------------------
    clear_screen()
    print("\nWelcome to battleship!\n")
    print("Player 1, plase define board size.\n")

    # define grid size
    rows = rows_size_input(rows)
    columns = rows  # columns_size_input(columns)

    # -------------------------------------------
    # Player 1 placement phase-------------------

    # create Player 1 fields
    player1_ship_grid = create_grid(rows, columns)
    player1_attack_grid = create_grid(rows, columns)

    # player 1 places ships

    if rows >= 8:
        clear_screen()
        draw_placement_grids(player1_ship_grid, columns, "Player 1")
        place_ship_of_any_size(5, rows, player1_ship_grid, "Player 1")
        wincheck_amount += 5

        clear_screen()
        draw_placement_grids(player1_ship_grid, columns, "Player 1")
        place_ship_of_any_size(4, rows, player1_ship_grid, "Player 1")
        wincheck_amount += 4

    else:
        pass

    clear_screen()
    draw_placement_grids(player1_ship_grid, columns, "Player 1")
    place_ship_of_any_size(3, rows, player1_ship_grid, "Player 1")
    wincheck_amount += 3

    clear_screen()
    draw_placement_grids(player1_ship_grid, columns, "Player 1")
    place_ship_of_any_size(3, rows, player1_ship_grid, "Player 1")
    wincheck_amount += 3

    clear_screen()
    draw_placement_grids(player1_ship_grid, columns, "Player 1")
    place_ship_of_any_size(2, rows, player1_ship_grid, "Player 1")
    wincheck_amount += 2

    clear_screen
    draw_placement_grids(player1_ship_grid, columns, "Player 1")

    # -------------------------------------------
    # Player 2 placement phase-------------------

    # create Player 2 fields
    player2_ship_grid = create_grid(rows, columns)
    player2_attack_grid = create_grid(rows, columns)

    # Player 2 places ships
    if rows >= 8:
        clear_screen()
        draw_placement_grids(player2_ship_grid, columns, "Player 2")
        place_ship_of_any_size(5, rows, player2_ship_grid, "Player 2")

        clear_screen()
        draw_placement_grids(player2_ship_grid, columns, "Player 2")
        place_ship_of_any_size(4, rows, player2_ship_grid, "Player 2")

    else:
        pass

    clear_screen()
    draw_placement_grids(player2_ship_grid, columns, "Player 2")
    place_ship_of_any_size(3, rows, player2_ship_grid, "Player 2")

    clear_screen()
    draw_placement_grids(player2_ship_grid, columns, "Player 2")
    place_ship_of_any_size(3, rows, player2_ship_grid, "Player 2")

    clear_screen()
    draw_placement_grids(player2_ship_grid, columns, "Player 2")
    place_ship_of_any_size(2, rows, player2_ship_grid, "Player 2")

    clear_screen()
    draw_placement_grids(player2_ship_grid, columns, "Player 2")

    # -------------------------------------------
    # battle mode -------------------------------

    while player1_hit_counter < wincheck_amount or player2_hit_counter < wincheck_amount:
        # Player 1's turn
        clear_screen()
        draw_play_grids(player1_ship_grid, player1_attack_grid, columns, "Player 1")
        hit_row, hit_column = attack_placement(attack_row,
                                               attack_column,
                                               rows,
                                               player1_attack_grid,
                                               player2_ship_grid
                                               )
        clear_screen()
        draw_play_grids(player1_ship_grid, player1_attack_grid, columns, "Player 1")
        player1_hit_counter = say_it_if_did_hit(hit_row,
                                                hit_column,
                                                player1_attack_grid,
                                                player2_ship_grid,
                                                player1_hit_counter
                                                )
        if player1_hit_counter is wincheck_amount:
            break
        if player1_hit_counter < wincheck_amount:
            pass
        switch_to_player2()

        # Player 2's turn
        clear_screen()
        draw_play_grids(player2_ship_grid, player2_attack_grid, columns, "Player 2")
        hit_row, hit_column = attack_placement(attack_row, attack_column, rows, player2_attack_grid, player1_ship_grid)
        clear_screen()
        draw_play_grids(player2_ship_grid, player2_attack_grid, columns, "Player 2")
        player2_hit_counter = say_it_if_did_hit(hit_row,
                                                hit_column,
                                                player2_attack_grid,
                                                player1_ship_grid,
                                                player2_hit_counter
                                                )
        if player2_hit_counter is wincheck_amount:
            break
        if player1_hit_counter < wincheck_amount:
            pass
        switch_to_player1()

    # -------------------------------------------
    # wincheck ----------------------------------

    if player1_hit_counter is wincheck_amount:
        clear_screen()
        print("Thank you for playing.\n\tPlayer 1 won.")

    elif player2_hit_counter is wincheck_amount:
        clear_screen()
        print("Thank you for playing.\n\tPlayer 2 won.")


main()
