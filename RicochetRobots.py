import pygame
import sys
import random

from square import Square
from robot import Robot

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 15)

# Define the required variables for the boardgame
boardSize = 16
square = 50
edge = 20
wallthickness = 6
halfthickness = 2

windowSize = (square*boardSize + edge*2, square*boardSize + edge*2)
windowTitle = "Ricochet Robots"

screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption(windowTitle)

# Define the required colours for the boardgame 
tile1 = (230, 245, 255)             
tile2 = (245, 255, 250)             
edgecol = (173, 216, 230)
black = (0,0,0)
grey = (100,100,100)

# Define the required colours for the robots and the targets
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)   

pygame.mouse.set_visible(1)      

# Draws the boardgame edge on the screen
def DrawBoardgameEdge():
    screen.fill(tile2)
    pygame.draw.rect(screen, edgecol, (0, 0, windowSize[0], edge), 0)
    pygame.draw.rect(screen, edgecol, (0, 0, edge, windowSize[0]), 0)
    pygame.draw.rect(screen, edgecol, (0, windowSize[0] - edge, windowSize[0], edge), 0)
    pygame.draw.rect(screen, edgecol, (windowSize[0] - edge, 0, edge, windowSize[0]), 0)
    
# Draws the chess-board pattern on the screen
def DrawBoardgame():
    for j in range(0, 15, 2):
        for i in range(0, 15, 2):
            pygame.draw.rect(screen, tile1, (j*square + edge, i*square + (square + edge), square, square), 0)
    for j in range(0, 15, 2):
        for i in range(0, 15, 2):
            pygame.draw.rect(screen, tile1, (j*square + edge + square, i*square + edge, square, square), 0)
# =============================================================================
#     # Buttons to reset the game and spawn a new target
#     pygame.draw.rect(screen, grey, (7*square + edge + 8, 7*square + edge + 8, 84, 34), 0)
#     pygame.draw.rect(screen, grey, (7*square + edge + 8, 8*square + edge + 8, 84, 34), 0)
#     textNewTarget = myfont.render('New Target', False, (255,255,255))
#     screen.blit(textNewTarget,(7*square + edge + 11, 7*square + edge + 12))
#     textTryAgain = myfont.render('Try Again', False, (255,255,255))
#     screen.blit(textTryAgain,(7*square + edge + 11, 8*square + edge + 12))
# =============================================================================
      
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
    DrawTarget()
    pygame.display.update()
    
def PlaceWalls():
    # Initialize board without walls (1-4); no square is currently occupied (5); no target is placed(6)
    board = [[Square(0,0,0,0,0,0) for j in range(boardSize)] for i in range(boardSize)]

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

def PlaceTarget():
    for i in range(boardSize):
        for j in range (boardSize):
            board[i][j].tar = 0
    rand = random.choice(range(16))
    # Blue targets
    if rand == 0:
        board[1][5].tar = 1
    if rand == 1:
        board[5][9].tar = 1
    if rand == 2:
        board[9][5].tar = 1
    if rand == 3:
        board[11][13].tar = 1
    #Red targets
    if rand == 4:
        board[2][1].tar = 2
    if rand == 5:
        board[2][14].tar = 2
    if rand == 6:
        board[12][6].tar = 2
    if rand == 7:
        board[14][14].tar = 2
    # Green targets
    if rand == 8:
        board[1][12].tar = 3
    if rand == 9:
        board[6][2].tar = 3
    if rand == 10:
        board[13][9].tar = 3
    if rand == 11:
        board[14][2].tar = 3
    # Yellow targets
    if rand == 12:
        board[4][6].tar = 4
    if rand == 13:
        board[6][11].tar = 4
    if rand == 14:
        board[9][1].tar = 4
    if rand == 15:
        board[10][8].tar = 4
    
    return board
# =============================================================================
# # List of targets
#     Be careful: tuple (x,y) is not (rows, coloumns) but (x,y) coordinates 
#     with the center of the coordinate system in the top left corner.
#     (the x-axis is the horizontal axis of the board)
#     blue targets: (5,1) (9,5) (5,9) (13,11)
#     red targets: (1,2) (14,2) (6,12) (14,14)
#     green targets: (12,1) (2,6) (9,13) (2,14)
#     yellow targets: (6,4) (11,6) (1,9) (8,10)
#     colourful target: (8,3)
# =============================================================================

