import pygame
import random

from robot import Robot
from square import Square

class App:

  BOARDSIZE = 16
  SQUARE = 50 #50x50 pixels

  # Define the required colours for the robots and the targets
  RED = (255,0,0)
  BLUE = (0,0,255)
  GREEN = (0,255,0)
  YELLOW = (255,255,0)
  VEL = 50


  def __init__(self):
    # Initialize board without walls (1-4); no square is currently occupied (5); no target is placed(6)
    self.board_ = [[Square(0,0,0,0,0,0) for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]

    redRobo = Robot(App.RED, 30+13*App.SQUARE, 30+12*App.SQUARE, 13, 12)
    blueRobo = Robot(App.BLUE, 30+5*App.SQUARE, 30+11*App.SQUARE, 5, 11)
    greenRobo = Robot(App.GREEN, 30+3*App.SQUARE, 30+6*App.SQUARE, 3, 6)
    yellowRobo = Robot(App.YELLOW, 30+13*App.SQUARE, 30, 13, 0)
    self.robots_ = [redRobo, blueRobo, greenRobo, yellowRobo]

  def PlaceWalls():
    for i in range(App.BOARDSIZE): # Add outer walls
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

    # Determines which robot was selected by the player. Returns '0' if no robot was selected
  def DetermineRobo(click):
    for r in self.robots_:
      if click[0] > r.curX and click[0] < r.curX+30 and click[1] > r.curY and click[1] < r.curY+30:
        return r

  def Run():

    # Places walls on the board
    self.board_ = PlaceWalls()

    # Determines occupied squares
    self.board_ = OccupiedSquares()

    # Places the target on the board
    self.board_ = PlaceTarget()

    # Draw board and robots
    DrawRobots()

    # MAIN LOOP
    currentRobo = 0
    boardBackup = self.board_
    moveCount = 0

    while True:
      pygame.time.delay(100)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          currentRobo = DetermineRobo(event.pos)
        if event.type == pygame.KEYDOWN and currentRobo != 0:
            d = KeyToDir(event.key)
            if currentRobo.move(board, d, App.VEL):
                moveCount += 1
            DrawRobots()
            OccupiedSquares()
            for i in range(BOARDSIZE):
                for j in range (BOARDSIZE):
                    if board[i][j].occ == board[i][j].tar and board[i][j].occ != 0:
                        print("Success! New target placed")
                        print("You took " + str(moveCount) + " moves to find a solution")
                        moveCount = 0
                        board = PlaceTarget()
                        DrawRobots()
              print("Moves: " + str(moveCount))
        pygame.display.update()



if __name__ == '__main__':
  game = App()
  game.Run()

