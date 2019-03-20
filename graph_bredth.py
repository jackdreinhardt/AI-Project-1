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

from ai_player import AIPlayer
from robot import Robot
from node import Node
from move_tuple import MoveTuple
#import copy

class Graph_Search_BF:
    
    
    def copyState(self,state1):
        robots = []
        for i in range(len(state1)):
            x=state1[i].x_
            y=state1[i].y_
            c= state1[i].color_
            robots.append(Robot(c,x,y))
            
        return robots    
        
    
    def __init__(self,name,score,board):
        AIPlayer.__init__(self, None, None,None)
        
    def search(self,board,robots,target):
        finalNode = self.graph_Search(board,robots,target)
        
        if (finalNode!=False):
            
            return Node.find_moves(finalNode)
        else:
            return "FAILURE"
 

    def graph_Search(self,board, robots,target):
        
       frontier= []
       expanded = []
       initialState= self.copyState(robots)
       initialNode = Node(initialState,0,0)
       
       frontier.append(initialNode)
       
       while True:
          
           
           currentNode = Node.copyNode(frontier[0])
           del frontier[0]
           
           expanded.append(Node.copyNode(currentNode))
           
           for r in currentNode.robots_:
               if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_==r.y_):
                       return currentNode
              
           
           for i in range (len(currentNode.robots_)):
                #move robot in one direction
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                
                for j in range (len(direction)):
                   
                    
                    if (currentNode.robots_[i].possibleMoves(board,robots,direction[j])) :
                        newNode =  Node.copyNode(currentNode)
                        tr=True
                        newNode.robots_[i] = newNode.robots_[i].move(board,robots,direction[j])
                        
                        
                        newNode.move_tuple_=MoveTuple(currentNode.robots_[i].color_,direction[j])
                        newNode.father_=currentNode
                        
                        for m in range (len(frontier))  :
                            if (Node.compareState(frontier[m],newNode)==True):
                                tr=False
                                break
                        for n in range(len(expanded))  :  
                            if (Node.compareState(expanded[n],newNode)==True):
                                tr=False
                                break
                        if(tr):
                            
                            frontier.append(Node.copy_node(newNode))
                            
                            
                        
                            
                            
                           
   
                        
                    
               