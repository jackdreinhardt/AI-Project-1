from player import Player
from globals import *
import pygame
import time
import copy
import random

CUTOFF_TIME = 60

class AIPlayer(Player):
    def __init__(self, name, score):
        Player.__init__(self, name, score)
        self.nodes_expanded_ = 0
        self.start_time = 0

    def execute_moves(self, app, limit=10, heuristic=None):
        print(self.name_, "is searching for a solution...")
        count = 0
        self.nodes_expanded_ = 0
        moves = self.search(app.board_, app.target_, app.robots_, limit)
        print("Result: ", moves)
        if (moves == FAILURE or moves == TIME_CUTOFF or moves == DEPTH_CUTOFF):
            return moves
        for m in moves: # for each move
            for r in app.robots_: # for each robot
                if r.color_ == m[0]: # check if robot matches
                    robot = r.move(app.board_, app.robots_, m[1])
                    for i in range(len(app.robots_)):
                            if robot.color_ == app.robots_[i].color_:
                                app.robots_[i] = robot # move robot on board
                    pygame.time.delay(1000)
                    app.graphics_.drawBoardState(app.board_, app.robots_, app.target_)
                    count += 1
        return count

    # moves is an array of (robot, direction) pairs
    #   robot: an instance of the Robot class
    #   direction: a string, "NORTH" "SOUTH" "EAST" or "WEST"
    def search(self, board, robots, limit, heuristic):
        return None
