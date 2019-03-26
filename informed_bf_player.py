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
from collections import deque
import copy
from goal_state import Goal_state
from target import Target

#import copy

class Graph_Search_BF(AIPlayer):


    def __init__(self):
        AIPlayer.__init__(self, 'Informed Breadth First', 0)
        self.nodes_expanded_ = 0


    

    def search(self, board, target, robots, limit,heuristic):
       
        self.start_time = time.time()
        return Node.get_solution(self.graph_search(board, target, robots, limit, heuristic))
        

    def graph_search(self,board, target,robots,limit,heuristic):
        
       #pop 
       
       initialNode = Node(robots, 0, 0, 0, 0,0)
       
       frontier = deque([initialNode])
       expanded = deque([])
       
       for robot in robots:
               
               if self.is_target(robot,target):
                   return initialNode

       while True:
           
           # if frontier is emptyy
           if (len(frontier) == 0):
               return DEPTH_CUTOFF
           if (time.time() - self.start_time > CUTOFF_TIME):
               return TIME_CUTOFF
           
           currentNode = Node.copyNode(frontier[0])
           frontier.popleft()
           expanded.append(currentNode)
           self.nodes_expanded_ += 1
           
           for i in range (len(currentNode.robots_)):
                
                #move robot in one direction
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                
                for j in range (len(direction)):
                    
                    if (currentNode.robots_[i].move_possible(board,currentNode.robots_,direction[j])) :
                        newNode =  Node.copyNode(currentNode)
                        unique_node=True
                        newNode.robots_[i] = newNode.robots_[i].move(board,currentNode.robots_,direction[j])
                        newNode.move_tuple_ = (COLORS[i], direction[j])
                        newNode.father_ = currentNode
                        newNode.level_+=1
                        currentNode.children_.append(newNode)
                        r=newNode.robots_[i]
                        if self.is_target(r,target):
                            return newNode
                             
                        
                        for m in range (len(frontier))  :
                            if (Node.compare_robots(frontier[m],newNode)):
                                unique_node=False
                                break
                        for n in range(len(expanded))  :  
                            if (Node.compare_robots(expanded[n],newNode)):
                                unique_node=False
                                break
                        
          
                        if(unique_node and newNode.level_<(limit)): 
                            
                            frontier.append((newNode))
                            
    @staticmethod                      
    def is_target(robot, target):
          if (robot.color_==target.color_ and robot.x_ == target.x_ and robot.y_ == target.y_):
              return True
          else:
              return False
             
                     
                            
                        
                        
                        
                           
   
                        
                    
               
