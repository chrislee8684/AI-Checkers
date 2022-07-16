from copy import deepcopy #to copy objects indepedently

DIM = 8

class legal_move: #one specific legal move
    def __init__(self, final_location, opp_pieces):
        self.final_location = final_location #empty location that piece will go to
        self.opp_pieces = opp_pieces #list of opp pieces that will be removed by legal move

def append_upper_right(board, piece, legal_locations): #checks and if good, appends diag. spaces + allows recursion if opponent\

    if board[piece.position[0] - 1][piece.position[1] + 1] == 0:  # upper right diag.; #1
        open_location = [piece.position[0] - 1,piece.position[1] + 1]
        legal_locations.append(legal_move(open_location,[]))
    else:
        recursion(board, piece, legal_locations, 1)

def append_upper_left(board, piece, legal_locations):
    if board[piece.position[0] - 1][piece.position[1] - 1] == 0:  # upper left diag.; #2
        open_location = [piece.position[0] - 1,piece.position[1] - 1]
        legal_locations.append(legal_move(open_location,[]))
    else:
        recursion(board, piece, legal_locations, 2)

def append_lower_right(board, piece, legal_locations):
    if board[piece.position[0] + 1][piece.position[1] + 1] == 0:  # lower right diag.; #3
        open_location = [piece.position[0] + 1,piece.position[1] + 1]
        legal_locations.append(legal_move(open_location,[]))
    else:
        recursion(board, piece, legal_locations, 3)

def append_lower_left(board, piece, legal_locations):
    print(piece.position[0], piece.position[1])
    if board[piece.position[0] + 1][piece.position[1] - 1] == 0:  # lower left diag.; #4
        open_location = [piece.position[0] + 1,piece.position[1] - 1]
        legal_locations.append(legal_move(open_location,[]))
    else:
        recursion(board, piece, legal_locations, 4)

