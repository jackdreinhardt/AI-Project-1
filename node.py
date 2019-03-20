# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:35:17 2019

@author: kilia
"""
import copy

class Node:
    
    
        
    def __init__(self,robots,father, movetuple):
        self.robots_=robots
        self.father_=father
        self.move_tuple_=movetuple #what robot was moved to what direction
        
    @staticmethod    
    def compareState(state1,state2):
        
        t=True
        for i in range(len(state1.robots_)):
                if (state1.robots_[i].color_!=state2.robots_[i].color_) or (state1.robots_[i].x_!=state2.robots_[i].x_ ) or (state1.robots_[i].y_!=state2.robots_[i].y_):
                    t=False
        return t           
            
    
    def get_level(self):
        current = self
        output=0
        while (current.father_!=0):
            output=output+1
            current=current.father_
        return output
                 
            
    
        
    @staticmethod 
    def copy_node(oldNode):
        
        return copy.deepcopy(oldNode)
    
    
    @staticmethod
    def find_moves(goalNode):
        moves = []
        currentNode = (goalNode)
        
        while currentNode.father_!=0:
            moves.insert(0,currentNode.move_tuple_)
            currentNode=currentNode.father_
        
        return moves 
    @staticmethod
    def print_moves(goalNode):
        
        if (goalNode == "FAILURE"):
            return False
        else:
            
        
            n = Node.copy_node(goalNode)
            while True:
                color = goalNode.move_tuple_.robotColour_
                c=""
                if (color == (255,0,0)):
                    c="red"
                if (color ==(255,255,0)):
                    c="yellow"
                if (color ==(0,255,0)):
                    c= "green"
                if (color ==(0,0,255)):
                    c= "blue"
                
                direction = goalNode.move_tuple_.dir_
                
                print(c,direction)
                n = Node.copy_node(n.father_)  
                if n.move_tuple.dir_==None:
                    return True
            
            
        