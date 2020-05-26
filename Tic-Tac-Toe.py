# global variables
import time
game_still_going = True
winner = None
current_player = "X"
#board

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
#----------------------------------defining functions---------------------------------------------
#display_board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "    1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "    4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "    7 | 8 | 9")
    print()

#handling each player's turn
def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1 - 9:")
    print()
    valid = False
    #will ask if you overwrite
    while not valid:
            # will ask again and again if you enter an invalid input
            while position not in ["1","2","3","4","5","6","7","8","9"]:
                position = input("Invalid input.Try with a proper position for 1-9:")
                print()

            position = int(position)
            position = position - 1

            if board[position] == "-":
                valid = True
            else:
                print("You cant go there.Try again.")
            

    board[position] = player

    display_board()

    

#check if the game is over
def check_over():
    check_for_winner()
        #rows
        #colums
        #diagnols
    check_tie()

#check the winner
def check_for_winner():
    global winner
    row_winner = check_rows()
    col_winner = check_columns()
    diagonal_winner = check_diagnols()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
def check_rows():
    global game_still_going
    #row by row checking
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
#set the game false to stop the loop
    if row1 or row2 or row3:
        game_still_going = False
#return a winner
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    # column by column checking
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    # set the game false to stop the loop
    if col1 or col2 or col3:
        game_still_going = False
    # return a winner
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None

def check_diagnols():
    global game_still_going
    # diagonals by diagonals checking
    diagnols1 = board[0] == board[4] == board[8] != '-'
    diagnols2 = board[2] == board[4] == board[6] != '-'


    # set the game false to stop the loop
    if diagnols1 or diagnols2:
        game_still_going = False
    # return a winner
    if diagnols1:
        return board[0]
    elif diagnols2:
        return board[2]
    else:
        return None


# check if it is a tie
def check_tie():
    global game_still_going
    #if there is no - in the board ,it is a tie
    if "-" not in board:
        game_still_going = False
    

#flip the player
def flip_player():
    global current_player
    #O's turn after X's
    if current_player == "X":
        current_player = "O"
    # X's turn after O's
    elif current_player == "O":
        current_player = "X"

def game_over():
    ask = input("Do you want to play again? y/n ")
    if ask=='n' or 'N' or 'no':
        game_still_going = False

#-----------------------------------------end of defining functions---------------------------------------------
#play game
def play_game():
    display_board()
    #running the game under a loop
    while game_still_going:
        handle_turn(current_player)
        #check if the game is over.If over ,the loop will stop.
        check_over()
        #if the game is not over ,its the next player's turn
        flip_player()

    #printing the winner
    if winner == 'X' or winner == 'O':
        print(winner + " won")
        game_over()
    #if there is no winner(i.e winner = None ) then the game is a tie
    elif winner == None:
        print("Its a tie")
        game_over()
        

    



play_game()