# For each square determines if the square is currently occupied
def OccupiedSquares():
    for i in range(boardSize):
        for j in range (boardSize):
            board[i][j].occ = 0
    board[blueRobo.curSy][blueRobo.curSx].occ = 1
    board[redRobo.curSy][redRobo.curSx].occ = 2
    board[greenRobo.curSy][greenRobo.curSx].occ = 3
    board[yellowRobo.curSy][yellowRobo.curSx].occ = 4
    
    return board
    
# Determines which robot was selected by the player. Returns '0' if no robot was selected
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
# =============================================================================
#     if click[0] > 378 and click[0] < 462 and click[1] > 378 and click[1] < 412:
#         board = boardBackup
#         DrawRobots()
#         OccupiedSquares()
# =============================================================================

    return 0
    
# Moves the selected robot in the desired position until the robots hits a wall or another robot
def RoboMoves(currentRobo, key):
    if key == pygame.K_LEFT:
        while (board[currentRobo.curSy][currentRobo.curSx].west == 0):
            if (board[currentRobo.curSy][(currentRobo.curSx)-1].occ != 0):
                break
            currentRobo.curSx -= 1
            currentRobo.curX -= vel
    if key == pygame.K_RIGHT:
        while (board[currentRobo.curSy][currentRobo.curSx].east == 0):
            if (board[currentRobo.curSy][(currentRobo.curSx)+1].occ != 0):
                break
            currentRobo.curSx += 1
            currentRobo.curX += vel
    if key == pygame.K_UP:
        while (board[currentRobo.curSy][currentRobo.curSx].north == 0):
            if (board[(currentRobo.curSy)-1][currentRobo.curSx].occ != 0):
                break
            currentRobo.curSy -= 1
            currentRobo.curY -= vel
    if key == pygame.K_DOWN:
        while (board[currentRobo.curSy][currentRobo.curSx].south == 0):
            if (board[(currentRobo.curSy)+1][currentRobo.curSx].occ != 0):
                break
            currentRobo.curSy += 1
            currentRobo.curY += vel
             
    return currentRobo

# Draws the current position of all robots on the board
def DrawRobots():
    ResetBoard()
    pygame.draw.rect(screen, blue, (blueRobo.curX,blueRobo.curY,30,30), 0)
    pygame.draw.rect(screen, red, (redRobo.curX,redRobo.curY,30,30), 0)
    pygame.draw.rect(screen, green, (greenRobo.curX,greenRobo.curY,30,30), 0)
    pygame.draw.rect(screen, yellow, (yellowRobo.curX,yellowRobo.curY,30,30), 0)
    pygame.display.update()
          
def DrawTarget():
    for i in range(boardSize):
        for j in range (boardSize):
            if board[i][j].tar != 0:
                if board[i][j].tar == 1:
                    pygame.draw.circle(screen, blue, (edge+j*square+25, edge+i*square+25), 10, 0)
                if board[i][j].tar == 2:
                    pygame.draw.circle(screen, red, (edge+j*square+25, edge+i*square+25), 10, 0)
                if board[i][j].tar == 3:
                    pygame.draw.circle(screen, green, (edge+j*square+25, edge+i*square+25), 10, 0)
                if board[i][j].tar == 4:
                    pygame.draw.circle(screen, yellow, (edge+j*square+25, edge+i*square+25), 10, 0)


## ----------------------------------------------------------    
# The Program # ---------------------------------------------

# Initalizes the robots
redRobo = Robot(red, 30+13*square, 30+12*square, 13, 12)
blueRobo = Robot(blue, 30+5*square, 30+11*square, 5, 11)
greenRobo = Robot(green, 30+3*square, 30+6*square, 3, 6)
yellowRobo = Robot(yellow, 30+13*square, 30, 13, 0)
vel = 50

# Places walls on the board
board = PlaceWalls()

# Determines occupied squares
board = OccupiedSquares()

# Places the target on the board
board = PlaceTarget()

# Draw board and robots 
DrawRobots()

# MAIN LOOP
currentRobo = 0
boardBackup = board

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
            if RoboMove.colour == red:
                redRobo = RoboMove
            elif RoboMove.colour == blue:
                blueRobo = RoboMove
            elif RoboMove.colour == green:
                greenRobo = RoboMove
            elif RoboMove.colour == yellow:
                yellowRobo = RoboMove
            DrawRobots()
            OccupiedSquares()
            for i in range(boardSize):
                for j in range (boardSize):
                    if board[i][j].occ == board[i][j].tar and board[i][j].occ != 0:
                        print("Success! New target placed")
                        board = PlaceTarget()
                        DrawRobots()
            
    pygame.display.update()


