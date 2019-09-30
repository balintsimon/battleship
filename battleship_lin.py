import os
import random


# systemwide functions
def clear_screen():
    #os.system('cls') # clear screen under Windows
    os.system('clear') # clear screen under Linux, macOS

def point_input_for_table(grid_size, printout): # checks if an input is valid within the table
    while True:
        coordinates = input(printout)
        try:
            if len(coordinates) < 2:
                print("Please provide a valid row and column.")
                continue

            if len(coordinates) is 2:
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
                        row = int(row)- 1
                        pass
                    else: #if row.isdigit() is True and int(row) > grid_size:
                        print("Please provide a valid row and column.")
                        continue

                except ValueError:
                        print("Please provide a valid row and culumn.")
                        continue
                    
                try:
                    if column.isalpha() is True and int(convert_char_to_digit(column)) <= grid_size-1:
                        digit_char = 0
                        digit_char = int(convert_char_to_digit(column))
                        break
                    else:
                        print("Please provide a valid row and column.")
                except ValueError:
                    print("Please provide a valid row and column.")
                    continue
                
            if len(coordinates) is 3:
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
                        row = int(row)- 1
                        pass
                    else:
                        print("Please provide a valid row and column.")
                        continue
                except ValueError:
                        print("Please provide a valid row and culumn.")
                        continue
                    
                try:
                    if column.isalpha() is True and int(convert_char_to_digit(column)) <= grid_size-1:
                        digit_char = int(convert_char_to_digit(column))
                        break
                    else:
                        print("Please provide a valid row and column.")
                        continue
                except ValueError:
                    print("Please provide a valid row and column.")
                    continue

            if len(coordinates) > 3:
                print("Please provide a valid row and column.")
                continue

        except ValueError:
            print("Please provide a valid row and column.")
            continue

    return row, digit_char

def convert_char_to_digit(char):
    char_char = ["a","b","c","d","e","f","g","h","i","j"]
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
def rows_size_input(rows): # takes input from user to define size of field
    # define rows size
    while True:
        rows = input("Please enter the size of the table you would like to use (between 6 and 10): ") #number of rows you want (between 6 and 10): ")
        try:
            if int(rows) < 6 or int(rows) > 10:
                print("Please provide a rows size between 6 and 10.")
                continue
            elif int(rows) >= 6 and int(rows) <= 10:
                return int(rows)
                break
        except ValueError:
                print("Please provide a number.")
                continue

def columns_size_input(columns): # takes input from user to define size of field
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

def create_grid(grid, rows, columns): # create any grid
    for _r_ in range(rows):
        row_final = []
        for _c_ in range(columns):
            row_final.append(' ')
        grid.append(row_final)
    return grid

def display_grid(grid, columns): # display mechanism for any grid
    # column labels
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:columns]
    print('    | ' + ' | '.join(column_names.upper()) + ' |')
    
    # row number and the grid
    for number, row in enumerate(grid):
        print(f"{str(number + 1).rjust(3)}", '| ' + ' | '.join(row) + ' |')

def draw_placement_grids(placement_grid, columns, player_name): # summarize the display functions
    clear_screen()
    print(f"\n\t{player_name}'s ships' board:\n")
    display_grid(placement_grid, columns)
    print(f"\n\t'O' = {player_name}'s ship unharmed \n\t'@' = {player_name}'s ship where it got hit")
    print("\n\n")
    print("""Now's the time to place your ships. To do so, first you should choose the begin and end points of your ship, 
    \nbased on it's length (as you can see below).
    \nPlease choose coordinates in the format row first, column second (like '1A') and choose them wisely, so:
    \n\t- you don't cross your own ship(s) and
    \n\t- you stay within the board size you choose.\n\n""")

def draw_play_grids(placement_grid, attack_grid, columns, player_name): # summarize the display functions
    clear_screen()
    print(f"\n\t{player_name}'s ships' board:\n")
    display_grid(placement_grid, columns)
    print(f"\n\t'O' = {player_name}'s ship unharmed \n\t'@' = {player_name}'s ship where it got hit")
    print("\n\n")
    print(f"\t{player_name}'s attack board:\n")
    display_grid(attack_grid, columns)
    print(f"\n\t'X' = where {player_name} attacked, but did not hit \n\t'@' = where {player_name} attacked and hit the enemy\n")


