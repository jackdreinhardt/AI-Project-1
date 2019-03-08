import pygame
import sys

from square import Square
from robot import Robot

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
 
def ResetBoard():
    DrawBoardgameEdge()
    DrawBoardgame()
    DrawWalls()
    pygame.display.update()
    
def PlaceWalls():
    # Initialize board without walls
    board = [[Square(0,0,0,0,0) for j in range(boardSize)] for i in range(boardSize)]

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

def OccupiedSquares():
    for i in range(boardSize):
        for j in range (boardSize):
            board[i][j].occ = 0
    board[redRobo.curSy][redRobo.curSx].occ = 1
    board[blueRobo.curSy][blueRobo.curSx].occ = 1
    board[greenRobo.curSy][greenRobo.curSx].occ = 1
    board[yellowRobo.curSy][yellowRobo.curSx].occ = 1
    
    return board
    
def DetermineRobo(click):
    if click[0] > redRobo.curX and click[0] < redRobo.curX+30 and click[1] > redRobo.curY and click[1] < redRobo.curY+30:
        currentRobo = redRobo
        return currentRobo
    if click[0] > blueRobo.curX and click[0] < blueRobo.curX+30 and click[1] > blueRobo.curY and click[1] < blueRobo.curY+30:
        currentRobo = blueRobo
        return currentRobo
    if click[0] > greenRobo.curX and click[0] < greenRobo.curX+30 and click[1] > greenRobo.curY and click[1] < greenRobo.curY+30:
        currentRobo = greenRobo
        return currentRobo    
    if click[0] > yellowRobo.curX and click[0] < yellowRobo.curX+30 and click[1] > yellowRobo.curY and click[1] < yellowRobo.curY+30:
        currentRobo = yellowRobo
        return currentRobo
    
    return 0
    
def RoboMoves(currentRobo, key):
    if key == pygame.K_LEFT:
        while (board[currentRobo.curSy][currentRobo.curSx].west == 0):
            if (board[currentRobo.curSy][(currentRobo.curSx)-1].occ == 1):
                break
            currentRobo.curSx -= 1
            currentRobo.curX -= vel
    if key == pygame.K_RIGHT:
        while (board[currentRobo.curSy][currentRobo.curSx].east == 0):
            if (board[currentRobo.curSy][(currentRobo.curSx)+1].occ == 1):
                break
            currentRobo.curSx += 1
            currentRobo.curX += vel
    if key == pygame.K_UP:
        while (board[currentRobo.curSy][currentRobo.curSx].north == 0):
            if (board[(currentRobo.curSy)-1][currentRobo.curSx].occ == 1):
                break
            currentRobo.curSy -= 1
            currentRobo.curY -= vel
    if key == pygame.K_DOWN:
        while (board[currentRobo.curSy][currentRobo.curSx].south == 0):
            if (board[(currentRobo.curSy)+1][currentRobo.curSx].occ == 1):
                break
            currentRobo.curSy += 1
            currentRobo.curY += vel
             
    return currentRobo

def DrawRobots():
    ResetBoard()
    pygame.draw.rect(screen, blueRobo.colour, (blueRobo.curX,blueRobo.curY,30,30), 0)
    pygame.draw.rect(screen, redRobo.colour, (redRobo.curX,redRobo.curY,30,30), 0)
    pygame.draw.rect(screen, greenRobo.colour, (greenRobo.curX,greenRobo.curY,30,30), 0)
    pygame.draw.rect(screen, yellowRobo.colour, (yellowRobo.curX,yellowRobo.curY,30,30), 0)
    pygame.display.update()
            
## ----------------------------------------------------------    
# The Program # ---------------------------------------------

# Initalizes the robots
redRobo = Robot((255,0,0), 30, 30, 0, 0)
blueRobo = Robot((0,0,255), 30, 80, 0, 1)
greenRobo = Robot((0,255,0), 80, 30, 1, 0)
yellowRobo = Robot((255, 255, 0), 80, 80, 1, 1)
vel = 50

# Places walls on the board
board = PlaceWalls()

# Determines occupied squares
board = OccupiedSquares()

# Draw board and robots 
DrawRobots()

# MAIN LOOP
currentRobo = 0

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():                    
        if event.type == pygame.QUIT:  
            pygame.display.quit()                 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos  
            currentRobo = DetermineRobo(click)
        if event.type == pygame.KEYDOWN and currentRobo != 0:
            key = event.key
            RoboMove = RoboMoves(currentRobo, key)
            if RoboMove.colour == (255,0,0):
                redRobo = RoboMove
            elif RoboMove.colour == (0,0,255):
                blueRobo = RoboMove
            elif RoboMove.colour == (0,255,0):
                greenRobo = RoboMove
            elif RoboMove.colour == (255,255,0):
                yellowRobo = RoboMove
            DrawRobots()
            OccupiedSquares()
            
    pygame.display.update()
