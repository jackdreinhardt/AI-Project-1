# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:24:50 2019

@author: kilia
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:46:16 2019

@author: kilia
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:39:24 2019

@author: kilia
"""
import time
from ai_player import *
from node import Node
import copy
import random
from globals import *
import copy
from goal_state import Goal_state
from target import Target

#import copy

class Graph_Search_BF(AIPlayer):


    def __init__(self):
        AIPlayer.__init__(self, 'Informed Breadth First', 0)
        self.nodes_expanded_ = 0


    

    def search(self, board, target, robots, limit,heuristic):
        start_time = time.clock()
        finalNode = self.graph_search(board, target, robots,limit,heuristic)
        if (finalNode != FAILURE): 
            print (time.clock() - start_time, "seconds")
            return Node.get_solution(finalNode)
        else: 
            print (time.clock() - start_time, "seconds")
            return FAILURE


    def go_backwards(self,board, target,robots,limit,heuristic):
        goal_squares=[]
        virtual_robot = Robot(target.color_,target.x_, target.y_)
        direction = ["NORTH", "SOUTH", "EAST", "WEST"]goal_squares.append((target.y_,target.x_))
        while goal_squares != 0:
            
            r = list(filter(lambda r: r.color_==target.color_, robots)
            if (r.color_==target.color_):
                #target reached
                
            else:
                #mögliche Goals hinzugefügt
                for d in direction:
                    goal = self.get_goal_squares(square,board,d,goal_squares)
                    goal_squares+=goal
            
        
        
        
        
        
       
                            
    @staticmethod                      
    def is_target(robot, target):
          if (robot.color_==target.color_ and robot.x_ == target.x_ and robot.y_ == target.y_):
              return True
          else:
              return False
          
    #returns all squares being reachable for the target with two robots
    @staticmethod       
    def get_goal_squares(square,board, d,goal_squares):
        
        
        if (d=="NORTH"):
            b = True
            while b:
                if board.square(y,x).wall_west==1 or board.square(y,x).wall_east==1:
                    # this squares have a wall perpendicular to the way and are reachable goal states
                    
                    if (!=list(filter(lambda r: r=(y,x) , goal_squares)):
                        
                        goal_squares[0].append((y,x))
                # Try to move other robot
                
                elif board.square(y,x+1).wall_west==1 or board.square(y,x-1).wall_east==1:
                    # run bfs for a certain limit
                    goal_squares[1].append((y,x+1))
                    
                if (board.square(y,x).wall_north_==1):
                    b= False
                y+=1    
        elif (d=="SOUTH"):
            b = True
            while b:
                if board.square(y,x).wall_west==1 or board.square(y,x).wall_east==1:
                    # this squares have a wall perpendicular to the way and are reachable goal states
                    if (!=list(filter(lambda r: r=(y,x) , goal_squares)):    
                        
                # Try to move other robot
                
                elif board.square(y,x+1).wall_west==1 or board.square(y,x-1).wall_east==1:
                   
                    
                if (board.square(y,x).wall_north_==1):
                    b= False
                y-=1
        elif (d=="WEST"):
            b = True
            while b:
                if board.square(y,x).wall_north==1 or board.square(y,x).wall_south==1:
                    # this squares have a wall perpendicular to the way and are reachable goal states
                    if (!=list(filter(lambda r: r=(y,x) , goal_squares)):
                        goal_squares[0].append((y,x))
                # Try to move other robot
                
                elif board.square(y,x+1).wall_north==1 or board.square(y,x-1).wall_south==1:
                    
                    
                if (board.square(y,x).wall_west_==1):
                    b= False
                x+=1    
        elif (d=="WEST"):
            b = True
            while b:
                if board.square(y,x).wall_north==1 or board.square(y,x).wall_south==1:
                    # this squares have a wall perpendicular to the way and are reachable goal states
                    if (!=list(filter(lambda r: r=(y,x) , goal_squares)):
                        goal_squares[0].append((y,x))
                # Try to move other robot
                
                elif board.square(y,x+1).wall_north==1 or board.square(y,x-1).wall_south==1:
                    
                    
                if (board.square(y,x).wall_west_==1):
                    b= False
                x-=1 
                
     return goal_squares
          
                            
                        
                        
                        
                           
   
                        
                    
               
