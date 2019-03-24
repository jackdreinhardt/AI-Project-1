# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:57:54 2019

@author: kilia
"""
from square import Square
class Goal_state:
    
    def __init__(self,color,x,y,level):
        self.x_ = x
        self.y_ = y
        self.color_ = color
        self.level_ = level
        
        
    def is_goal_state(self,board,robots):
        for r in robots:
            if(self.x_ == r.x_ and self.y_ == r.y_ and self.color_ == r.color_):
                if (board.square(self.y_,self.x_).number_walls() > 1):
                    return self.level_
            
        return False
    
        