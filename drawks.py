import pygame

#draw boardgameEdge
#Drawboardgame
#DrawWalls
#DrawRobots
#DrawTargets

#Draw

from robot import Robot
from square import Square

class GraphicalBoard:
    def __init__(self, boardSize):
        self.BoardSize_ = boardSize
        self.SquareSize = 50
        self.EdgeSize = 20
        self.WallThickness = 6
        self.HalfThickness = 2
        
        window_dim = self.SquareSize * self.BoardSize_
        self.WindowSize = (window_dim, window_dim)
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
        
        

      #draws everything  
    def drawBoardState(self,board, robots):
#        pygame.init()
#        pygame.font.init()
#        pygame.mouse.set_visible(1)
        self.drawBoard()
        self.drawKiliansBoard(board, robots)
        self.drawRobots(board,robots)
        
        
    #Here, the chess board is drawn    
    def drawBoard(self):
        self.Screen.fill(self.Tile2)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.WindowSize[0], 0), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, 0, self.WindowSize[0]), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, self.WindowSize[0] , self.WindowSize[0], 0), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (self.WindowSize[0], 0, 0, self.WindowSize[0]), 0)
     
        for j in range(0, 15, 2):
            for i in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize, i*self.SquareSize + (self.SquareSize), self.SquareSize, self.SquareSize), 0)
        for j in range(0, 15, 2):
            for i in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.SquareSize, i*self.SquareSize , self.SquareSize, self.SquareSize), 0)
       
    #my new draw method, By using this, the geographyical/physical location of the Robot/Squares should be redundant
    def drawKiliansBoard(self, board, robots):
        
        
        
        
#        # Draw outer walls
        
#        
#        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness, self.WallThickness), 0)
#        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WallThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness), 0)
#        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.WindowSize[0]-self.EdgeSize, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness, self.WallThickness), 0)
#        pygame.draw.rect(self.Screen, self.Black, (self.WindowSize[0]-self.EdgeSize, self.EdgeSize-self.HalfThickness, self.WallThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness), 0)

        # Draw inner square walls
        pygame.draw.rect(self.Screen, self.Black, (7*self.SquareSize-self.HalfThickness, 7*self.SquareSize-self.HalfThickness, 2*self.SquareSize, self.WallThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (7*self.SquareSize-self.HalfThickness, 7*self.SquareSize-self.HalfThickness, self.WallThickness, 2*self.SquareSize), 0)
        pygame.draw.rect(self.Screen, self.Black, (7*self.SquareSize-self.HalfThickness, 9*self.SquareSize-self.HalfThickness, 2*self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (9*self.SquareSize-self.HalfThickness, 7*self.SquareSize-self.HalfThickness, self.WallThickness, 2*self.SquareSize+2*self.HalfThickness), 0)
        
        #Draw everything else
        
        for j in range(0,16):
            for i in range (0,16):
                if (board[i][j].south==1):
                    #draw bottom wall
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize,(i+1)*self.SquareSize-self.WallThickness/2 ,self.SquareSize,self.WallThickness), 0)
                if board[i][j].north==1:
                    #top wall
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize,i*self.SquareSize-self.WallThickness/2 ,self.SquareSize,self.WallThickness), 0)
                if board[i][j].west==1:
                   # draw left
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize-self.WallThickness/2,i*self.SquareSize ,self.WallThickness,self.SquareSize), 0)
                if board[i][j].east==1:
                    #draw right
                    pygame.draw.rect(self.Screen, self.Black, ((j+1)*self.SquareSize-self.WallThickness/2,(i)*self.SquareSize,self.WallThickness ,self.SquareSize), 0)
                
                
                
                
                
                if board[i][j].tar:
                    if board[i][j].tar == 1:
                       pygame.draw.circle(self.Screen, self.Blue, (round((j+0.5)*self.SquareSize),round((i+0.5)*self.SquareSize)), 10, 0)
                    if board[i][j].tar == 2:
                       pygame.draw.circle(self.Screen, self.Red, (round((j+0.5)*self.SquareSize),round((i+0.5)*self.SquareSize)), 10, 0)
                    if board[i][j].tar == 3:
                       pygame.draw.circle(self.Screen, self.Green, (round((j+0.5)*self.SquareSize),round((i+0.5)*self.SquareSize)), 10, 0)
                    if board[i][j].tar == 4:
                       pygame.draw.circle(self.Screen, self.Yellow, (round((j+0.5)*self.SquareSize),round((i+0.5)*self.SquareSize)), 10, 0)
                    #draw Target
                   
                    
                
               
   
    def resetBoard(self,board, robots):
        self.drawBoard()
        self.drawKiliansBoard(board,robots)
        pygame.display.update()
        
    
    def drawRobots(self, board, robots):
        self.resetBoard(board,robots)
        for j in range(0,16):
            for i in range (0,16):
        
                    #draw Robot
                    for k in range(0,4):
                        space =10
                        
                        if (robots[k].curSy == i) and (robots[k].curSx == j):
                            
                            pygame.draw.rect(self.Screen, robots[k].colour, (j*self.SquareSize+space, i*self.SquareSize+space ,self.SquareSize-2*space,self.SquareSize-2*space), 0)
        pygame.display.update()
        
    def printToConsole(self,board):
         for j in range(0,16):
             for i in range (0,16):
                print(board[j][i].west, end = '')
             print()

