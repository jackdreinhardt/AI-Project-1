import time
from collections import deque

from globals import *

from ai_player import AIPlayer
from node import Node

# BFS class
#
# Algorithm to find a solution to ricochet robots using BFS

class Graph_Search_BF(AIPlayer):
    def __init__(self):
        AIPlayer.__init__(self, 'Breadth First Search', 0)
        self.nodes_expanded_ = 0

    def search(self, board, target, robots, limit, heuristic):
        self.start_time = time.time()
        return self.graph_search(board, target, robots, limit, heuristic)      

    def graph_search(self, board, target, robots, limit, heuristic):
       initialNode = Node(robots, 0, 0, 0, 0,0)
       frontier = deque([initialNode])
       expanded = deque()
       
       for r in robots:     
            if initialNode.is_goal_state(r, target):
                return initialNode
       while True:
           if len(frontier) == 0:
               return DEPTH_CUTOFF
           if time.time() - self.start_time > CUTOFF_TIME:
               return TIME_CUTOFF

           currentNode = frontier.popleft()
           expanded.append(currentNode)
           self.nodes_expanded_ += 1
           
           for i in range(len(currentNode.robots_)):
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                for j in range (len(direction)):
                    if currentNode.robots_[i].move_possible(board,currentNode.robots_,direction[j]):
                        newNode = currentNode.copyNode()
                        newNode.robots_[i] = newNode.robots_[i].move(board,currentNode.robots_,direction[j])
                        newNode.move_tuple_ = (COLORS[i], direction[j])
                        newNode.father_ = currentNode
                        newNode.level_+=1
                        if newNode.is_goal_state(newNode.robots_[i], target):
                            return newNode.get_solution()
                             
                        unique_node=True
                        # check if newNode is already in frontier
                        for m in range(len(frontier)):
                            if newNode.compareState(frontier[m]):
                                unique_node = False
                                break
                        # check if newNode has already been expanded
                        for n in range(len(expanded)):
                            if newNode.compareState(expanded[n]):
                                unique_node = False
                                break
                        if unique_node and newNode.level_ < limit: frontier.append(newNode)
             
                     
                            
                        
                        
                        
                           
   
                        
                    
               
