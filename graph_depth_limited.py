# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:45:12 2019

@author: kilia
"""

from ai_player import AIPlayer
from robot import Robot
from node import Node
from move_tuple import MoveTuple
#import copy


        

        
class Graph_Search_DF:
    
    
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
   print(target.color_)
   frontier= []
   expanded = []
   initialState= self.copyState(robots)
   initialNode = Node(initialState,0,0)
   def search(self,board,robots,target):
    finalNode = self.graph_Search(board,robots,target)
    
    if (finalNode!=False):
        
        return Node.find_moves(finalNode)
    else:
        return "FAILURE"
   frontier.append(initialNode)
   limit =4
   print ("Searching")
   while True:
       
       
       if (len(frontier)>0):
           currentNode = Node.copy_node(frontier[0])
           del frontier[0]
           expanded.append(Node.copy_node(currentNode))
       else:
           
           return False
       
       if (currentNode.get_level()<=limit):
       
            for r in currentNode.robots_:
                if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_==r.y_):
                    print(len(expanded))   
                    return currentNode
          
            for i in range (len(currentNode.robots_)):
                #move robot in one direction
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                
                for j in range (len(direction)):
                   
                    
                    if (currentNode.robots_[i].possibleMoves(board,robots,direction[j])) :
                        newNode =  Node.copy_node(currentNode)
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
                            
                            frontier.insert(0,Node.copy_node(newNode))
       
                        
                            
                           
   
                        
                    
               
      
           