# play related functions
def place_ship_of_any_size(ship_length_to_place, current_grid_size, grid_to_modify, player): #
    if ship_length_to_place is 1:
        while True:
            placement_coord_row, placement_coord_col = point_input_for_table(current_grid_size, f"{player}, where would you like to place a ship of size 1 (ex. 1A): ")
            if grid_to_modify[placement_coord_row][placement_coord_col] != "O":
                grid_to_modify[placement_coord_row][placement_coord_col] = "O"
                break
            elif grid_to_modify[placement_coord_row][placement_coord_col] is "O":
                print("You can't place a ship on top of another. They can't fly.")
                continue
            else:
                continue
        
    elif ship_length_to_place is 2:
        while True:
            placement_coord_row, placement_coord_col = point_input_for_table(current_grid_size, f"{player}, where should your ship of size 2 begin? (ex. 1A): ")
            if grid_to_modify[placement_coord_row][placement_coord_col] != "O":
                grid_to_modify[placement_coord_row][placement_coord_col] = "O"
                while True:
                    placement_coord_row2, placement_coord_col2 = point_input_for_table(current_grid_size, "... and where would you like it to end? (ex. 1A): ")
                    if grid_to_modify[placement_coord_row2][placement_coord_col2] != "O":
                        ship_size_check = (placement_coord_row2 is placement_coord_row and abs(placement_coord_col2 - placement_coord_col) is (ship_length_to_place-1)) or (abs(placement_coord_row2 - placement_coord_row) is (ship_length_to_place-1) and placement_coord_col2 is placement_coord_col)
                        if ship_size_check is True:
                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                            break
                        else:
                            print("Sorry, check your boat's length again to put its rear someplace.")
                            continue
                    elif grid_to_modify[placement_coord_row2][placement_coord_col2] is "O":
                        print("You can't place a ship on top of another. They can't fly. Choose another direction.")
                        continue
                    else:
                        print("WTF?")
                        continue
                break
            elif grid_to_modify[placement_coord_row][placement_coord_col] is "O":
                print("You can't place a ship on top of another. They can't fly.")
                continue
            else:
                print("WTF?")
                continue

    elif ship_length_to_place is 3:
        while True:
            placement_coord_row, placement_coord_col = point_input_for_table(current_grid_size, f"{player}, where should your ship of size 3 begin? (ex. 1A): ")
            if grid_to_modify[placement_coord_row][placement_coord_col] != "O":
                grid_to_modify[placement_coord_row][placement_coord_col] = "O"
                while True:
                    placement_coord_row2, placement_coord_col2 = point_input_for_table(current_grid_size, "...and where would you like it to end? (ex. 1A): ")
                    if grid_to_modify[placement_coord_row2][placement_coord_col2] != "O":
                        ship_size_check = (placement_coord_row2 is placement_coord_row and abs(placement_coord_col2 - placement_coord_col) is (ship_length_to_place-1)) or (abs(placement_coord_row2 - placement_coord_row) is (ship_length_to_place-1) and placement_coord_col2 is placement_coord_col)
                        if ship_size_check is True: # ha jó irányba áll a hajó és megfelelő hosszú is

                            if placement_coord_row2 is placement_coord_row: # ha a sor változó állandó

                                if placement_coord_col2 is (placement_coord_col - (ship_length_to_place - 1)): # ha vízszintesen, balra toljuk el a hajót

                                    if grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 2)] != "O":
                                        grid_to_modify[placement_coord_row2][placement_coord_col - (ship_length_to_place - 2)] = "O"
                                        grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                        break

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                                elif placement_coord_col2 is (placement_coord_col + (ship_length_to_place - 1)): # ha vízszintesen, jobbra áll a hajó

                                    if grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 2)] != "O":
                                        grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 2)] = "O"
                                        grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                        break

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                            elif placement_coord_col2 is placement_coord_col: # ha az oszlop változatlan
                                
                                if placement_coord_row2 is (placement_coord_row - (ship_length_to_place - 1)): # felfelé áll

                                    if grid_to_modify[placement_coord_row2 + (ship_length_to_place - 2)][placement_coord_col2] != "O":
                                        grid_to_modify[placement_coord_row - (ship_length_to_place - 2)][placement_coord_col2] = "O"
                                        grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                        break

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                                elif placement_coord_row2 is (placement_coord_row + (ship_length_to_place - 1)): # lefelé áll

                                    if grid_to_modify[placement_coord_row2 - (ship_length_to_place - 2)][placement_coord_col2] != "O":
                                        grid_to_modify[placement_coord_row + (ship_length_to_place - 2)][placement_coord_col2] = "O"
                                        grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                        break

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                            break
                        else:
                            print("Sorry, check your boat's length again to put its rear someplace.")
                            continue
                    elif grid_to_modify[placement_coord_row2][placement_coord_col2] is "O":
                        print("You can't place a ship on top of another. They can't fly. Choose another direction.")
                        continue
                    else:
                        print("WTF?")
                        continue
                break
            elif grid_to_modify[placement_coord_row][placement_coord_col] is "O":
                print("You can't place a ship on top of another. They can't fly.")
                continue
            else:
                print("WTF?")
                continue

    elif ship_length_to_place is 4:
        while True:
            placement_coord_row, placement_coord_col = point_input_for_table(current_grid_size, f"{player}, where should your ship of size 4 begin? (ex. 1A): ")
            if grid_to_modify[placement_coord_row][placement_coord_col] != "O":
                grid_to_modify[placement_coord_row][placement_coord_col] = "O"
                while True:
                    placement_coord_row2, placement_coord_col2 = point_input_for_table(current_grid_size, "... and where would you like it to end? (ex. 1A): ")
                    if grid_to_modify[placement_coord_row2][placement_coord_col2] != "O":
                        ship_size_check = (placement_coord_row2 is placement_coord_row and abs(placement_coord_col2 - placement_coord_col) is (ship_length_to_place-1)) or (abs(placement_coord_row2 - placement_coord_row) is (ship_length_to_place-1) and placement_coord_col2 is placement_coord_col)
                        if ship_size_check is True: # ha jó irányba áll a hajó és megfelelő hosszú is

                            if placement_coord_row2 is placement_coord_row: # ha a sor változatlan

                                if placement_coord_col2 is (placement_coord_col - (ship_length_to_place - 1)): # ha vízszintesen, balra toljuk el a hajót

                                    if grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 2)] != "O":

                                        if grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 3)] != "O":
                                            grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 2)] = "O"
                                            grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 3)] = "O"
                                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                            break
                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                                elif placement_coord_col2 is (placement_coord_col + (ship_length_to_place - 1)): # ha vízszintesen, jobbra áll a hajó

                                    if grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 2)] != "O":

                                        if grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 3)] != "O":
                                            grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 2)] = "O"
                                            grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 3)] = "O"
                                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                            break
                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                            elif placement_coord_col2 is placement_coord_col: # ha az oszlop változatlan
                                
                                if placement_coord_row2 is (placement_coord_row - (ship_length_to_place - 1)): # felfelé áll

                                    if grid_to_modify[placement_coord_row2 + (ship_length_to_place - 2)][placement_coord_col2] != "O":

                                        if grid_to_modify[placement_coord_row2 + (ship_length_to_place - 3)][placement_coord_col2] != "O":
                                            grid_to_modify[placement_coord_row - (ship_length_to_place - 2)][placement_coord_col2] = "O"
                                            grid_to_modify[placement_coord_row - (ship_length_to_place - 3)][placement_coord_col2] = "O"
                                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                            break

                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                                elif placement_coord_row2 is (placement_coord_row + (ship_length_to_place - 1)): # lefelé áll

                                    if grid_to_modify[placement_coord_row2 - (ship_length_to_place - 2)][placement_coord_col2] != "O":

                                        if grid_to_modify[placement_coord_row2 - (ship_length_to_place - 3)][placement_coord_col2] != "O":
                                            grid_to_modify[placement_coord_row + (ship_length_to_place - 2)][placement_coord_col2] = "O"
                                            grid_to_modify[placement_coord_row + (ship_length_to_place - 3)][placement_coord_col2] = "O"
                                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                            break

                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                            break
                        else:
                            print("Sorry, check your boat's length again to put its rear someplace.")
                            continue
                    elif grid_to_modify[placement_coord_row2][placement_coord_col2] is "O":
                        print("You can't place a ship on top of another. They can't fly. Choose another direction.")
                        continue
                    else:
                        print("WTF?")
                        continue
                break
            elif grid_to_modify[placement_coord_row][placement_coord_col] is "O":
                print("You can't place a ship on top of another. They can't fly.")
                continue
            else:
                print("WTF?")
                continue

    elif ship_length_to_place is 5:
        while True:
            placement_coord_row, placement_coord_col = point_input_for_table(current_grid_size, f"{player}, where should your ship of size 5 begin? (ex. 1A): ")
            if grid_to_modify[placement_coord_row][placement_coord_col] != "O":
                grid_to_modify[placement_coord_row][placement_coord_col] = "O"
                while True:
                    placement_coord_row2, placement_coord_col2 = point_input_for_table(current_grid_size, "... and where would you like it to end? (ex. 1A): ")
                    if grid_to_modify[placement_coord_row2][placement_coord_col2] != "O":
                        ship_size_check = (placement_coord_row2 is placement_coord_row and abs(placement_coord_col2 - placement_coord_col) is (ship_length_to_place-1)) or (abs(placement_coord_row2 - placement_coord_row) is (ship_length_to_place-1) and placement_coord_col2 is placement_coord_col)
                        if ship_size_check is True: # ha jó irányba áll a hajó és megfelelő hosszú is

                            if placement_coord_row2 is placement_coord_row: # ha a sor változatlan

                                if placement_coord_col2 is (placement_coord_col - (ship_length_to_place - 1)): # ha vízszintesen, balra toljuk el a hajót

                                    if grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 2)] != "O":

                                        if grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 3)] != "O":

                                            if grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 4)] != "O":
                                                grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 2)] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 3)] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2 + (ship_length_to_place - 4)] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                                break

                                            else:
                                                print("You can't place a ship on top of another. They can't fly.")
                                                continue

                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                                elif placement_coord_col2 is (placement_coord_col + (ship_length_to_place - 1)): # ha vízszintesen, jobbra áll a hajó

                                    if grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 2)] != "O":

                                        if grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 3)] != "O":
                                            
                                            if grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 4)] != "O":
                                                grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 2)] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 3)] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2 - (ship_length_to_place - 4)] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                                break

                                            else:
                                                print("You can't place a ship on top of another. They can't fly.")
                                                continue

                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                            elif placement_coord_col2 is placement_coord_col: # ha az oszlop változatlan
                                
                                if placement_coord_row2 is (placement_coord_row - (ship_length_to_place - 1)): # felfelé áll

                                    if grid_to_modify[placement_coord_row2 + (ship_length_to_place - 2)][placement_coord_col2] != "O":

                                        if grid_to_modify[placement_coord_row2 + (ship_length_to_place - 3)][placement_coord_col2] != "O":

                                            if grid_to_modify[placement_coord_row2 + (ship_length_to_place - 4)][placement_coord_col2] != "O":
                                                grid_to_modify[placement_coord_row - (ship_length_to_place - 2)][placement_coord_col2] = "O"
                                                grid_to_modify[placement_coord_row - (ship_length_to_place - 3)][placement_coord_col2] = "O"
                                                grid_to_modify[placement_coord_row - (ship_length_to_place - 4)][placement_coord_col2] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                                break

                                            else:
                                                print("You can't place a ship on top of another. They can't fly.")
                                                continue

                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                                elif placement_coord_row2 is (placement_coord_row + (ship_length_to_place - 1)): # lefelé áll

                                    if grid_to_modify[placement_coord_row2 - (ship_length_to_place - 2)][placement_coord_col2] != "O":

                                        if grid_to_modify[placement_coord_row2 - (ship_length_to_place - 3)][placement_coord_col2] != "O":
                                            
                                            if grid_to_modify[placement_coord_row2 - (ship_length_to_place - 4)][placement_coord_col2] != "O":
                                                grid_to_modify[placement_coord_row + (ship_length_to_place - 2)][placement_coord_col2] = "O"
                                                grid_to_modify[placement_coord_row + (ship_length_to_place - 3)][placement_coord_col2] = "O"
                                                grid_to_modify[placement_coord_row + (ship_length_to_place - 4)][placement_coord_col2] = "O"
                                                grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                                                break

                                            else:
                                                print("You can't place a ship on top of another. They can't fly.")
                                                continue

                                        else:
                                            print("You can't place a ship on top of another. They can't fly.")
                                            continue

                                    else:
                                        print("You can't place a ship on top of another. They can't fly.")
                                        continue

                            grid_to_modify[placement_coord_row2][placement_coord_col2] = "O"
                            break
                        else:
                            print("Sorry, check your boat's length again to put its rear someplace.")
                            continue
                    elif grid_to_modify[placement_coord_row2][placement_coord_col2] is "O":
                        print("You can't place a ship on top of another. They can't fly. Choose another direction.")
                        continue
                    else:
                        print("WTF?")
                        continue
                break
            elif grid_to_modify[placement_coord_row][placement_coord_col] is "O":
                print("You can't place a ship on top of another. They can't fly.")
                continue
            else:
                print("WTF?")
                continue

    else:
        print("There's no such ship that would match the size")

