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

from ai_player import *
from node import Node
import copy
import random
from globals import *
import copy

#import copy

class Graph_Search_BF(AIPlayer):


    def __init__(self):
        AIPlayer.__init__(self, 'Breadth-First', 0)


    

    def search(self, board, target, robots, limit):
        finalNode = self.graph_search(board, target, robots)
        if (finalNode != FAILURE): return Node.get_solution(finalNode)
        else: return FAILURE


    def graph_search(self,board, target,robots):

       frontier = []
       expanded = []
       robots_copy = copy.deepcopy(robots)
       initialNode = Node(robots_copy, 0, 0, 0, 0)
       frontier.append(initialNode)
       
       limit = 6

       while True:
           
           if (len(frontier) == 0):
               print("fail")
               return FAILURE

           
           currentNode = Node.copyNode(frontier[0])
           del frontier[0]
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
                        r=newNode.robots_[i]
                        if target.color_ == r.color_ and target.x_ == r.x_ and target.y_ == r.y_:
                            return newNode
                        
                        
                        
                        
                        
                        for m in range (len(frontier))  :
                            if (Node.compareState(frontier[m],newNode)==True):
                                unique_node=False
                                break
                        for n in range(len(expanded))  :  
                            if (Node.compareState(expanded[n],newNode)==True):
                                unique_node=False
                                break
                        
          
                        if(unique_node and newNode.get_level()<=limit): 
                            newNode.father_.children_.append(newNode)
                            frontier.append((newNode))
                            
                            
                            
                        
                            
                        
                        
                        
                           
   
                        
                    
               
