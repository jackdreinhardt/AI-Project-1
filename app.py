import pygame
import random
import time
from globals import *
from depth_limited_player import Depth_Limited_Player

from robot import Robot
from square import Square
from drawks import GraphicalBoard
from board import Board
from BF_Graph_Search import Graph_Search_BF


class App:
  def __init__(self):
    self.robots_ = (Robot(RED, 1, 1), Robot(BLUE, 2, 2),
                    Robot(GREEN, 0, 3), Robot(YELLOW, 4, 0))
    self.state_ = Board()
    self.graphics_ = GraphicalBoard(BOARDSIZE)

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

  def RunAI(self):
    self.state_.PlaceWalls(16)
    self.state_.PlaceRobots(self.robots_)
#    self.state_.PlaceTarget()

    self.graphics_.drawBoardState(self.state_.board_, self.robots_)

    robot = None
    moveCount = 0

<<<<<<< HEAD
#    while True:
#      pygame.time.delay(100)
#      ai_player = Depth_Limited_Player()
#      print("Searching for solution")
#      solution = ai_player.search(self.state_.board_, self.robots_, 3)
#      if (solution != "FAILURE" and solution != "CUTOFF"):
#        print("Found solution")
#        for m in range(len(solution)):
#          #print(solution)
#          self.robots_[solution[m][0]].move(self.state_.board_, solution[m][1]) # move robot
#          self.graphics_.drawRobots(self.state_.board_, self.robots_)
#          time.sleep(1)
#          break
#      else:
#        print("No solution found")
#        break
=======

    pygame.time.delay(100)
    ai_player = Depth_Limited_Player()
    print("Searching for solution")
    solution = ai_player.search(self.state_.board_, self.robots_, 5)
    if (solution != "FAILURE" and solution != "CUTOFF"):
      print("Found solution")
      for m in range(len(solution)):
        #print(solution)
        self.robots_[solution[m][0]].move(self.state_.board_, solution[m][1]) # move robot
        self.graphics_.drawRobots(self.state_.board_, self.robots_)
        time.sleep(1)
    else:
      print("No solution found")
>>>>>>> 9b6d2f43e98c43442ab24eb7a2daac0270898f86

  def Run(self):
    self.state_.PlaceWalls(6)
    self.state_.PlaceRobots(self.robots_)
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
              self.state_.PlaceTarget()
              self.graphics_.drawRobots(self.state_.board_, self.robots_)
          print("Moves: " + str(moveCount))
      pygame.display.update()

if __name__ == '__main__':
  game = App()
  game.RunAI()
