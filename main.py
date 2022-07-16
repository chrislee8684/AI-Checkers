'''
Pseudo-code

Surface:
    - load game from file
    - ASCII interface
    - func to display board
    - time limit

Structural:
    - data structure (produce searched game space as ASCII rep.)
    - legal moves func.
    - func. to apply move
    - minimax algo. func. (w. alpha-beta pruning)
    - heuristic func.


For player vs computer:
(Before Game)
Command: Who would like to go first? (Player or Computer)
Command: What is the time limit for each turn?
Command: Would you like to load game from file?
(load game from file)
(board is displayed thru ASCII interface)

(Game Starts)
(assume comp goes first)
Comp -> uses heuristic to rank scenarios (based on legal moves) x depths ahead, minimax assumes player makes best move and applies best move (a-B pruning cuts off non-optimal branch), ASCII tree rep. generated
     -> (if all moves ranked same, choose randomly)
Player -> shown legal moves, selects one move, move is applied to board
(following repeats: keep track of score)

*For computer's every turn, a new search tree is generated (bc need to see best option for each scenario (can't assume player will always make best move)

(Game Ends)
when a player has nothing left
Command: ... has won. (Display final score)
'''
import rectangle as rectangle

from Initialize import * #import everything from game_setup
from Graphics import *
from Backend import *
import pygame
import sys

pygame.init() #must initialize pygame

# board = standard_board(board_setup()) #initialize board
# print(board) #show board
# Num_black, Num_white = piece_to_object(board) #save pieces as objects; altering list thru func. and returns are independent of each other

# static_board(black_pieces,white_pieces)
pygame.display.update() #update changes to surface

practice_board = np.zeros((DIM,DIM))
practice_board[0][7]=2
practice_board[1][6]=1
practice_board[2][1]=2
practice_board[2][3]=1
practice_board[2][5]=1
practice_board[2][7]=2
practice_board[3][2]=4
practice_board[4][1]=4
practice_board[4][5]=1
practice_board[7][2]=2

# practice_board[1][2]=1 #test apply move

print(practice_board)

Num_black, Num_white = piece_to_object(practice_board)

for piece in white_pieces:
    print(piece, piece.position)

print('\n')
for piece in black_pieces:
    print(piece, piece.position)

for piece in white_pieces:
     print(piece.position)
     print(piece.type)
     print(piece.team)
     list = legal_moves(practice_board,piece)
     print("final_destination - opp_pieces")
     for x in list:
        print(x.final_location,'-',x.opp_pieces)
     print("\n")

#apply_move(practice_board, white_pieces[1], list[1], black_pieces, white_pieces, 2)

print(practice_board)

for piece in white_pieces:
    print(piece, piece.position)

print('\n')
for piece in black_pieces:
    print(piece, piece.position)



#game_type =2  #initilize type of game
turn = 2 #initialize turn (0 vs 1)
Game_not_over = True #game loop condition



while turn != 0:
    turn=int(input("Who would like to play first? Player 1 (press 0) pr player 2 (press 1)?"))

while Game_not_over:
    for event in pygame.event.get(): #event = motion instance; loop allows screen to contiously be on screen (bc each event = instance)
        if event.type == pygame.QUIT: #if user x's out
            sys.exit() #exit system properly
        print(pygame.mouse.get_pos())

    #player 1 move
    if turn == 0:
        print("Player 1's turn")

    #player 2 move
    else:
        pass

    turn +=1
    turn = turn % 2 #keeps repeating turn = 0 vs 1





