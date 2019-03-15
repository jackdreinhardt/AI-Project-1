import pygame

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
        self.WindowSize = (window_dim + 2 * self.EdgeSize, window_dim + 2 * self.EdgeSize)
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
        self.drawBoard()
        self.drawObstacles(board, robots)
        self.drawRobots(board, robots)
        
        
    #Here, the chess board is drawn    
    def drawBoard(self):
        self.Screen.fill(self.Tile2)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.WindowSize[0], self.EdgeSize), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.EdgeSize, self.WindowSize[0]), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, self.WindowSize[0] - self.EdgeSize, self.WindowSize[0], self.EdgeSize), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (self.WindowSize[0] - self.EdgeSize, 0, self.EdgeSize, self.WindowSize[0]), 0)

        for i in range(0, 15, 2):
            for j in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize, i*self.SquareSize + (self.SquareSize + self.EdgeSize), self.SquareSize, self.SquareSize), 0)
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize + self.SquareSize, i*self.SquareSize + self.EdgeSize, self.SquareSize, self.SquareSize), 0)


    #my new draw method, By using this, the geographyical/physical location of the Robot/Squares should be redundant
    def drawObstacles(self, board, robots):
        for i in range(0,16):
            for j in range (0,16):
                square = board[i][j]
                if square.south_:
                    #draw bottom wall
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+j*self.SquareSize, self.EdgeSize+(i+1)*self.SquareSize-self.WallThickness/2 ,self.SquareSize,self.WallThickness), 0)
                if square.north_:
                    #top wall
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+j*self.SquareSize, self.EdgeSize+i*self.SquareSize-self.WallThickness/2 ,self.SquareSize,self.WallThickness), 0)
                if square.west_:
                   # draw left
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+j*self.SquareSize-self.WallThickness/2, self.EdgeSize+i*self.SquareSize ,self.WallThickness,self.SquareSize), 0)
                if square.east_:
                    #draw right
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+(j+1)*self.SquareSize-self.WallThickness/2,self.EdgeSize+(i)*self.SquareSize,self.WallThickness ,self.SquareSize), 0)
                if square.target_ != None:
                    pygame.draw.circle(self.Screen, board[i][j].target_.color_, (self.EdgeSize+round((j+0.5)*self.SquareSize),self.EdgeSize+round((i+0.5)*self.SquareSize)), 10, 0)           
   
    def resetBoard(self,board, robots):
        self.drawBoard()
        self.drawObstacles(board,robots)
        pygame.display.update()
    
    def drawRobots(self, board, robots):
        self.resetBoard(board,robots)
        for j in range(0,16):
            for i in range (0,16):
        
                    #draw Robot
                    for k in range(0,4):
                        space =10
                        if (robots[k].y_ == i) and (robots[k].x_ == j):
                            pygame.draw.rect(self.Screen, robots[k].color_, (self.EdgeSize+j*self.SquareSize+space, self.EdgeSize+i*self.SquareSize+space ,self.SquareSize-2*space,self.SquareSize-2*space), 0)
        pygame.display.update()
        
    def printToConsole(self,board):
         for j in range(0,16):
             for i in range (0,16):
                print(board[j][i].west, end = '')
             print()