def recursion(board, piece, legal_locations, diag_drxn): #diag_drxn keeps track of direction the move came from; 1 = upper right, 2 = upper left, 3 = lower right, 4 = lower left
    if diag_drxn==1: #upper right
        if piece.position[1]<6 and 1<piece.position[0]:  # recursion index limiation
            if board[piece.position[0] - 1][piece.position[1] + 1] % 2 != board[piece.position[0]][piece.position[1]] % 2:  # upper right diag.= opp.
                if board[piece.position[0] - 2][piece.position[1] + 2] == 0:  # empty space behind opp.
                    final_destination = [piece.position[0] - 2,piece.position[1] + 2]
                    opp_location = [piece.position[0] - 1,piece.position[1] + 1]
                    legal_locations.append(legal_move(final_destination, opp_location))
                    copy = deepcopy(piece) #copy b/c necc. to keep track of new positions during recursion
                    copy.position[0]=piece.position[0] - 2
                    copy.position[1]=piece.position[1] + 2
                    if piece.type == 4: #king
                            recursion(board, copy,legal_locations, 1)
                            recursion(board, copy,legal_locations, 2)
                            recursion(board, copy,legal_locations, 3)
                    elif piece.type == 3 and piece.team == 2: #white pawn; goes up (not applic. to black pawn)
                            recursion(board, copy,legal_locations, 1)
                            recursion(board, copy,legal_locations, 2)

    elif diag_drxn==2: #upper left
        if 1<piece.position[1] and 1<piece.position[0]:  # recursion index limiation
            if board[piece.position[0] - 1][piece.position[1] - 1] % 2 != board[piece.position[0]][piece.position[1]] % 2:  # upper left diag.= opp.
                if board[piece.position[0] - 2][piece.position[1] - 2] == 0:  # empty space behind opp.
                    final_destination = [piece.position[0] - 2, piece.position[1] - 2]
                    opp_location = [piece.position[0] - 1, piece.position[1] - 1]
                    legal_locations.append(legal_move(final_destination, opp_location))
                    copy = deepcopy(piece) # copy b/c necc. to keep track of new positions during recursion
                    copy.position[0] = piece.position[0] - 2
                    copy.position[1] = piece.position[1] - 2
                    if piece.type == 4: #king
                            recursion(board, copy,legal_locations, 1)
                            recursion(board, copy,legal_locations, 2)
                            recursion(board, copy,legal_locations, 4)
                    elif piece.type == 3 and piece.team == 2:  # white pawn; goes up (not applic. to black pawn)
                            recursion(board, copy,legal_locations, 1)
                            recursion(board, copy,legal_locations, 2)

    elif diag_drxn==3: #lower right
        if piece.position[1]<6 and piece.position[0]<6: #recursion index limiation
            if board[piece.position[0] + 1][piece.position[1] + 1] % 2 != board[piece.position[0]][piece.position[1]] % 2:  # lower right diag.= opp.
                if board[piece.position[0] + 2][piece.position[1] + 2] == 0:  # empty space behind opp.
                    final_destination = [piece.position[0] + 2, piece.position[1] + 2]
                    opp_location = [piece.position[0] + 1, piece.position[1] + 1]
                    legal_locations.append(legal_move(final_destination, opp_location))
                    copy = deepcopy(piece)  # copy b/c necc. to keep track of new positions during recursion
                    copy.position[0] = piece.position[0] + 2
                    copy.position[1] = piece.position[1] + 2
                    if piece.type == 4: #king
                            recursion(board, copy, legal_locations, 1)
                            recursion(board, copy, legal_locations, 3)
                            recursion(board, copy, legal_locations, 4)
                    elif piece.type == 3 and piece.team == 1:  # black pawn; goes down (not applic. to white pawn)
                            recursion(board, copy, legal_locations, 3)
                            recursion(board, copy, legal_locations, 4)

    elif diag_drxn==4: #lower left
        if 1<piece.position[1] and piece.position[0]<6: #recursion index limiation
            if board[piece.position[0] + 1][piece.position[1] - 1] % 2 != board[piece.position[0]][piece.position[1]] % 2:  # lower left diag.= opp.
                if board[piece.position[0] + 2][piece.position[1] - 2] == 0:  # empty space behind opp.
                    final_destination = [piece.position[0] + 2, piece.position[1] - 2]
                    opp_location = [piece.position[0] + 1, piece.position[1] - 1]
                    legal_locations.append(legal_move(final_destination, opp_location))
                    copy = deepcopy(piece) # copy b/c necc. to keep track of new positions during recursion
                    copy.position[0] = piece.position[0] + 2
                    copy.position[1] = piece.position[1] - 2
                    if piece.type == 4: #king
                            recursion(board, copy, legal_locations, 3)
                            recursion(board, copy, legal_locations, 4)
                            recursion(board, copy, legal_locations, 2)
                    elif piece.type == 3 and piece.team == 1:  # black pawn; goes down (not applic. to white pawn)
                            recursion(board, copy, legal_locations, 3)
                            recursion(board, copy, legal_locations, 4)

