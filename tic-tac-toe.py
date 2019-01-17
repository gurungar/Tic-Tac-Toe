from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[1].rjust(2)+'|'+board[2].rjust(2)+'|'+board[3].rjust(2))
    print(board[4].rjust(2)+'|'+board[5].rjust(2)+'|'+board[6].rjust(2))
    print(board[7].rjust(2)+'|'+board[8].rjust(2)+'|'+board[9].rjust(2))
    
def player_input():
    chosen = input("Player 1, Would you like to choose 'X' or 'O'? ")
    while chosen != 'X' and chosen != 'O':
        print("Wrong Input")
        chosen = input("Player 1, Would you like to choose 'X' or 'O'? ")
    
    player1 = chosen
    player2 = ''
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)
    
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    #check the horizontals
 
    if board[1:4] == [mark]*3 or board[4:7] == [mark]*3 or board[7:] == [mark]*3:
        return True
    #check the verticals
    elif list(board[1]+board[4]+board[7]) == [mark]*3 or list(board[2]+board[5]+board[8]) == [mark]*3 or list(board[3]+board[6]+board[9]) == [mark]*3:
        return True
    #Check the diagonals
    elif list(board[1]+board[5]+board[9]) == [mark]*3 or list(board[3]+board[5]+board[7]) == [mark]*3:
        return True
    else:
        return False



def choose_first():
    x = random.randint(1,2)
    if x == 1:
        print("Player 1 goes first")
        return x
    else:
        print("Player 2 goes first")
        return x
        
        
def space_check(board, position):
    if board[position] == '':
        return True
    else:
        return False


def full_board_check(board):
    if board.count('O') == 5 or board.count('X') == 5:
        return True
    else:
        return False
        
def player_choice(board):
    
    #Ask for players choice
    choose = int(input("Enter the spot: "))
    #Check if the slot is empty
    while space_check(board, choose) != True and choose < 1 and choose > 9:
        choose = int(input("Invalid Spot: Enter the spot: "))
    return choose        
       
       
       
def replay():
    
    play = input("Would you like to play?(Y/N)")
    while play != 'Y' and play != 'N':
        play = input("Would you like to play?(Y/N)")
        
    if play == 'Y':
        return True
    else:
        return False
        
        
        
print('Welcome to Tic Tac Toe!')

#while True:
while replay():
    # Set the game up here
    board = ['#','','','','','','','','',''] 
    
    #Display the empty board
    display_board(board)
    
    #Store the player symbol
    player1, player2 = player_input()
    
    #Helps 'mark' adjust from 'X' to 'O' and vice versa
    first_mark = ''
    if choose_first() == 1:
        first_mark = player1
    else:
        first_mark = player2
    
    #provides the position where the player wishes to draw
    position = player_choice(board)
    place_marker(board,first_mark,position)
    display_board(board)
    
    
    #while game_on:
    mark = first_mark #initiate mark variable
    while not win_check(board,mark): #Check to see if there is a winner
        #Turn 1
        if first_mark == 'X':
            mark = 'O'
        else:
            mark = 'X'
            
        position = player_choice(board)
        place_marker(board,mark,position)
        display_board(board)
      
        first_mark = mark
        
        if full_board_check(board):
            print("Draw")
            break;
    print("Game Over!")
            #pass
print("Thank you for playing!")
    #if not replay():
        #break
        
        
        
        
        
        
        
