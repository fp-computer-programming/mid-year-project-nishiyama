# memory game by aiden

import random

# this list will be sorted out and randomized, it exists to provide the terms for the user

# concept 1 (nested lists)

# concept 2 (lists)

choices = [
    ['cat', 'dog', 'cow', 'mouse'],
    ['horse', 'bird', 'bat', 'duck'],
    ['cat', 'dog', 'cow', 'mouse'],
    ['horse', 'bird', 'bat', 'duck']
    ]

# this is just a layout for the board in order for it to be neatly sorted (making 4 separate lists would seem redunant)

board = [
    [],[],[],[]
    ]

# im sorting out each part of the board in order to make sure no terms are repeated

# concept 3 (random)
board[0] = random.sample(choices[0], 4)
board[1] = random.sample(choices[1], 4)
board[2] = random.sample(choices[2], 4)
board[3] = random.sample(choices[3], 4)

# this is a blank board for in between guesses in order for the user to have an idea of whats happening
mod_row_a = ['X', 'X', 'X', 'X']
mod_row_b = ['X', 'X', 'X', 'X']
mod_row_c = ['X', 'X', 'X', 'X']
mod_row_d = ['X', 'X', 'X', 'X']

placeholder = '_'

# i made this variable to map the users "score"
chosen = []
score = len(chosen)

# these variables act in order to store and compare the terms inputted by the user. im sure there are far easier ways 
# to go about this, but i found this to be the most logical

mem_row_1 = 0
mem_row_2 = 0
mem_col_1 = []
mem_col_2 = []


blankspace = ("\n" * 20)


# i have no idea how to format this better.

# concept 4 (string format method)
print("\n 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(board[0], board[1], board[2], board[3]))

print('Your objective is to match each of the terms above with one another. The game ends when there are '
'no terms left to be matched. In order to choose a term, you must enter the column (1-4) of the term followed by the '
'row (1-4) on your keyboard.')

# concept 5 (inputs)
begin = input("Please enter 'Y' when you wish to begin the game: ")

# initiates the start of the game and the conditions to finish.

# concept 7 (while loops)
while True:

    # concept 7 (try except)
    try:
        while score < 8:
            if begin.upper() == 'Y':
                # still dont know what better way to print these lines, it would defeat the purpose of the game to have
                # the answers displayed onscreen.

                print(blankspace)
                print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
                # small condition which makes it a bit nicer looking by changing the grammar.

                if(len(chosen) == 1):
                    print("You have 1 match")
                else:
                    print('You have {0} matches'.format(len(chosen)))
                # this is the area where the user chooses their first selection. idealy, theyd click the term, but this
                # is only a text-based game and that it not a possibility.

                column = int(input("Please select a column: "))
                row = int(input("Please select a row: "))
                # this is a chained conditional which establishes the users visuals to the correct answers.

                # concept 8 (nested conditionals)

                # concept 9 (conditionals)

                if column == 1:
                    column = board[0]
                    mem_col_1 = mod_row_a
                elif column == 2:
                    column = board[1]
                    mem_col_1 = mod_row_b
                elif column == 3:
                    column = board[2]
                    mem_col_1 = mod_row_c
                elif column == 4:
                    column = board[3]
                    mem_col_1 = mod_row_d
                # this is a variable which shows the users first selection.
                first = column[row - 1]
                mem_row_1 = row
                mem_col_1[mem_row_1 - 1] = placeholder
                print(blankspace)
                print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
                # same exact process for the second selection. again, this seems redundant but i am not sure how else
                # to organize this.

                column = int(input("Please select a new column: "))
                row = int(input("Please select a new row: "))
                if column == 1:
                    column = board[0]
                    mem_col_2 = mod_row_a
                elif column == 2:
                    column = board[1]
                    mem_col_2 = mod_row_b
                elif column == 3:
                    column = board[2]
                    mem_col_2 = mod_row_c
                elif column == 4:
                    column = board[3]
                    mem_col_2 = mod_row_d
                # this variable will store the second value.
                second = column[row - 1]
                mem_row_2 = row
                # this was something that i came up with as the user might not be completely sure of their input.
                mem_col_2[mem_row_2 - 1] = placeholder
                print(blankspace)
                print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
                # if the first term is equal to the second and the terms are not already found, this will be counted
                # towards the users total score.
                
                # concept 10 (logical operators)
                if first == second and (mem_col_1[mem_row_1 - 1] != " "):
                    chosen.append(first)
                    mem_col_1[mem_row_1 - 1] = " "
                    mem_col_2[mem_row_2 - 1] = " "
                    score += 1
                else:
                    mem_col_1[mem_row_1 - 1] = "X"
                    mem_col_2[mem_row_2 - 1] = "X"
        print(blankspace)
        mod_row_a = [' ', ' ', ' ', ' ']
        mod_row_b = [' ', ' ', ' ', ' ']
        mod_row_c = [' ', ' ', ' ', ' ']
        mod_row_d = [' ', ' ', ' ', ' ']
        print(blankspace)
        print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
        print("You win!\nThank you for playing the game!")
    except:
        print("An error occurred, the game has exited.")
        break
    else:
        break