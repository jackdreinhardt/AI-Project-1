# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:39:24 2019

@author: kilia
"""

from ai_player import AIPlayer
from robot import Robot



class node:
    
    
        
    def __init__(self,robots,father, movetuple):
        self.robots_=robots
        self.father_=father
        self.moveTuple_=movetuple
        
    @staticmethod    
    def compareState(state1,state2):
        
        t=True
        for i in range(len(state1.robots_)):
                if (state1.robots_[i].color_!=state2.robots_[i].color_) or (state1.robots_[i].x_!=state2.robots_[i].x_ ) or (state1.robots_[i].y_!=state2.robots_[i].y_):
                    t=False
        return t           
            
                    
            
    
        
    @staticmethod 
    def copyNode(oldNode):
        f=oldNode.father_
        if(oldNode.moveTuple_!=0):
            tupl = moveTuple(oldNode.moveTuple_.robotColour_, oldNode.moveTuple_.dir_)
        else:
            tupl=0
        r=[]
        for i in range(len(oldNode.robots_)):
            x=oldNode.robots_[i].x_
            y=oldNode.robots_[i].y_
            c= oldNode.robots_[i].color_
            r.append(Robot(c,x,y))
            
        return node(r,f,tupl)
    
    
        
class moveTuple:
    def __init__(self,robotColor,direction):
        self.robotColour_ = robotColor
        self.dir_= direction
        


            
        
        

class Graph_Search_BF:
    
    
    def copyState(self,state1):
        robots = []
        for i in range(len(state1)):
            x=state1[i].x_
            y=state1[i].y_
            c= state1[i].color_
            robots.append(Robot(c,x,y))
            
        return robots    
        
    
    def __init__(self):
        AIPlayer.__init__(self, None, None)
        
    def search(self,board,robots,target):
        finalNode = self.graph_Search(board,robots,target)
        return self.findMoves(finalNode)

    def findMoves (self,goalNode):
        
        moves = []
        currentNode = node.copyNode(goalNode)
        
        while currentNode.father_!=0:
            moves.append(currentNode.moveTuple_)
            currentNode=currentNode.father_
        for i in range(len(moves)):
            print(moves[i].robotColour_)
            print(moves[i].dir_)
        return moves 

    def graph_Search(self,board, robots,target):
        
       frontier= []
       expanded = []
       initialState= self.copyState(robots)
       initialNode = node(initialState,0,0)
       
       frontier.append(initialNode)
       
       while True:
           
           print ("Searching")
           
           currentNode = node.copyNode(frontier[0])
           del frontier[0]
           
           expanded.append(node.copyNode(currentNode))
           
           for r in currentNode.robots_:
               if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_==target.y_):
                       return currentNode
              
           
           for i in range (len(currentNode.robots_)):
                #move robot in one direction
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                
                for j in range (len(direction)):
                   
                    newNode =  node.copyNode(currentNode)
                    if currentNode.robots_[i].move_possible(board,direction[j]) :
                        tr=True
                        newNode.robots_[i].move(board,direction[j])
                        for m in range (len(frontier))  :
                            if (node.compareState(frontier[m],newNode)==True):
                                tr=False
                                break
                        for n in range(len(expanded))  :  
                            if (node.compareState(expanded[n],newNode)==True):
                                tr=False
                                break
                        if(tr):
                            #newMove = moveTuple(currentNode.robots_[i].color_,direction[j])
                            newNode.moveTuple_=moveTuple(currentNode.robots_[i].color_,direction[j])
                            newNode.father_=currentNode
                            frontier.append(node.copyNode(newNode))
                            print (len(expanded))
                        
                            
                            
                           
   
                        
                    
               