def attack_placement(row, column, current_grid_size, attack_grid_to_modify, defence_grid_to_modify):
    attack_coord_row, attack_coord_col = point_input_for_table(current_grid_size, "Enter where you want to shoot (ex. 1A): ")
    did_it_hit(attack_coord_row, attack_coord_col, attack_grid_to_modify, defence_grid_to_modify)
    return attack_coord_row, attack_coord_col

def did_it_hit(row_to_modify, column_to_modify, attack_grid, defence_grid): # rewrites attack and defence grids according to the input
    if defence_grid[row_to_modify][column_to_modify] is "O":
        attack_grid[row_to_modify][column_to_modify] = "@"

    elif defence_grid[row_to_modify][column_to_modify] is "@":
        defence_grid[row_to_modify][column_to_modify] = "@"
        attack_grid[row_to_modify][column_to_modify] = "@"

    else: 
        attack_grid[row_to_modify][column_to_modify] = "X"

def say_it_if_did_hit(row_to_modify, column_to_modify, attack_grid, defence_grid, player_hit_counter):
    if defence_grid[row_to_modify][column_to_modify] is "O":
        print("You hit something...")
        defence_grid[row_to_modify][column_to_modify] = "@"
        player_hit_counter = player_hit_counter + 1
        return player_hit_counter

    if defence_grid[row_to_modify][column_to_modify] is "@":
        print("You already hit something there...")
        return player_hit_counter

    else: 
        print("You missed.")
        return player_hit_counter


