import numpy as np

DIM = 8 #board dimension

black_pieces = [] #list of black piece objects
white_pieces = [] #list of white piece objects

class Piece:
    def __init__(self, team, type, position, ID):  # attributes of a piece
        self.team = int(team)  # black(1) or white(2)
        self.type = int(type)  # normal(3) or king(4); indepedent of how kings on board are called
        self.position = position  # location
        self.ID = ID #each piece needs ID

def board_setup(): #board matrix
    board = np.zeros((DIM,DIM))
    return board

def standard_board(board): #turn zero matrix board into conventional board
    #black piece (1) setup
    for r in range(3): #rows; range(3)=0,1,2
        if r % 2 == 0: #if even row (0,2)
            for x in range(DIM): #range(8) = 0 to 7
                if x % 2 != 0: #if odd column
                    board[r][x] = 1
        else: #odd row (1)
            for x in range(DIM):
                if x % 2 == 0: #if even column
                    board[r][x] = 1

    #white piece (2) setup
    for r in range(5, DIM): #rows; range (5,8) = 5,6,7 but ROWS 6,7,8
        if r % 2 != 0: #if odd row (5,7)
            for x in range(DIM): #range(8) = 0 to 7
                if x % 2 == 0: #if even column
                    board[r][x] = 2
        else: #even row (6)
            for x in range(DIM):
                if x % 2 != 0: #if odd column
                    board[r][x] = 2
    return board

def load_file():
    pass

def piece_to_object(board): #sep. from standard_board func. bc if board is loaded, then placement of pieces would be diff.

    Num_black = 0  #local
    Num_white = 0

    for r in range(DIM): #rows 0-7
        if r % 2 == 0: #rows 0,2,4,6
            for x in range(DIM): #columns 0-7
                if x % 2 != 0: #odd columns -> (even, odd) spaces
                    if board[r][x] == 1: #if black pawn piece
                        black_pieces.append(Piece(1, 3, [r,x], Num_black)) #assume all start pieces = normal piece
                        Num_black += 1
                    elif board[r][x] == 2: #if white pawn piece
                        white_pieces.append(Piece(2, 3, [r,x], Num_white))
                        Num_white +=1
                    elif board[r][x] == 3: #if black king piece
                        black_pieces.append(Piece(1, 4, [r,x], Num_black))
                        Num_white +=1
                    elif board[r][x] == 4: #if white king piece
                        white_pieces.append(Piece(2, 4, [r,x], Num_white))
                        Num_white +=1

        else: #rows 1,3,5,7
            for x in range(DIM):
                if x % 2 == 0: # even columns -> (odd, even) spaces
                    if board[r][x] == 1: #if black pawn piece
                        black_pieces.append(Piece(1, 3, [r,x], Num_black)) #assume all start pieces = normal piece
                        Num_black += 1
                    elif board[r][x] ==2: #if white pawn piece
                        white_pieces.append(Piece(2, 3, [r,x], Num_white))
                        Num_white += 1
                    elif board[r][x] == 3: #if black king piece
                        black_pieces.append(Piece(1, 4, [r,x], Num_black))
                        Num_white +=1
                    elif board[r][x] == 4: #if white king piece
                        white_pieces.append(Piece(2, 4, [r,x], Num_white))
                        Num_white +=1

    return Num_black, Num_white #black and white piece counters

def team_choice(): #team that user selects
    pass

