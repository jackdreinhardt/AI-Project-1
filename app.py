import pygame
import random as rd
import time
from globals import *

from robot import Robot
from board import Board
from target import Target
from drawks import GraphicalBoard

from BF_Graph_Search import Graph_Search_BF
from depth_limited_player import Depth_Limited_Player


class App:
    def __init__(self, boardSize, num_robots):
        self.robots_ = [Robot(RED, rd.randrange(boardSize), rd.randrange(boardSize)),
                        Robot(BLUE, rd.randrange(boardSize), rd.randrange(boardSize)),
                        Robot(GREEN, rd.randrange(boardSize), rd.randrange(boardSize)),
                        Robot(YELLOW, rd.randrange(boardSize), rd.randrange(boardSize))]
        self.board_ = Board(boardSize)
        self.target_ = Target(boardSize, self.board_, num_robots)
        self.graphics_ = GraphicalBoard(boardSize)

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
        self.graphics_.drawBoardState(self.board_, self.robots_)

        robot = None
        moveCount = 0

        while True:
            pygame.time.delay(100)
            ai_player = Depth_Limited_Player()
            print("Searching for solution")
            solution = ai_player.search(self.board_, self.robots_, 3)
            if (solution != "FAILURE" and solution != "CUTOFF"):
                print("Found solution")
                for m in range(len(solution)):
                    #print(solution)
                    self.robots_[solution[m][0]].move(self.board_, solution[m][1]) # move robot
                    self.graphics_.drawRobots(self.board_, self.robots_)
                    time.sleep(1)
            else:
                print("No solution found")
            self.board_.PlaceTarget()
            self.graphics_.drawRobots(self.board_, self.robots_)
            pygame.display.update()
        
      
    def Run(self):
        self.graphics_.drawBoardState(self.board_, self.robots_)

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
                    if robot.move_possible(self.board_, self.robots_, d):
                        robot = robot.move(self.board_, self.robots_, d)
                        for i in range(len(self.robots_)):
                            if robot.color_ == self.robots_[i].color_:
                                self.robots_[i] = robot
                    self.graphics_.drawRobots(self.board_, self.robots_)

                    for r in self.robots_:
                        if r.y_ == self.target_.y_ and r.x_ == self.target_.x_ and r.color_ == target_.color_:
                            print("Success! New target placed")
                            print("You took " + str(moveCount) + " moves to find a solution")
                            moveCount = 0
                            self.board_.PlaceTarget()
                            self.graphics_.drawRobots(self.board_, self.robots_)
                    print("Moves: " + str(moveCount))
            pygame.display.update()

if __name__ == '__main__':
  game = App(6, 4)
  game.Run()


