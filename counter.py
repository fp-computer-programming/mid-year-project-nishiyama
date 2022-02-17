import random
choices = [
    ['cat', 'dog', 'cow', 'mouse'],['horse', 'bird', 'bat', 'duck'],['cat', 'dog', 'cow', 'mouse'],
    ['horse', 'bird', 'bat', 'duck']
    ]
board = [[],[],[],[]]
board[0] = random.sample(choices[0], 4)
board[1] = random.sample(choices[1], 4)
board[2] = random.sample(choices[2], 4)
board[3] = random.sample(choices[3], 4)
mod_row_a = ['X', 'X', 'X', 'X']
mod_row_b = ['X', 'X', 'X', 'X']
mod_row_c = ['X', 'X', 'X', 'X']
mod_row_d = ['X', 'X', 'X', 'X']
chosen = []
score = len(chosen)
mem_row_1 = 0
mem_row_2 = 0
mem_col_1 = []
mem_col_2 = []
blankspace = ("\n" * 20)
print("\n 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(board[0], board[1], board[2], board[3]))
print('Your objective is to match each of the terms above with one another. The game ends when there are '
'no terms left to be matched. In order to choose a term, you must enter the column (1-4) of the term followed by the '
'row (1-4) on your keyboard.')
begin = input("Please enter 'Y' when you wish to begin: ")
while True:
    try:
        while score < 8:
            if begin.upper() == 'Y':
                print(blankspace)
                print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
                if(len(chosen) == 1):
                    print("You have 1 match")
                else:
                    print('You have {0} matches'.format(len(chosen)))
                column = int(input("Please select a column: "))
                row = int(input("Please select a row: "))
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
                first = column[row - 1]
                mem_row_1 = row
                mem_col_1[mem_row_1 - 1] = "_"
                print(blankspace)
                print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
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
                second = column[row - 1]
                mem_row_2 = row
                mem_col_2[mem_row_2 - 1] = "_"
                print(blankspace)
                print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
                if first == second and (mem_col_1[mem_row_1 - 1] != " "):
                    chosen.append(first)
                    mem_col_1[mem_row_1 - 1] = " "
                    mem_col_2[mem_row_2 - 1] = " "
                    score += 1
                else:
                    mem_col_1[mem_row_1 - 1] = "X"
                    mem_col_2[mem_row_2 - 1] = "X"
        mod_row_a = [' ', ' ', ' ', ' ']
        mod_row_b = [' ', ' ', ' ', ' ']
        mod_row_c = [' ', ' ', ' ', ' ']
        mod_row_d = [' ', ' ', ' ', ' ']
        print(blankspace)
        print(" 1 {0}\n 2 {1}\n 3 {2}\n 4 {3}\n".format(mod_row_a, mod_row_b, mod_row_c, mod_row_d))
        print("You win!\nThank you for playing!")
    except:
        print("An error occurred...")
        break
    else:
        break