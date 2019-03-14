import pygame
import random

from robot import Robot
from square import Square
from drawks import GraphicalBoard

class App:

  BOARDSIZE = 16
  SQUARE = 40 #50x50 pixels
  EDGE = 20 #20 pixels wide self.board_ edge
  WALLTHICKNESS = 6 #in pixels
  HALFTHICKNESS = 2 #

  # Define the required colours for the robots and the targets
  RED = (255,0,0)
  BLUE = (0,0,255)
  GREEN = (0,255,0)
  YELLOW = (255,255,0)
  VEL = 50


  def __init__(self):
    # Initialize self.board_ without walls (1-4); no square is currently occupied (5); no target is placed(6)
    self.board_ = [[Square(0,0,0,0,0,0) for j in range(App.BOARDSIZE)] for i in range(App.BOARDSIZE)]

    redRobo = Robot(App.RED,  13, 12)
    blueRobo = Robot(App.BLUE,  5, 11)
    greenRobo = Robot(App.GREEN,  3, 6)
    yellowRobo = Robot(App.YELLOW, 13, 0)
    self.robots_ = [redRobo, blueRobo, greenRobo, yellowRobo]

    self.graphics_ = GraphicalBoard(App.BOARDSIZE, App.SQUARE, App.EDGE, App.WALLTHICKNESS, App.HALFTHICKNESS)

  # For each square determines if the square is currently occupied
  def OccupiedSquares(self):
    for i in range(App.BOARDSIZE):
        for j in range (App.BOARDSIZE):
            self.board_[i][j].occ = 0
    count = 1   
    for r in self.robots_:
      self.board_[r.curSy][r.curSx].occ = r.colour
      count += 1
  
      
  
          
     # Traget saves Colour
  def PlaceTarget(self):
    for i in range(App.BOARDSIZE):
        for j in range (App.BOARDSIZE):
            self.board_[i][j].tar = 0
    rand = random.choice(range(16))
    # Blue targets
    if rand == 0:
        self.board_[1][5].tar = self.RED
    if rand == 1:
        self.board_[5][9].tar = self.RED
    if rand == 2:
        self.board_[9][5].tar = self.RED
    if rand == 3:
        self.board_[11][13].tar = self.RED
    #Red targets
    if rand == 4:
        self.board_[2][1].tar = self.BLUE
    if rand == 5:
        self.board_[2][14].tar = self.BLUE
    if rand == 6:
        self.board_[12][6].tar = self.BLUE
    if rand == 7:
        self.board_[14][14].tar = self.BLUE
    # Green targets
    if rand == 8:
        self.board_[1][12].tar = self.GREEN
    if rand == 9:
        self.board_[6][2].tar = self.GREEN
    if rand == 10:
        self.board_[13][9].tar = self.GREEN
    if rand == 11:
        self.board_[14][2].tar = self.GREEN
    # Yellow targets
    if rand == 12:
        self.board_[4][6].tar = self.YELLOW
    if rand == 13:
        self.board_[6][11].tar = self.YELLOW
    if rand == 14:
        self.board_[9][1].tar = self.YELLOW
    if rand == 15:
        self.board_[10][8].tar = self.YELLOW

  def PlaceWalls(self):
    for i in range(16): # Add outer walls
      self.board_[0][i].north = 1
      self.board_[15][i].south = 1
      self.board_[i][0].west = 1
      self.board_[i][15].east = 1

    # Add inner square walls
    self.board_[6][7].south = self.board_[6][8].south = 1
    self.board_[7][6].east = self.board_[8][6].east = 1
    self.board_[7][9].west = self.board_[8][9].west = 1
    self.board_[9][7].north = self.board_[9][8].north = 1

    # Add vertical walls
    self.board_[0][3].east = self.board_[0][4].west = 1
    self.board_[0][10].east = self.board_[0][11].west = 1
    self.board_[1][5].east = self.board_[1][6].west = 1
    self.board_[1][11].east = self.board_[1][12].west = 1
    self.board_[2][0].east = self.board_[2][1].west = 1
    self.board_[2][13].east = self.board_[2][14].west = 1
    self.board_[3][7].east = self.board_[3][8].west = 1
    self.board_[4][6].east = self.board_[4][7].west = 1
    self.board_[5][9].east = self.board_[5][10].west = 1
    self.board_[6][2].east = self.board_[6][3].west = 1
    self.board_[6][11].east = self.board_[6][12].west = 1
    self.board_[9][1].east = self.board_[9][2].west = 1
    self.board_[9][4].east = self.board_[9][5].west = 1
    self.board_[10][8].east = self.board_[10][9].west = 1
    self.board_[11][12].east = self.board_[11][13].west = 1
    self.board_[12][6].east = self.board_[12][7].west = 1
    self.board_[13][8].east = self.board_[13][9].west = 1
    self.board_[14][1].east = self.board_[14][2].west = 1
    self.board_[14][14].east = self.board_[14][15].west = 1
    self.board_[15][5].east = self.board_[15][6].west = 1
    self.board_[15][11].east = self.board_[15][12].west = 1

    # Add horizontal walls
    self.board_[0][5].south = self.board_[1][5].north = 1
    self.board_[0][12].south = self.board_[1][12].north = 1
    self.board_[2][1].south = self.board_[3][1].north = 1
    self.board_[2][14].south = self.board_[3][14].north = 1
    self.board_[3][0].south = self.board_[4][0].north = 1
    self.board_[3][8].south = self.board_[4][8].north = 1
    self.board_[4][6].south = self.board_[5][6].north = 1
    self.board_[4][15].south = self.board_[5][15].north = 1
    self.board_[5][9].south = self.board_[6][9].north = 1
    self.board_[5][11].south = self.board_[6][11].north = 1
    self.board_[6][2].south = self.board_[7][2].north = 1
    self.board_[8][1].south = self.board_[9][1].north = 1
    self.board_[8][5].south = self.board_[9][5].north = 1
    self.board_[9][15].south = self.board_[10][15].north = 1
    self.board_[10][0].south = self.board_[11][0].north = 1
    self.board_[10][8].south = self.board_[11][8].north = 1
    self.board_[10][13].south = self.board_[11][13].north = 1
    self.board_[12][6].south = self.board_[13][6].north = 1
    self.board_[13][9].south = self.board_[14][9].north = 1
    self.board_[13][14].south = self.board_[14][14].north = 1
    self.board_[14][2].south = self.board_[15][2].north = 1

  def KeyToDir(self, key):
    if key == pygame.K_UP:
        return "NORTH"
    elif key == pygame.K_DOWN:
        return "SOUTH"
    elif key == pygame.K_RIGHT:
        return "EAST"
    elif key == pygame.K_LEFT:
        return "WEST"
    else:
        return "NOT SUPPORTED"

  # Determines which robot was selected by the player. Returns '0' if no robot was selected
  def DetermineRobo(self, click):
    for r in self.robots_:
      if click[0] > r.curSx*self.SQUARE and click[0] < (r.curSx+1)*self.SQUARE and click[1] > r.curSy*self.SQUARE and click[1] < self.SQUARE*(r.curSy+1):
        return r
    return None

  def Run(self):
    self.PlaceWalls()
    self.PlaceTarget()
    self.OccupiedSquares()

    self.graphics_.drawBoardState(self.board_,self.robots_)

    # MAIN LOOP
    currentRobo = 0
    #boardBackup = self.board_
    moveCount = 0
    
    self.graphics_.printToConsole(self.board_)
    
    while True:
      
      pygame.time.delay(100)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          currentRobo = self.DetermineRobo(event.pos)
        if event.type == pygame.KEYDOWN and currentRobo != None:
          d = self.KeyToDir(event.key)
          if currentRobo.move(self.board_, d, App.VEL):
              moveCount += 1
          self.graphics_.drawRobots(self.board_, self.robots_)
          self.OccupiedSquares()
          for i in range(App.BOARDSIZE):
              for j in range (App.BOARDSIZE):
                  if self.board_[i][j].occ == self.board_[i][j].tar and self.board_[i][j].occ != 0:
                      print("Success! New target placed")
                      print("You took " + str(moveCount) + " moves to find a solution")
                      moveCount = 0
                      self.board_ = self.PlaceTarget()
                      self.graphics_.drawRobots(self.board_, self.robots_)
          print("Moves: " + str(moveCount))
      pygame.display.update()



if __name__ == '__main__':
  game = App()
  game.Run()