def legal_moves(board, piece): #iterates through list of pieces, sees which pieces can move, and shows where each piece can move

    legal_locations = [] #will return empty list if not legal piece

    if piece.type ==4: #king; same for both black and white
        if 0<piece.position[0]<DIM-1: # middle rows
            if piece.position[1]==0: #checking leftmost column (2 max legal moves)
                append_upper_right(board, piece, legal_locations)
                append_lower_right(board, piece, legal_locations)
            if 0<piece.position[1]<DIM-1: #checking middle columns(section) (4 max legal moves)
                append_upper_right(board, piece, legal_locations)
                append_lower_right(board, piece, legal_locations)
                append_upper_left(board, piece, legal_locations)
                append_lower_left(board, piece, legal_locations)
            if piece.position[1] ==DIM-1: #checking rightmost column (2 max legal moves)
                append_upper_left(board, piece, legal_locations)
                append_lower_left(board, piece, legal_locations)
        elif piece.position[0] == 0: #top row
            if 0<piece.position[1]<DIM-1: #checking middle columns (2 max legal moves)
                append_lower_left(board, piece, legal_locations)
                append_lower_right(board, piece, legal_locations)
            if piece.position[1] == DIM-1: #checking upper right corner (1 max legal move)
                append_lower_left(board, piece, legal_locations)
        elif piece.position[0] == DIM-1: #bottom row
            if 0<piece.position[1]<DIM-1: #middle columns (2 max legal moves)
                append_upper_left(board, piece, legal_locations)
                append_upper_right(board, piece, legal_locations)
            if piece.position[1] == 0: #checking lower left corner (1 legal move)
                append_upper_right(board, piece, legal_locations)

    if piece.team == 1: #for black team pawn; goes down
        if piece.type == 3 and piece.position[0]<DIM-1: #if pawn and row limit
            if piece.position[1] == 0: #accounts for leftmost piece
                append_lower_right(board, piece, legal_locations)
            if 0 < piece.position[1]<DIM-1: #accounts for middle pieces
                append_lower_left(board, piece, legal_locations)
                append_lower_right(board, piece, legal_locations)
            if piece.position[1] == DIM-1: #accounts for rightmost piece
                append_lower_left(board, piece, legal_locations)

    if piece.team == 2: #for white team pawn; goes up
        if piece.type == 3 and 0<piece.position[0]: #if pawn
            if piece.position[1] == 0: #accounts for leftmost piece
                append_upper_right(board, piece, legal_locations)
            if 0 < piece.position[1]<DIM-1: #accounts for middle pieces
                append_upper_left(board, piece, legal_locations)
                append_upper_right(board, piece, legal_locations)
            if piece.position[1] == DIM-1: #accounts for rightmost piece
                append_upper_left(board, piece, legal_locations)

    final_legal_moves = refine_legal_moves(legal_locations)

    return final_legal_moves

def refine_legal_moves(legal_locations): #takes in legal_moves list and appends opp. pieces if recursion occurs
    refined_legal_moves_list = []
    temp_list = [] #temp list to hold in opp_pieces


    size = len(legal_locations)

    for x in range(size):
        if legal_locations[x].opp_pieces==[]: #if move = empty space
            refined_legal_moves_list.append(legal_locations[x])
        elif legal_locations[x].opp_pieces!=[]: #if opp. piece
            if legal_locations[x-1].opp_pieces!=[] and 0<x: #if prev piece also has opp. piece, append prev opp list
                legal_locations[x].opp_pieces.extend(legal_locations[x].opp_pieces)
                refined_legal_moves_list.append(legal_locations[x])
            else: #if only one opponent
                temp_list.clear()
                refined_legal_moves_list.append(legal_locations[x])

#work on 2 things: extend lsit with location being [x] and nested loop so check if within neighboring distance to append

    return refined_legal_moves_list


def apply_move(board, piece, legal_move, black_pieces, white_pieces, team_turn): #applies a specific legal move from legal_moves list for a spec. piece
    if legal_move.opp_pieces == []: #if no opp_pieces
        board[legal_move.final_location[0]][legal_move.final_location[1]] = board[piece.position[0]][piece.position[1]] #update board: final location gets updated w/ piece #
        board[piece.position[0]][piece.position[1]] = 0 #update board: prev location can only beocome empty
        piece.position = legal_move.final_location #update piece: position attribute updated

    else: #there are opp. pieces
        board[legal_move.final_location[0]][legal_move.final_location[1]] = board[piece.position[0]][piece.position[1]]  #same as if statemnt (switch current and final postion #'s)
        board[piece.position[0]][piece.position[1]] = 0
        piece.position = legal_move.final_location

        if team_turn == 1: #black team's turn
            for white_piece in white_pieces:
                if white_piece.position == legal_move.opp_pieces:
                    board[white_piece.position[0]][white_piece.position[1]] = 0 #update board: opponent becomes zero
                    white_pieces.remove(white_piece) #take out white piece from list
        elif team_turn ==2: #white team's turn
            for black_piece in black_pieces:
                if black_piece.position == legal_move.opp_pieces:
                    board[black_piece.position[0]][black_piece.position[1]] = 0  # update board: opponent becomes zero
                    black_pieces.remove(black_piece)  # take out black piece from list


def minimax(): #minimax algo for AI
    pass

def Eval(): #evalatues board and returns score
    pass

def is_game_over(): #checks if game is over
    pass

def is_king(): #checks if pawn turned into king
    pass

