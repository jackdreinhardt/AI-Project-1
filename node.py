# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:35:17 2019

@author: kilia
"""
import copy
from robot import Robot

class Node:

# =============================================================================
#     def __init__(self, robots, father, movetuple):
#         self.robots_ = robots
#         self.father_ = father
#         self.move_tuple_ = movetuple # what robot was moved to what direction
# =============================================================================

    def __init__(self, robots, father, movetuple, g=0, h=0):
        self.robots_ = robots
        self.father_ = father
        self.move_tuple_ = movetuple # what robot was moved to what direction
        self.g_ = g # g(n)
        self.h_ = h # heuristic
        self.children_ = []

    def get_cost(self):
        return self.g_ + self.h_

    @staticmethod
    def get_solution(node):
        solution = []
        current = node
        while (current.father_ != 0):
            solution.insert(0, current.move_tuple_)
            current = current.father_
        return solution

    @staticmethod
    def compareState(state1, state2):
        for i in range(len(state1.robots_)):
            
            if (state1.robots_[i].color_ == state2.robots_[i].color_ and state1.robots_[i].x_ == state2.robots_[i].x_  and state1.robots_[i].y_ == state2.robots_[i].y_):
                #states are e
                return False
        return True
    
    
    # assuming both nodes having the same order of robots and it's colors
    # returns True if the nodes robots are exactly the same
    @staticmethod 
    def compare_robots(node_1,node_2):
        for i in range(len(node_1.robots_)):
            if ( node_1.robots_[i].x_ != node_2.robots_[i].x_ or node_1.robots_[i].y_ != node_2.robots_[i].y_):
                return False
        return True    
                

    def get_level(self):
        current = self
        output = 0
        while (current.father_ != 0):
            output += 1
            current = current.father_
        return output

    @staticmethod
    def copyNode(oldNode):
        mt = copy.deepcopy(oldNode.move_tuple_)
        father = copy.deepcopy(oldNode.father_)
        robots =[]
        for r in oldNode.robots_:
            robots.append (Robot(r.color_,r.x_,r.y_))
        return Node(robots,father,mt,0,0)
    

    
    
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
    @staticmethod        
    def move_robot(node_input,r_color,new_x,new_y):
        new_node = Node.copyNode(node_input)
        for r in new_node.robots_:
            if(r.color_==r_color):
                r.x_=new_x
                r.y_=new_y
        return new_node        
            
        
