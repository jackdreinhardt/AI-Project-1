import pygame
import sys
import numpy as np

from square import Square

pygame.init()

boardSize = 16
square = 50
edge = 20
wallthickness = 6
halfthickness = 2

windowSize = (square*boardSize + edge*2, square*boardSize + edge*2)
windowTitle = "Ricochet Robots"

screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption(windowTitle)

tile1 = (230, 245, 255)             
tile2 = (245, 255, 250)             
edgecol = (173, 216, 230)
black = (0,0,0)   
red = (255,0,0)

pygame.mouse.set_visible(1)      

def DrawBoardgameEdge():
    screen.fill(tile2)
    pygame.draw.rect(screen, edgecol, (0, 0, windowSize[0], edge), 0)
    pygame.draw.rect(screen, edgecol, (0, 0, edge, windowSize[0]), 0)
    pygame.draw.rect(screen, edgecol, (0, windowSize[0] - edge, windowSize[0], edge), 0)
    pygame.draw.rect(screen, edgecol, (windowSize[0] - edge, 0, edge, windowSize[0]), 0)
    
def DrawBoardgame():
    for j in range(0, 15, 2):
        for i in range(0, 15, 2):
            pygame.draw.rect(screen, tile1, (j*square + edge, i*square + (square + edge), square, square), 0)
    for j in range(0, 15, 2):
        for i in range(0, 15, 2):
            pygame.draw.rect(screen, tile1, (j*square + edge + square, i*square + edge, square, square), 0)
      
def DrawWalls():
    # Draw outer walls
    pygame.draw.rect(screen, black, (edge-halfthickness, edge-halfthickness, windowSize[0]-3/2*edge-halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge-halfthickness, edge-halfthickness, wallthickness, windowSize[0]-3/2*edge-halfthickness), 0)
    pygame.draw.rect(screen, black, (edge-halfthickness, windowSize[0]-edge, windowSize[0]-3/2*edge-halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (windowSize[0]-edge, edge-halfthickness, wallthickness, windowSize[0]-3/2*edge-halfthickness), 0)
    
    # Draw inner Square walls
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+7*square-halfthickness, 2*square, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+7*square-halfthickness, wallthickness, 2*square), 0)
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+9*square-halfthickness, 2*square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+9*square-halfthickness, edge+7*square-halfthickness, wallthickness, 2*square+2*halfthickness), 0)

    # Draw vertical walls
    pygame.draw.rect(screen, black, (edge+4*square-halfthickness, edge-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+11*square-halfthickness, edge-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+6*square-halfthickness, edge+1*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+12*square-halfthickness, edge+1*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+1*square-halfthickness, edge+2*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+14*square-halfthickness, edge+2*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+8*square-halfthickness, edge+3*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+4*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+10*square-halfthickness, edge+5*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+3*square-halfthickness, edge+6*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+12*square-halfthickness, edge+6*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+2*square-halfthickness, edge+9*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+5*square-halfthickness, edge+9*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+9*square-halfthickness, edge+10*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+13*square-halfthickness, edge+11*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+12*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+9*square-halfthickness, edge+13*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+2*square-halfthickness, edge+14*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+15*square-halfthickness, edge+14*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+6*square-halfthickness, edge+15*square-halfthickness, wallthickness, square+2*halfthickness), 0)
    pygame.draw.rect(screen, black, (edge+12*square-halfthickness, edge+15*square-halfthickness, wallthickness, square+2*halfthickness), 0)

    # Draw horizontal walls
    pygame.draw.rect(screen, black, (edge+5*square-halfthickness, edge+1*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+12*square-halfthickness, edge+1*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+1*square-halfthickness, edge+3*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+14*square-halfthickness, edge+3*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+0*square-halfthickness, edge+4*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+8*square-halfthickness, edge+4*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+6*square-halfthickness, edge+5*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+15*square-halfthickness, edge+5*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+9*square-halfthickness, edge+6*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+11*square-halfthickness, edge+6*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+2*square-halfthickness, edge+7*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+1*square-halfthickness, edge+9*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+5*square-halfthickness, edge+9*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+15*square-halfthickness, edge+10*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+0*square-halfthickness, edge+11*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+8*square-halfthickness, edge+11*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+13*square-halfthickness, edge+11*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+6*square-halfthickness, edge+13*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+9*square-halfthickness, edge+14*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+14*square-halfthickness, edge+14*square-halfthickness, square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+2*square-halfthickness, edge+15*square-halfthickness, square+2*halfthickness, wallthickness), 0)
 