# main game functions
def set_variables():
    # grid size variables
    global rows
    global columns

    # lists for player 1
    global player1_ship_grid
    global player1_attack_grid
    global player1_hit_counter

    # lists for player 2
    global player2_ship_grid
    global player2_attack_grid
    global player2_hit_counter

    # attack related variables
    global attack_row 
    global attack_column
    global wincheck_amount

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

def boot():
    global rows
    global columns
    clear_screen()
    print("\nWelcome to battleship!\n")
    print("Player 1, plase define board size.\n")

    # define grid size
    rows = rows_size_input(rows)
    columns = rows #columns_size_input(columns)

def player1_placement_phase():
    global player1_attack_grid
    global player1_ship_grid
    global columns
    global rows
    global wincheck_amount
    # 1------------------------------------------------------------------
    # create Player 1 fields
    player1_ship_grid = create_grid(player1_ship_grid, rows, columns)
    player1_attack_grid = create_grid(player1_attack_grid, rows, columns)

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

def player2_placement_phase():
    global player2_ship_grid
    global player2_attack_grid
    global rows
    global columns
    # 2-----------------------------------------------------------------
    # create Player 2 fields
    player2_ship_grid = create_grid(player2_ship_grid, rows, columns)
    player2_attack_grid = create_grid(player2_attack_grid, rows, columns)

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

