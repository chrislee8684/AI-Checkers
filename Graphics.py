import pygame

pygame.init() #must initialize pygame

DIM = 8
LIGHT = (219,176,127)
DARK = (140,88,28)
BLACK = (0,0,0)
WHITE = (255,255,255)

Tile_side = 100 #each tile = 100 pixels
width = DIM * Tile_side
height = (DIM+1) *Tile_side #extra layer for options
size = (width,height) #pygame takes in size as tuple
surface=pygame.display.set_mode(size) #creates a surface object rep. by graphics

def static_board(black_pieces, white_pieces):
    for r in range(DIM):  #for background tiles
        if r % 2 == 0:  # if even row: 0,2,4,6
            for x in range(DIM):  # columns
                if x % 2 != 0:  # if odd column
                    pygame.draw.rect(surface, DARK, (r*Tile_side, x*Tile_side, Tile_side, Tile_side))
                else: pygame.draw.rect(surface, LIGHT, (r*Tile_side, x*Tile_side, Tile_side, Tile_side))
        else:  # odd rows: 1,3,5,7
            for x in range(DIM):
                if x % 2 == 0:  # if even column
                    pygame.draw.rect(surface, DARK, (r*Tile_side, x*Tile_side, Tile_side, Tile_side))
                else:
                    pygame.draw.rect(surface, LIGHT, (r * Tile_side, x * Tile_side, Tile_side, Tile_side))

    for piece in black_pieces:
        pygame.draw.circle(surface, BLACK, (piece.position[1]*Tile_side + Tile_side/2, piece.position[0]*Tile_side + Tile_side/2), Tile_side/3) #x=column, y=row

    for piece in white_pieces:
        pygame.draw.circle(surface, WHITE, (piece.position[1]*Tile_side + Tile_side/2, piece.position[0]*Tile_side + Tile_side/2), Tile_side/3)

    return None