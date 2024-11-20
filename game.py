# Capstone Project 1: TIC TAC TOE Game

# -TIC TAC TOE Game

# This ia a two player game made within a Jupyter.

# To clear the screen between moves we import :

# from IPython.display import clear_output

# clear_output()

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print ('' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('  |   |')
    print ('------------')
    print ('' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('  |   |')
    print ('------------')
    print ('' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print ('  |   |')
    print ('------------')

    # print (board[7]+'|'+board[8]+'|'+board[9])
    # print (board[4]+'|'+board[5]+'|'+board[6])
    # print (board[1]+'|'+board[2]+'|'+board[3])
    test_board = ['#','X','O','X','O','X','O','X','O','X']
    display_board(test_board)
    # display_board(test_board)

    
    # Write a function that can take in a player input and assign their marker as 'X' or 'O'.
    def player_input():
    
    
    OUTPUT = (Player 1 marker, Player 2 marker)
    
    
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        
        return ('X','O')
    else:
        return ('O','X')
    
    player1_marker , player2_marker = player_input()
    player1_marker

    # a marker ('X' or 'O'), and a desired position (number 1-9) and assign it to the board.
    def place_marker(board, marker, position):
    board[position] = marker

    test_board   #display the modified board
    place_marker(test_board, '$',8)
    display_board(test_board)

    # Define the test board
# Let's say the winning condition is in the top row with 'X'
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']  # Index 0 is unused

# Define the winning mark
winning_mark = 'X'

# Function to check for a win
def Win_check(board, mark):
    # Check for a win in Tic Tac Toe
    if (board[7] == mark and board[8] == mark and board[9] == mark) or \
       (board[4] == mark and board[5] == mark and board[6] == mark) or \
       (board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    
    if (board[7] == mark and board[4] == mark and board[1] == mark) or \
       (board[8] == mark and board[5] == mark and board[2] == mark) or \
       (board[9] == mark and board[6] == mark and board[3] == mark):
        return True
    
    if (board[7] == mark and board[5] == mark and board[3] == mark) or \
       (board[9] == mark and board[5] == mark and board[1] == mark):
        return True
    
    return False

    # Run the function
    result = Win_check(test_board, winning_mark)
    print(result)  # This should print True
    winning_mark = 'X'    
    test_board       # it should return true

    def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def win_check(board, player):
   
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

test_board = [['X', 'O', 'X'],
              ['X', 'X', 'O'],
              ['O', 'X', 'O']]

# Display the board
display_board(test_board)

# Check for a win
if win_check(test_board, 'X'):
    print("Player X wins!")
else:
    print("Player X does not win yet.")  # for win check

display_board(test_board)
win_check(test_board,'X')

# function that uses the random module to randomly decide which player goes first
import random

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# the player if they want to play again and returns a boolean True if they do want to play again
def replay():
    choice = input("play again? Enter Yes or No")

    return choice == 'Yes'
# Use while loop
print('Welcome to Tic Tac Toe!')

while True:
    # PLAY THE GAME
    # Set everything up (Board, whose first, choose markers X,O)
    the_board = [''] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False
    
    # GAME PLAY
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:  # Player 2's turn
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'

    # Ask to replay
    if not replay():
        break

