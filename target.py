import random as rd
from globals import *
from board import Board
from robot import Robot
from square import Square
from goal_state import Goal_state
import copy

class Target:
    def __init__(self, boardSize, board, robots):
        self.board_size_ = boardSize
        self.set_target(board, robots)

    def set_target(self, board, robots):
        self.color_ = robots[rd.randrange(len(robots))].color_
        locations = self.valid_locations(board, robots)
        loc = locations[rd.randrange(len(locations))]
        self.x_ = loc[1]
        self.y_ = loc[0]

    def valid_target_loc(self, board, robots, i, j):
        return ((board.square(i, j).wall_north_ and board.square(i, j).wall_east_) \
            or (board.square(i, j).wall_north_ and board.square(i, j).wall_west_) \
            or (board.square(i, j).wall_south_ and board.square(i, j).wall_east_) \
            or (board.square(i, j).wall_south_ and board.square(i, j).wall_west_)) \
            and not board.center(i, j) \
            and not (i,j) in [(r.y_,r.x_) for r in robots]
            # and not (i == 0 or i ==  self.board_size_ - 1) \
            # and not (j == 0 or j == self.board_size_ - 1) \
            

    def valid_locations(self, board, robots):
        locations = []
        for i in range(self.board_size_):
            for j in range(self.board_size_):
                if self.valid_target_loc(board, robots, i, j):
                    locations.append((i,j))
        return locations
    
    def get_goal_locations(self,board,levels):
        directions = ["NORTH", "SOUTH", "EAST", "WEST"]
        
        frontier = []
        
        
        goal_states = []
                
        initial = Goal_state(self.color_,self.x_,self.y_,0)
        frontier.append(initial)
        
        while (len(frontier)!= 0):
            current = copy.deepcopy(frontier[0])
            del frontier[0]
            for d in directions:
                
                robot = copy.deepcopy(Robot(current.color_,current.x_,current.y_))
                #check if move is possible
                if (self.move_possible(board,robot,d)):
                    #virtual_robot is moved 
                    self.move(board,robot,d)
                    add = True
                    for g in goal_states:
                        if(robot.color_== g.color_ and robot.x_ == g.x_ and robot.y_ == g.y_):
                            add = False
                    for g in frontier:
                        if(robot.color_== g.color_ and robot.x_ == g.x_ and robot.y_ == g.y_):
                            add = False
                    if (add and current.level_ < levels):
                        goal_states.append(Goal_state(robot.color_, robot.x_, robot.y_,current.level_+1))
                        frontier.append(Goal_state(robot.color_, robot.x_, robot.y_,current.level_+1))
                    
        return goal_states                    
        


    def move_possible(self, board, robot, d):
        x = robot.x_
        y = robot.y_
        if d == "NORTH":
            if board.square(y, x).wall_north_:
                return False
        elif d == "SOUTH":
            if board.square(y, x).wall_south_:
                return False
        elif d == "EAST":
            if board.square(y, x).wall_east_:
                return False
        elif d == "WEST":
            if board.square(y, x).wall_west_:
                return False
        
        return True

   
    # Robot is moved, doesn't return a copy of robot
    @staticmethod
    def move(board, robot, d):
        
        if d == "NORTH":
            while not board.square(robot.y_, robot.x_).wall_north_:
                
                robot.y_ -= 1
        elif d == "SOUTH":
            while not board.square(robot.y_, robot.x_).wall_south_:
                robot.y_ += 1
        elif d == "EAST":
            while not board.square(robot.y_, robot.x_).wall_east_:
                robot.x_ += 1
        elif d == "WEST":
           while not board.square(robot.y_, robot.x_).wall_west_:
                robot.x_ -= 1
        