def play_phase():
    global player1_hit_counter
    global player2_hit_counter
    global wincheck_amount
    global player1_attack_grid
    global player2_attack_grid
    global player1_ship_grid
    global player2_ship_grid
    global rows
    global columns
    global attack_row
    global attack_column

    while player1_hit_counter < wincheck_amount or player2_hit_counter < wincheck_amount:
        # Player 1's turn
        clear_screen()
        draw_play_grids(player1_ship_grid, player1_attack_grid, columns, "Player 1")
        hit_row, hit_column = attack_placement(attack_row, attack_column, rows, player1_attack_grid, player2_ship_grid)
        clear_screen()
        draw_play_grids(player1_ship_grid, player1_attack_grid, columns, "Player 1")
        player1_hit_counter = say_it_if_did_hit(hit_row, hit_column, player1_attack_grid, player2_ship_grid, player1_hit_counter)
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
        player2_hit_counter = say_it_if_did_hit(hit_row, hit_column, player2_attack_grid, player1_ship_grid, player2_hit_counter)
        if player2_hit_counter is wincheck_amount:
            break
        if player1_hit_counter < wincheck_amount:
            pass
        switch_to_player1()

def winner_is():
    global player1_hit_counter
    global player2_hit_counter
    global wincheck_amount

    if player1_hit_counter is wincheck_amount:
        clear_screen()
        print("Thank you for playing.\n\tPlayer 1 won.")

    elif player2_hit_counter is wincheck_amount:
        clear_screen()
        print("Thank you for playing.\n\tPlayer 2 won.")

def main():
    set_variables()
    boot()
    player1_placement_phase()
    switch_to_player2()
    player2_placement_phase()
    switch_to_battle_mode()
    play_phase()
    winner_is()

# -----------------------------------------------------------------------------------------------------
main()