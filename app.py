import pygame
import random as rd
import time

from globals import *

from robot import Robot
from board import Board
from target import Target
from drawks import GraphicalBoard

from graph_bredth import Graph_Search_BF
from graph_depth_limited import Graph_Search_DF

from depth_limited_player import Depth_Limited_Player
from a_star_player import A_Star_Player

class App:
    def __init__(self, boardSize, num_robots):
        self.board_ = Board(boardSize)
        self.robots_ = [Robot(RED, rd.randrange(boardSize), rd.randrange(boardSize)),
                        Robot(BLUE, rd.randrange(boardSize), rd.randrange(boardSize)),
                        Robot(GREEN, rd.randrange(boardSize), rd.randrange(boardSize)),
                        Robot(YELLOW, rd.randrange(boardSize), rd.randrange(boardSize))]
        Robot.validate_positions(self.board_, self.robots_)
        self.target_ = Target(boardSize, self.board_, self.robots_)
        self.graphics_ = GraphicalBoard(boardSize)
        self.menu_ = Menu(boardSize)

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
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        pygame.time.delay(100)
        ai_player = Depth_Limited_Player()
        print("Searching for solution")
        start_time = time.time()
        solution = ai_player.search(self.board_, self.target_, self.robots_, 7)
        if (solution != "FAILURE" and solution != "CUTOFF"):
            print("Found solution of length " + str(len(solution)))
            solution_time = time.time() - start_time
            print("The algorithm took " + str(solution_time) + " seconds to find a solution")
            for m in range(len(solution)):
                #print(solution)
                self.robots_[solution[m][0]] = self.robots_[solution[m][0]].move(self.board_, self.robots_, solution[m][1]) # move robot
                self.graphics_.drawRobots(self.board_, self.robots_, self.target_)
                time.sleep(1)
        else:
            print("No solution found")

    def RunAStar(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        pygame.time.delay(100)
        ai_player = A_Star_Player()
        print("Searching for solution")
        start_time = time.time()
        solution = ai_player.search(self.board_, self.target_, self.robots_)
        if (solution != "FAILURE"):
            print("Found solution of length " + str(len(solution)))
            solution_time = time.time() - start_time
            print("The algorithm took " + str(solution_time) + " seconds to find a solution")
            for m in range(len(solution)):
                #print(solution)
                self.robots_[solution[m][0]] = self.robots_[solution[m][0]].move(self.board_, self.robots_, solution[m][1]) # move robot
                self.graphics_.drawRobots(self.board_, self.robots_, self.target_)
                time.sleep(1)
        else:
            print("No solution found")

    def RunBF(self):
        self.graphics_.drawBoardState(self.board_, self.robots_,self.target_)
        player = Graph_Search_BF("k",15,None)
        print("running")
        solution = player.search(self.board_,self.robots_,self.target_)

        for i in solution:
            print(i)


        input()
        pygame.display.quit()
        pygame.quit()

    def Menu(self):
        self.menu_.display()
        settings = self.menu_.get_settings()
        

    def Run(self):
        self.Settings()
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

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
                        moveCount += 1
                        print("Moves: " + str(moveCount))
                        for i in range(len(self.robots_)):
                            if robot.color_ == self.robots_[i].color_:
                                self.robots_[i] = robot
                    self.graphics_.drawRobots(self.board_, self.robots_, self.target_)

                    for r in self.robots_:
                        if r.y_ == self.target_.y_ and r.x_ == self.target_.x_ and r.color_ == self.target_.color_:
                            print("Success! New target placed")
                            print("You took " + str(moveCount) + " moves to find a solution")
                            moveCount = 0
                            self.target_.set_target(self.board_, self.robots_)
                            self.graphics_.drawRobots(self.board_, self.robots_, self.target_)
            pygame.display.update()

if __name__ == '__main__':
    game = App(16, 4)
    game.Menu()
    game.Run()
    # game.RunBF()