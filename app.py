import pygame
import random

from robot import Robot
from square import Square
from drawks import GraphicalBoard
from board import Board
from globals import *

class App:
  def __init__(self):
    self.robots_ = [Robot(RED, 13, 12), Robot(BLUE, 5, 11),
                    Robot(GREEN, 3, 6), Robot(YELLOW, 13, 0)]
    self.state_ = Board(self.robots_)
    self.graphics_ = GraphicalBoard(BOARDSIZE)

  def settings():
    print("AI or human? (a / h)")


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

  def Run(self):
    self.state_.PlaceWalls()
    self.state_.PlaceRobots()
    self.state_.PlaceTarget()

    self.graphics_.drawBoardState(self.state_.board_, self.robots_)

    robot = None
    moveCount = 0
    
    while True:
      pygame.time.delay(100)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          robot = self.graphics_.DetermineRobo(event.pos, self.robots_)
        if event.type == pygame.KEYDOWN and robot != None:
          d = self.KeyToDir(event.key)
          if robot.move(self.state_.board_, d):
              moveCount += 1
          self.graphics_.drawRobots(self.state_.board_, self.robots_)

          for r in self.robots_:
            if self.state_.board_[r.y_][r.x_].target_ != None and self.state_.board_[r.y_][r.x_].target_.color_ == r.color_:
              print("Success! New target placed")
              print("You took " + str(moveCount) + " moves to find a solution")
              moveCount = 0
              self.PlaceTarget()
              self.graphics_.drawRobots(self.state_.board_, self.robots_)
          print("Moves: " + str(moveCount))
      pygame.display.update()

if __name__ == '__main__':
  game = App()
  game.settings()
  game.Run()

