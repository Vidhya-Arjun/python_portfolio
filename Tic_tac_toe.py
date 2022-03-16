import random

# Code for Setting up game's layout

def display_board(board): # board is a list with 3 X 3 board layout
    print("  |    |")
    print(" " +  board[7]  +  " | "  +  board[8]  + " | " +  board[9])
    print("  |    |")
    print("----------")
    print(" " + board[4]   +  " | "  + board[5]   + " | " + board[6])
    print("  |    |")
    print("----------")
    print(" " + board[1]   +  " | "  + board[2]   + " | " + board[3])
    print("  |    |")


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
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True         

# A function that offers the user to place their marker in preferable position
def player_choice(board):
    position = 0
    

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):    
        position = int(input("Enter the position where the your marker to be placed, ranges between 1 and 9: "))
        space_check_value = space_check(board,position)
        print(space_check_value)        
    return position        

#Replay check , to ask the user: is he interested in playing the game again

def replay():
    replay_check = input("DO you want play again: if so press y else n :")
    return replay_check == 'y'

    print("\t\t\t\t Welcome to Tic-Tac-Toe game")

while True:
    
    # intializing the board for game
    
    intialise_board = [''] * 10
    print(intialise_board)
    
    # deciding which player to start the game
    
    player_one , player_two = player_input()
    
    print(player_one, player_two)
   
    # decision on whose turn
    
    turn = choose_first()
    
    #prompting the user to start the game 
    prompt_start = input("Are you ready to play ? Enter y or n : ")
    
    if prompt_start.lower()[0] == 'y':
        prompt_start = True
    else:
        prompt_start = False
        
    print("turn" , turn)
    print("check player_one" , player_one)    
      
    #Game starts
    while prompt_start:
        if turn == "Player 1":
            display_board(intialise_board)
            position = player_choice(intialise_board)
            print(position)
            place_marker(intialise_board,player_one,position)
            
            if win_check(intialise_board,player_one):
                display_board(intialise_board)
                print("Congratulation player 1 you won")
                prompt_start = False
            else:
                if full_board_check(intialise_board):
                    display_board(intialise_board)
                    print("Game is draw")
                    break
                
                else:
                    turn = "Player 2"
                    print("else turn = Player 2")
      
    # Game turn for player 2
        else:
        
            display_board(intialise_board)
            position = player_choice(intialise_board)
            place_marker(intialise_board,player_two,position)
            
            if win_check(intialise_board,player_two): 
                display_board(intialise_board)
                print("Congratulation Player 2 you won")
                prompt_start = False
            else:
                if full_board_check(intialise_board):
                    display_board(intialise_board)
                    print("Game is draw")
                    break
                
                else:
                    turn = "Player 1"

   # replay check point                 
    if not replay():
        break
