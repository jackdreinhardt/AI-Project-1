# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:03:05 2019

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

#import copy

class Graph_Search_DF(AIPlayer):


    def __init__(self):
        AIPlayer.__init__(self, 'Breadth-First', 0)


    

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
       
        
        #reorder items to make sure the algorithm always tries to move the robot having the same color like the target firstly
       for i in range(len(robots)):
           if(robots[i].color_==target.color_):
               first = i
       robots[first], robots[len(robots)-1] = robots[len(robots)-1], robots[first]
       
       frontier = []
       expanded = []
       
       initialNode = Node(robots, 0, 0, 0, 0)
       frontier.append(initialNode)
       
       
       for robot in robots:
               
               if self.is_target(robot,target):
                            return initialNode

       while True:
           
           # if frontier is empty or the limit is 
           if (len(frontier) == 0):
               print("Expanded game states: ", len(expanded))
               return FAILURE

           
           currentNode = Node.copyNode(frontier[-1])
           del frontier[-1]
           expanded.append((currentNode))

           self.nodes_expanded_ += 1
           
                        
          
         
               
               
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
             
                        
                            
                        
                        
                        
                           
   
                        
                    
               
