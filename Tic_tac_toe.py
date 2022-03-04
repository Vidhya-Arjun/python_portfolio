import random

# Code for Setting up game's layout

def display_board(board): # board is a list with 3 X 3 board layout
    print("  |  |")
    print(" " +  board[7]  +  "| "  +  board[8]  + "| " +  board[9])
    print("  |  |")
    print("----------")
    print(" " + board[4]   +  "| "  + board[5]   + "| " + board[6])
    print("  |  |")
    print("----------")
    print(" " + board[1]   +  "| "  + board[2]   + "|" + board[3])
    print("  |  |")


# A function that helps the player to choose  their input as "X" or "O"

def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"): 
        marker = input("Choose you place marker as 'X' or 'O' : ").upper()
        
    if marker == "X" :
        return ('X','O')
    else:
        return('O','X')

# place_maker funtion marks the player's value in board

def place_marker(board,marker,position):
    board[position] = marker

# Game's logic is defined here. It decides the game is won or tie 
def win_check(board, mark):
    if board[7] == board[8] == board [9] == mark:
        return True
    elif board[4] == board[5] == board [6] == mark:
        return True
    elif board[1] == board[2] == board [3] == mark:
        return True
    elif board[7] == board[4] == board [1] == mark:
        return True
    elif board[8] == board[5] == board [2] == mark:
        return True
    elif board[9] == board[6] == board [3] == mark:
        return True
    elif board[7] == board[5] == board [3] == mark:
        return True
    elif board[9] == board[5] == board [1] == mark:
        return True
    else:
        return False   

# Since the game needs two player. using random function decides turn of the player

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"       

#To check whether empty space is available for player to play

def space_check(board, position):
     if board[position] == "":
        return True
     else:
        return False         

#TO check the board is full for next move

def full_board_check(board):
    for i in range(len(board)):
        return board[i] != ""        