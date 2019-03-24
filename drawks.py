import pygame

from robot import Robot
from square import Square

class GraphicalBoard:
    def __init__(self, boardSize):
        self.BoardSize_ = boardSize
        self.SquareSize = 40
        self.EdgeSize = 20
        self.WallThickness = 6
        self.HalfThickness = 2
        
        pygame.init()
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


    # draws the complete game state  
    def drawBoardState(self, board, robots, target):
        self.drawBoard()
        self.drawWalls(board)
        self.drawTarget(target)
        pygame.display.update()
        self.drawRobots(board, robots, target)
        
        
    #Here, the chess board is drawn    
    def drawBoard(self):
        self.Screen.fill(self.Tile2)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.WindowSize[0], self.EdgeSize), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.EdgeSize, self.WindowSize[0]), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, self.WindowSize[0] - self.EdgeSize, self.WindowSize[0], self.EdgeSize), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (self.WindowSize[0] - self.EdgeSize, 0, self.EdgeSize, self.WindowSize[0]), 0)

        for i in range(0, self.BoardSize_, 2):
            for j in range(0, self.BoardSize_, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize, i*self.SquareSize + (self.SquareSize + self.EdgeSize), self.SquareSize, self.SquareSize), 0)
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize + self.SquareSize, i*self.SquareSize + self.EdgeSize, self.SquareSize, self.SquareSize), 0)


    # my new draw method, By using this, the geographyical/physical location of the Robot/Squares should be redundant
    def drawWalls(self, board):
        for i in range(0,self.BoardSize_):
            for j in range (0,self.BoardSize_):
                square = board.square(i, j)
                if square.wall_south_:
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+j*self.SquareSize, self.EdgeSize+(i+1)*self.SquareSize-self.WallThickness/2 ,self.SquareSize,self.WallThickness), 0)
                if square.wall_north_:
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+j*self.SquareSize, self.EdgeSize+i*self.SquareSize-self.WallThickness/2 ,self.SquareSize,self.WallThickness), 0)
                if square.wall_west_:
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+j*self.SquareSize-self.WallThickness/2, self.EdgeSize+i*self.SquareSize ,self.WallThickness,self.SquareSize), 0)
                if square.wall_east_:
                    pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+(j+1)*self.SquareSize-self.WallThickness/2,self.EdgeSize+(i)*self.SquareSize,self.WallThickness ,self.SquareSize), 0)

    def drawTarget(self, target):
        pygame.draw.circle(self.Screen, target.color_, (self.EdgeSize+round((target.x_+0.5)*self.SquareSize),self.EdgeSize+round((target.y_+0.5)*self.SquareSize)), round(self.SquareSize/5), 0)           

    def drawRobots(self, board, robots, target):
        for r in robots:
            space = round(self.SquareSize/5)
            pygame.draw.rect(self.Screen, r.color_, (self.EdgeSize+r.x_*self.SquareSize+space, self.EdgeSize+r.y_*self.SquareSize+space ,self.SquareSize-2*space,self.SquareSize-2*space), 0)
        pygame.display.update()

    # Determines which robot was selected by the player. Returns None if no robot was selected
    def DetermineRobo(self, click, robots):
        for r in robots:
            north_click_bound = self.EdgeSize+r.y_*self.SquareSize
            south_click_bound = self.EdgeSize+(r.y_+1)*self.SquareSize
            east_click_bound = self.EdgeSize+(r.x_+1)*self.SquareSize
            west_click_bound = self.EdgeSize+r.x_*self.SquareSize
            if click[0] > west_click_bound and click[0] < east_click_bound and click[1] > north_click_bound and click[1] < south_click_bound:
                return r
        return None
        

