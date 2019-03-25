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


    

    def search(self, board, target, robots, limit):
        start_time = time.clock()
        finalNode = self.graph_search(board, target, robots,limit)
        if (finalNode != FAILURE): 
            print (time.clock() - start_time, "seconds")
            return Node.get_solution(finalNode)
        else: 
            print (time.clock() - start_time, "seconds")
            return FAILURE


    def graph_search(self,board, target,robots,limit):

       frontier = []
       expanded = []
       
       
       #from all these positions the target can be reached within less than 5+1 moves
       goal_states = target.get_goal_locations(board,1)
       
       initialNode = Node(robots, 0, 0, 0, 0)
       frontier.append(initialNode)
       
       x=0
       for robot in robots:
               
               if self.is_target(robot,target):
                            return initialNode

       while True:
           
           # if frontier is empty or the limit is 
           if (len(frontier) == 0):
               print("Expanded game states: ", len(expanded))
               return FAILURE

           
           currentNode = Node.copyNode(frontier[0])
           del frontier[0]
           expanded.append((currentNode))

           
           for i in range (len(currentNode.robots_)):
                
                #move robot in one direction
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                
                for j in range (len(direction)):
                   
                    
                    if (currentNode.robots_[i].move_possible(board,currentNode.robots_,direction[j])) :
                        
                        
                        newNode =  Node.copyNode(currentNode)
                        unique_node=True
                        newNode.robots_[i] = newNode.robots_[i].move(board,currentNode.robots_,direction[j])
                        newNode.move_tuple_ = (copy.deepcopy(COLORS[i]), direction[j])
                        newNode.father_ = currentNode
                        currentNode.children_.append(newNode)
                        r=newNode.robots_[i]
                        if self.is_target(r,target):
                            return newNode
                        
                        
#                        for g in goal_states:
#                            if (g.is_goal_state(board,robots)!=False):
#                                # goal state is reachable from the current node -> All nodes will be removed from the frontier
#                                
#                                frontier.clear()
#                                frontier.append((newNode))
#                                break
                                
                                
                        
                        for m in range (len(frontier))  :
                            if (Node.compare_robots(frontier[m],newNode)):
                                unique_node=False
                                break
                        for n in range(len(expanded))  :  
                            if (Node.compare_robots(expanded[n],newNode)):
                                unique_node=False
                                break
                        
          
                        if(unique_node and newNode.get_level()<(limit)): 
                            
                            frontier.append((newNode))
                            
    @staticmethod                      
    def is_target(robot, target):
          if (robot.color_==target.color_ and robot.x_ == target.x_ and robot.y_ == target.y_):
              return True
          else:
              return False
             
                     
                            
                        
                        
                        
                           
   
                        
                    
               
