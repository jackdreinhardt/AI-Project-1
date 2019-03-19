# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:39:24 2019

@author: kilia
"""

from ai_player import AIPlayer

CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

class node:
    def __init__(self,robots,father):
        self.
class moveTuple:
    def __init__(self,robot,direction):
        self.robot_ = robot
        self.dir_= direction
        
class gameState:
    def __init__(self,robots,executedMoves) :
        self.robots_=robots
        self.moves_=executedMoves
        

class Graph_Search_BF:
    
    def __init__(self, thing,score):
        self.thing_ = thing
        AIPlayer.__init__(self, thing,score)
        self.frontier_ = None

    

    def graph_Search(self,board, robots):
        
       frontier= []
       expanded = []
       moves = []
       initialState = gameState(robots,moves)
       frontier.append(initialState)
       
       while True:
          
           currentState = frontier[0]
           del frontier[0]
           print("HELLO")
           expanded.append(currentState)
           
           for i in range (len(robots)):
               if board[currentState.robots_[i].x_][currentState.robots_[i].y_].target_!=None:
                   return currentState.moves_
              
           
           for i in range (len(robots)):
                #move robot in one direction
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                
                for j in range (len(direction)):
                    currentGameState= gameState(robots,moves)
                    if robots[i].moveRobot(board,direction[j],currentGameState.robots_[i]) :
                        for m in range (len(frontier))  :
                            if frontier[m].robots_==currentGameState.robots_:
                                break
                        for n in range(len(expanded))  :  
                            if expanded[n].robots_==currentGameState.robots_:
                                break
                        newMove = moveTuple(i,j)
                        currentGameState.moves_.append(newMove)
                        frontier.append(currentGameState)
                        print("hi")
                            
                            
                            
   
                        
                    
               
      
           