def ResetGame():
    DrawBoardgameEdge()
    DrawBoardgame()
    DrawWalls()
    pygame.display.update()
    
def PlaceWalls():
    # Initialize board without walls
    board = [[Square(0,0,0,0) for j in range(boardSize)] for i in range(boardSize)]

    # Add outer walls
    for i in range(boardSize):
        board[0][i].north = 1
        board[15][i].south = 1
        board[i][0].west = 1
        board[i][15].east = 1
    
    # Add inner square walls
    board[6][7].south = 1
    board[6][8].south = 1
    board[7][6].east = 1    
    board[8][6].east = 1
    board[7][9].west = 1
    board[8][9].west = 1
    board[9][7].north = 1
    board[9][8].north = 1
    
    # Add vertical walls
    board[0][3].east = 1
    board[0][4].west = 1
    board[0][10].east = 1
    board[0][11].west = 1
    board[1][5].east = 1
    board[1][6].west = 1
    board[1][11].east = 1
    board[1][12].west = 1
    board[2][0].east = 1
    board[2][1].west = 1
    board[2][13].east = 1
    board[2][14].west = 1
    board[3][7].east = 1
    board[3][8].west = 1
    board[4][6].east = 1
    board[4][7].west = 1
    board[5][9].east = 1
    board[5][10].west = 1
    board[6][2].east = 1
    board[6][3].west = 1
    board[6][11].east = 1
    board[6][12].west = 1
    board[9][1].east = 1
    board[9][2].west = 1
    board[9][4].east = 1
    board[9][5].west = 1
    board[10][8].east = 1
    board[10][9].west = 1
    board[11][12].east = 1
    board[11][13].west = 1
    board[12][6].east = 1
    board[12][7].west = 1
    board[13][8].east = 1
    board[13][9].west = 1
    board[14][1].east = 1
    board[14][2].west = 1
    board[14][14].east = 1
    board[14][15].west = 1
    board[15][5].east = 1
    board[15][6].west = 1
    board[15][11].east = 1
    board[15][12].west = 1
    
    # Add horizontal walls
    board[0][5].south = 1
    board[1][5].north = 1
    board[0][12].south = 1
    board[1][12].north = 1
    board[2][1].south = 1
    board[3][1].north = 1
    board[2][14].south = 1
    board[3][14].north = 1
    board[3][0].south = 1
    board[4][0].north = 1
    board[3][8].south = 1
    board[4][8].north = 1
    board[4][6].south = 1
    board[5][6].north = 1
    board[4][15].south = 1
    board[5][15].north = 1
    board[5][9].south = 1
    board[6][9].north = 1
    board[5][11].south = 1
    board[6][11].north = 1
    board[6][2].south = 1
    board[7][2].north = 1
    board[8][1].south = 1
    board[9][1].north = 1
    board[8][5].south = 1
    board[9][5].north = 1
    board[9][15].south = 1
    board[10][15].north = 1
    board[10][0].south = 1
    board[11][0].north = 1
    board[10][8].south = 1
    board[11][8].north = 1
    board[10][13].south = 1
    board[11][13].north = 1
    board[12][6].south = 1
    board[13][6].north = 1    
    board[13][9].south = 1
    board[14][9].north = 1 
    board[13][14].south = 1
    board[14][14].north = 1
    board[14][2].south = 1
    board[15][2].north = 1 
    
    return board
    
    
## ----------------------------------------------------------    
# The Program # ---------------------------------------------

# Initalizes red robot
x = 30 
y = 30
vel = 50
curX = 0 
curY = 0

# Places Walls on the board
board = PlaceWalls()

# MAIN LOOP
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():                    
        if event.type == pygame.QUIT:  
            pygame.display.quit()                 
            pygame.quit()
            sys.exit()

    ResetGame()
    pygame.draw.rect(screen, red, (x,y,30,30), 0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        while board[curY][curX].west == 0:
            curX -= 1
            x -= vel
    if keys[pygame.K_RIGHT]:
        while board[curY][curX].east == 0:
            curX += 1
            x += vel
    if keys[pygame.K_UP]:
        while board[curY][curX].north == 0:
            curY -= 1
            y -= vel
    if keys[pygame.K_DOWN]:
        while board[curY][curX].south == 0:
            curY += 1
            y += vel    

    
    pygame.display.update()
