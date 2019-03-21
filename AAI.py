from ai_player import *
import copy
import random

from stack import Stack
from node import Node

class Actual_AI_Player:
    def __init__(self):
        AIPlayer.__init__(self, None, None, None)

    def search(self, board, target, robots, limit):
        traverse = Stack()
        positions = Stack()
        for r in robots:
            if target.color_ != r.color_:
                positions.push(self.dfs(board, robots, limit, traverse))    

    
    def dfs(self, board, robots, limit, traverse):
        positions.push((r.x_, r.y_))
        traverse.push((r.x_, r.y_))
        direction = ["NORTH", "SOUTH", "EAST", "WEST"]
        if limit == 0:
            return positions
        else:
            for i in range(len(direction)):
                if robots.move_possible(board, robots, direction[i]):
                    move(board, robots, direction[i])
                    dfs(board, robots, limit-1, traverse)
        
        



        
        
        
    
        
        
        
        
        
        
        
                for r in robots:
            if target.color_ != r.color_:
                cutoff_occurred = False
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                stack = [(r.x_, r.y_)]
                visited = [(r.x_, r.y_)]
                while stack != empty
                    for i in range(len(direction)):
                        if xxx != in visited:
                            add xxx to stack
        
