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
        
        

      #draws everything  
    def drawBoardState(self,board):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(1)
        self.drawBoard()
        self.drawKiliansBoard()
        
        
    #Here, the chess board is drawn    
    def drawBoard(self):
        for j in range(0, 15, 2):
            for i in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize, i*self.SquareSizes + (self.SquareSize + self.EdgeSize), self.SquareSize, self.SquareSize), 0)
        for j in range(0, 15, 2):
            for i in range(0, 15, 2):
                pygame.draw.rect(self.Screen, self.Tile1, (j*self.SquareSize + self.EdgeSize + self.SquareSize, i*self.SquareSize + self.EdgeSize, self.SquareSize, self.SquareSize), 0)
       
    #my new draw method, By using this, the geographyical/physical location of the Robot/Squares should be redundant
    def drawKiliansBoard(self, board):
        
        
        self.Screen.fill(self.Tile2)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.WindowSize[0], self.EdgeSize), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, 0, self.EdgeSize, self.WindowSize[0]), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (0, self.WindowSize[0] - self.EdgeSize, self.WindowSize[0], self.EdgeSize), 0)
        pygame.draw.rect(self.Screen, self.Edgecol, (self.WindowSize[0] - self.EdgeSize, 0, self.EdgeSize, self.WindowSize[0]), 0)
     
        
        # Draw outer walls
        
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness, self.WallThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.EdgeSize-self.HalfThickness, self.WallThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize-self.HalfThickness, self.WindowSize[0]-self.EdgeSize, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness, self.WallThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (self.WindowSize[0]-self.EdgeSize, self.EdgeSize-self.HalfThickness, self.WallThickness, self.WindowSize[0]-3/2*self.EdgeSize-self.HalfThickness), 0)

        # Draw inner square walls
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, 2*self.SquareSize, self.WallThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.WallThickness, 2*self.SquareSize), 0)
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.EdgeSize+9*self.SquareSize-self.HalfThickness, 2*self.SquareSize+2*self.HalfThickness, self.WallThickness), 0)
        pygame.draw.rect(self.Screen, self.Black, (self.EdgeSize+9*self.SquareSize-self.HalfThickness, self.EdgeSize+7*self.SquareSize-self.HalfThickness, self.WallThickness, 2*self.SquareSize+2*self.HalfThickness), 0)
        
        #Draw everything else
        
        for j in range(0,15):
            for i in range (0,15):
                if board[i][j].hasWallSouth:
                    #draw bottom wall
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize,(i+1)*self.SquareSize-self.HalfThickness ,2*self.HalfThickness,self.WallThickness), 0)
                if board[i][j].hasWallNorth:
                    #top wall
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize,i*self.SquareSize-self.HalfThickness ,2*self.HalfThickness,self.WallThickness), 0)
                if board[i][j].hasWallWest:
                   # draw left
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize,i*self.SquareSize-self.HalfThickness ,self.WallThickness,2*self.HalfThickness), 0)
                if board[i][j].hasWallEast:
                    #draw right
                    pygame.draw.rect(self.Screen, self.Black, (j*self.SquareSize,(i+1)*self.SquareSize-self.HalfThickness,self.WallThickness ,2*self.HalfThickness), 0)
                
                
                
                
                
                if board[i][j].hasTarget:
                    if board[i][j].tar == 1:
                       pygame.draw.circle(self.Screen, self.Blue, ((j+0.5)*self.SquareSize,(i+0.5)*self.SquareSize), 10, 0)
                    if board[i][j].tar == 2:
                       pygame.draw.circle(self.Screen, self.Red, ((j+0.5)*self.SquareSize,(i+0.5)*self.SquareSize), 10, 0)
                    if board[i][j].tar == 3:
                       pygame.draw.circle(self.Screen, self.Green, ((j+0.5)*self.SquareSize,(i+0.5)*self.SquareSize), 10, 0)
                    if board[i][j].tar == 4:
                       pygame.draw.circle(self.Screen, self.Yellow, ((j+0.5)*self.SquareSize,(i+0.5)*self.SquareSize), 10, 0)
                    #draw Target
                    
                    
                
                if board[i][j].occupant:
                    #draw Robot
                    pygame.draw.rect(self.Screen, occupant.Colour, (j*self.SquareSize+self.SquareSize/2, i*self.SquareSize+self.SquareSize/2 ,30,30), 0)
        
        
   
    def resetBoard(self):
        self.drawBoard()
        self.drawKiliansBoard()
        pygame.display.update()
        
    
#
