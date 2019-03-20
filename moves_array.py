# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:56:54 2019

@author: kilia
"""

class Moves_node:
    
    
        
    def __init__(self):
        self.moves_ = []
        
    
    def add_move(self,robot,dir):
        self.moves_.append([robot,dir])        
            
    
    def copy(self):
        retr = Moves_node()
        for elements in self.moves_:
            m= elements[0]
            n= elements[1]
            retr.add_move(m,n)
            
        return retr     