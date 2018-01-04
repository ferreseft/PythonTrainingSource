# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 20:16:18 2018

@author: frank
"""

def print_board():
    print('| %s | %s | %s |') % (gameState[0], gameState[1], gameState[2])
    print('| %s | %s | %s |')% (gameState[3], gameState[4], gameState[5])
    print('| %s | %s | %s |')% (gameState[6], gameState[7], gameState[8])

def check_square(moved, gameStatus):
    if int(moved) > 8:
        return 0
    elif int(moved) < 0:
        return 0
    elif gameStatus[int(moved)] == ' ':
        return 1
    else:
        return 0
        
def check_winner(gameState):
    if gameState[0] == gameState[1] == gameState[2] and gameState[0] != ' ':
        win_state = 1
    elif gameState[3] == gameState[4] == gameState[5] and gameState[3] != ' ':
        win_state = 1
    elif gameState[6] == gameState[7] == gameState[8] and gameState[6] != ' ':
        win_state = 1
    elif gameState[0] == gameState[3] == gameState[6] and gameState[0] != ' ':
        win_state = 1
    elif gameState[1] == gameState[4] == gameState[7] and gameState[1] != ' ':
        win_state = 1
    elif gameState[2] == gameState[5] == gameState[8] and gameState[2] != ' ':
        win_state = 1
    elif gameState[0] == gameState[4] == gameState[8] and gameState[0] != ' ':
        win_state = 1
    elif gameState[2] == gameState[4] == gameState[6] and gameState[2] != ' ':
        win_state = 1
    else: 
        win_state = 0        
    return win_state
gameState = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = 0
current_round = 0
print_board()

while winner == 0:
    move_made = 0
    if current_round %2 == 0:
        while move_made == 0:
            move = raw_input("Player one pick a square ")
            if check_square(move, gameState):
                move_made = 1
                gameState[int(move)] = 'x'
            else:
                print('That square is not available.')
            won = check_winner(gameState)
            if check_winner(gameState) == 1:
                print('Congratulations player 1, you won')
                print_board()
                quit()
            else:
                print_board()
        
    else:
        while move_made == 0:
            move = raw_input("Player two pick a square ")
            if check_square(move, gameState):
                move_made = 1
                gameState[int(move)] = 'O'
            else:
                print("That square is not available.")
            if check_winner(gameState) == 1:
                print('Congratulations player 2, you won')
                print_board()
                quit()
            else:
                print_board()
        print_board()
    current_round +=1
         