import pygame
import sys

pygame.init()

square = 50
edge = 20
wallthickness = 6
halfthickness = 2

windowSize = (square*16 + edge*2, square*16 + edge*2)
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
    ## Outer walls
    pygame.draw.rect(screen, black, (edge-halfthickness, edge-halfthickness, windowSize[0]-3/2*edge-halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge-halfthickness, edge-halfthickness, wallthickness, windowSize[0]-3/2*edge-halfthickness), 0)
    pygame.draw.rect(screen, black, (edge-halfthickness, windowSize[0]-edge, windowSize[0]-3/2*edge-halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (windowSize[0]-edge, edge-halfthickness, wallthickness, windowSize[0]-3/2*edge-halfthickness), 0)
    
    ## Inner Square walls
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+7*square-halfthickness, 2*square, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+7*square-halfthickness, wallthickness, 2*square), 0)
    pygame.draw.rect(screen, black, (edge+7*square-halfthickness, edge+9*square-halfthickness, 2*square+2*halfthickness, wallthickness), 0)
    pygame.draw.rect(screen, black, (edge+9*square-halfthickness, edge+7*square-halfthickness, wallthickness, 2*square+2*halfthickness), 0)

    ## Vertical walls
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

    ## Horizontal walls
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
    
    
## ----------------------------------------------------------    
# The Program # ---------------------------------------------

## small show
x = 30
y = 30
vel = 20

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():                    
        if event.type == pygame.QUIT:  
            pygame.display.quit()                 
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    ResetGame()
    pygame.draw.rect(screen, red, (x,y,30,30), 0)    
    
    pygame.display.update()

