import pygame

#draw boardgameEdge
#Drawboardgame
#DrawWalls
#DrawRobots
#DrawTargets

#Draw

class GraphicalBoard:
    
    def __init__(self, boardSize, squareSize, edgeSize, wallthickness, halfthickness, windowTile):
        self.BoardSize = boardSize
        self.SquareSize = squareSize
        self.EdgeSize = edgeSize
        self.WallThickness = wallthickness
        self.HalfThickness = halfthickness
        self.WindowTile= windowTile
        self.MoveCount = 0
        
        self.WindowSize = (squareSize*boardSize + edgeSize*2, squareSize*boardSize + edgeSize*2)
        self.WindowTitle = "Ricochet Robots"
        self.Screen = pygame.display.set_mode(self.WindowSize)
        pygame.display.set_caption(self.WindowTitle)
    
    # Define the required colours for the boardgame
        self.Tile1 = (230, 245, 255)
        self.Tile2 = (245, 255, 250)
        self.Edgecol = (173, 216, 230)
        self.Black = (0,0,0)
        self.Grey = (100,100,100)
    
    # Define the required colours for the robots and the targets
        self.Red = (255,0,0)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Yellow = (255,255,0)
        
        
        
        
    def drawBoardState(self,board,robots):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(1)
        self.drawEdges
        self.drawBoard
        self.drawRobots
        self.drawTarget
        self.drawWalls
        
        
    def drawBoard(self):
        for j in range(0, 15, 2):
            for i in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize, i*self.SquareSizes + (self.SquareSize + self.EdgeSize), self.SquareSize, self.SquareSize), 0)
        for j in range(0, 15, 2):
            for i in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize + self.SquareSize, i*self.SquareSize + self.EdgeSize, self.SquareSize, self.SquareSize), 0)
       
        
    def drawEdges(self):
    
       self.Screen.fill(self.Tile2)
       pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.WindowSize[0], self.EdgeSize), 0)
       pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.EdgeSize, self.WindowSize[0]), 0)
       pygame.draw.rect(self.Screen, self.Edgecol, (0, self.WindowSize[0] - self.EdgeSize, self.WindowSize[0], self.EdgeSize), 0)
       pygame.draw.rect(self.Screen, self.Edgecol, (self.WindowSize[0] - self.EdgeSize, 0, self.EdgeSize, self.WindowSize[0]), 0)
       print("Eecuted DrawEdges")
       
    def drawWalls(self):
        # Draw outer walls
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WallThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.WindowSize[0]-self.EdgeSize, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.WindowSize[0]-self.EdgeSize, self.EdgeSize-self.HalfThickness, self.WallThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness), 0)

    # Draw inner self.SquareSize walls
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, 2*self.SquareSize, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.WallThickness, 2*self.SquareSize), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+9*self.SquareSize-self.HalfThickness, 2*self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.WallThickness, 2*self.SquareSize+2*self.HalfThickness), 0)

    # Draw vertical walls
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+4*self.SquareSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+11*self.SquareSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+12*self.SquareSize-self.HalfThickness, self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.EdgeSize+2*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.EdgeSize+2*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+8*self.SquareSize-self.HalfThickness, self.EdgeSize+3*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+4*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+10*self.SquareSize-self.HalfThickness, self.EdgeSize+5*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+3*self.SquareSize-self.HalfThickness, self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+12*self.SquareSize-self.HalfThickness, self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+2*self.SquareSize-self.HalfThickness, self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+5*self.SquareSize-self.HalfThickness, self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.EdgeSize+10*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+13*self.SquareSize-self.HalfThickness, self.EdgeSize+11*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+12*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.EdgeSize+13*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+2*self.SquareSize-self.HalfThickness, self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+15*self.SquareSize-self.HalfThickness, self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.EdgeSize+15*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+12*self.SquareSize-self.HalfThickness, self.EdgeSize+15*self.SquareSize-self.HalfThickness, self.WallThickness, self.SquareSize+2*self.HalfThickness), 0)

    # Draw horizontal walls
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+5*self.SquareSize-self.HalfThickness, self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+12*self.SquareSize-self.HalfThickness, self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.EdgeSize+3*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.EdgeSize+3*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+0*self.SquareSize-self.HalfThickness, self.EdgeSize+4*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+8*self.SquareSize-self.HalfThickness, self.EdgeSize+4*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.EdgeSize+5*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+15*self.SquareSize-self.HalfThickness, self.EdgeSize+5*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+11*self.SquareSize-self.HalfThickness, self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+2*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+1*self.SquareSize-self.HalfThickness, self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+5*self.SquareSize-self.HalfThickness, self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+15*self.SquareSize-self.HalfThickness, self.EdgeSize+10*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+0*self.SquareSize-self.HalfThickness, self.EdgeSize+11*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+8*self.SquareSize-self.HalfThickness, self.EdgeSize+11*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+13*self.SquareSize-self.HalfThickness, self.EdgeSize+11*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+6*self.SquareSize-self.HalfThickness, self.EdgeSize+13*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.EdgeSize+14*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
       pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+2*self.SquareSize-self.HalfThickness, self.EdgeSize+15*self.SquareSize-self.HalfThickness, self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)

    def drawRobots(self, robots):
       #ResetBoard()
       for i in range(robots.length):
           pygame.draw.rect(self.Screen, robots[i].Colour, (robots[i].curY,30,30),0)
       
       pygame.display.update()

    def drawTarget(self,board):
       for i in range(self.BoardSize):
          for j in range (self.BoardSize):
              if board[i][j].tar != 0:
                        if board[i][j].tar == 1:
                            pygame.draw.circle(self.Screen, self.Blue, (self.EdgeSize+j*self.SquareSize+25, self.EdgeSize+i*self.SquareSize+25), 10, 0)
                        if board[i][j].tar == 2:
                            pygame.draw.circle(self.Screen, self.Red, (self.EdgeSize+j*self.SquareSize+25, self.EdgeSize+i*self.SquareSize+25), 10, 0)
                        if board[i][j].tar == 3:
                            pygame.draw.circle(self.Screen, self.Green, (self.EdgeSize+j*self.SquareSize+25, self.EdgeSize+i*self.SquareSize+25), 10, 0)
                        if board[i][j].tar == 4:
                            pygame.draw.circle(self.Screen, self.Yellow, (self.EdgeSize+j*self.SquareSize+25, self.EdgeSize+i*self.SquareSize+25), 10, 0)
    
    def resetBoard(self):
        self.drawEdges()
        self.drawBoard()
        self.drawWalls()
        self.drawTarget()
        pygame.display.update()
#
