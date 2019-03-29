from ai_player import *

from node import Node

class Advanced_AI_Player(AIPlayer):
    def __init__(self):
        AIPlayer.__init__(self, 'AAI', 0)
        
    def search(self, board, target, robots, limit, heuristic=None):
        moves = [] # empty list to store history of moves
        self.start_time = time.time()
        for r in robots:
            if target.color_ == r.color_:
                print(r)
                currentRobot = r
        solution = self.recursive_DLS(board, target, robots, limit, moves, currentRobot)
        if (solution != FAILURE and solution != DEPTH_CUTOFF and solution != TIME_CUTOFF):
            new_solution = self.optimize_solution(board, target, robots, solution)
            print("removed " + str(len(solution)-len(new_solution)) + " moves")
            return new_solution
        else: return solution

    def optimize_solution(self, board, target, robots, solution):
        solution_len = len(solution)
        minimal_solution = copy.deepcopy(solution)
        for i in range(solution_len-1):
            solution = copy.deepcopy(minimal_solution)
            reached_goal = False
            if (solution_len-i-2 >= 0):
                del solution[solution_len-i-2]
            else:
                break
            new_robots = copy.deepcopy(robots)
            for m in solution: # for each move
                for i in range(len(new_robots)): # for each robot
                    if new_robots[i].color_ == m[0]: # check if robot matches
                        new_robots[i] = new_robots[i].move(board, new_robots, m[1])
                for r in new_robots: # goal test
                  if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_ == r.y_):
                    reached_goal = True
            if reached_goal: minimal_solution = copy.deepcopy(solution) # reaches goal state - update minimal solution
        return minimal_solution

    def recursive_DLS(self, board, target, robots, limit, moves, currentRobot):
        self.nodes_expanded_ += 1
        for r in robots:
          if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_ == r.y_):
            return moves # return solution
        if (time.time() - self.start_time > CUTOFF_TIME):
            return TIME_CUTOFF
        if limit == 0: # if depth limit was reached
            return DEPTH_CUTOFF
        else:
            cutoff_occurred = False
            time_cutoff_occurred = False
            direction = ["NORTH", "SOUTH", "EAST", "WEST"]
        #for i in range(len(robots)): # for each robot in robots
            random.shuffle(direction) # randomize order of directions
            for j in range(len(direction)): # for each direction
                if currentRobot.move_possible(board, robots, direction[j]): # check if move successful
                    if len(moves) > 0 \
                    and currentRobot.color_ == moves[len(moves)-1][0] \
                    and ((direction[j] == "NORTH" and moves[len(moves)-1][1] == "SOUTH") \
                    or (direction[j] == "SOUTH" and moves[len(moves)-1][1] == "NORTH") \
                    or (direction[j] == "EAST" and moves[len(moves)-1][1] == "WEST") \
                    or (direction[j] == "WEST" and moves[len(moves)-1][1] == "EAST")):
                        break # don't allow the opposite of the previous move

                    new_robots = copy.deepcopy(robots)
                    # new_board = copy.deepcopy(board)
                    new_moves = copy.deepcopy(moves)
                    for i in range(len(robots)):
                        if new_robots[i].color_ == currentRobot.color_:
                            newRobot = new_robots[i]
                    newRobot = newRobot.move(board, new_robots, direction[j])

                    #print("Moving robot " + str(i) + " " + direction[j])
                    new_moves.append((currentRobot.color_, direction[j])) # add move to history
                    result = self.recursive_DLS(board, target, new_robots, limit-1, new_moves)
                    if result == DEPTH_CUTOFF:
                        cutoff_occurred = True
                    elif result == TIME_CUTOFF:
                        time_cutoff_occurred = True
                    elif result != FAILURE:
                        return result
        if time_cutoff_occurred:
            return TIME_CUTOFF
        if cutoff_occurred:
            return DEPTH_CUTOFF
        else: return FAILURE
     
        
        
        
        
        

# =============================================================================
#     def search(self, board, target, robots, limit):
#         robotWalls = self.graph_search(board, target, robots)
#         print("robot Walls")
#         for i in range(len(robotWalls)):
#             print(robotWalls[i])
#         newGoals = self.backtrack(board, target, robots, robotWalls)
#         print("new goal states" , newGoals)
#         finalNode = self.graph_search2(board, target, robots, newGoals) #Very similar to graph_search. Definitely combine them in the future
#         pathNewGoal =  Node.get_solution(finalNode) 
#         solution = CombinePaths(pathNewGoal)
#         return solution
#         
# 
#     def find_min_index(self, frontier):
#         min_index = 0
#         min_cost = float("inf")
#         for i in range(len(frontier)):
#             if (frontier[i].get_cost() < min_cost):
#                 min_index = i
#                 min_cost = frontier[i].get_cost()
#         return min_index
#     
# 
#     def graph_search(self, board, target, robots):
#         frontier = []
#         expanded = []
#         robotWalls = []
#         initialState = copy.deepcopy(robots)
#         initialNode = Node(initialState, 0, 0, 0, 0)
#         frontier.append(initialNode)
#         for r in robots:
#             if target.color_ != r.color_:
#                 robotWalls.append((r.y_,r.x_))
#         direction = ["NORTH", "SOUTH", "EAST", "WEST"]
# 
#         for i in range(len(robots)):
#             cutoff = 5
#             while cutoff > 0:
#                 if (len(frontier) == 0):
#                     return FAILURE
#     
#                 # remove node at top of priority queue
#                 min_index = self.find_min_index(frontier)
#                 currentNode = Node.copyNode(frontier[min_index])
#                 del frontier[min_index]
#                 expanded.append(Node.copyNode(currentNode))
#                 
#                 print(currentNode.robots_[i].color_)
#                 if target.color_ != currentNode.robots_[i].color_:
#                     print("Hi")
#                     for j in range (len(direction)): # for each direction
#                         if (currentNode.robots_[i].move_possible(board, currentNode.robots_, direction[j])): # check if valid move
#                             newNode = Node.copyNode(currentNode)
#                             unique_node = True
#                             newNode.robots_[i] = newNode.robots_[i].move(board, newNode.robots_, direction[j])
#     
#                             #print("Moving robot " + str(i) + " " + direction[j] + " at depth " + str(newNode.g_))
#                             newNode.move_tuple_ = (i, direction[j])
#                             newNode.father_ = currentNode
#                             
#                             if (newNode.robots_[i].y_, newNode.robots_[i].x_) in robotWalls:
#                                 pass
#                             else:
#                                 robotWalls.append((newNode.robots_[i].y_, newNode.robots_[i].x_, newNode.robots_[i].color_, direction[j]))
#     
#                             for m in range (len(frontier)): # check if newNode is already in frontier
#                                 if (Node.compareState(frontier[m],newNode)==True):
#                                     unique_node = False
#                                     break
#                             for n in range(len(expanded)): # check if newNode has already been expanded
#                                 if (Node.compareState(expanded[n],newNode)==True):
#                                     unique_node = False
#                                     break
#                             if(unique_node): 
#                                 frontier.append(Node.copyNode(newNode))
#                 cutoff -= 1
#         return robotWalls
#     
#         
#     def backtrack(self, board, target, robots, robotWalls):
#         ###
#         # The last square is not added to newGoals because the while loop will be True at that point
#         ###
#         newGoals = []
#         
#         if board.square(target.y_, target.x_).wall_north_ == True:
#             i = target.y_
#             j = target.x_
#             tr=True
#             while tr: #Note: not checking for other robots in the way, might wanna change that (or modify: add 1 move when travelling "through" a robot)
#                 if (i,j-1) in robotWalls or (i,j+1) in robotWalls:
#                     newGoals.append((i, j))
#                 i += 1
#                 if board.square(i,j).wall_south_ == True:
#                     tr = False
#         if board.square(target.y_, target.x_).wall_south_ == True:
#             i = target.y_
#             j = target.x_
#             tr=True
#             while tr: #Note: not checking for other robots in the way, might wanna change that (or modify: add 1 move when travelling "through" a robot)
#                 if (i,j-1) in robotWalls or (i, j+1) in robotWalls:
#                     newGoals.append((i, j))                  
#                 i -= 1
#                 if board.square(i,j).wall_north_ == True:
#                     tr = False
#         if board.square(target.y_, target.x_).wall_east_ == True:
#             i = target.y_
#             j = target.x_
#             tr=True
#             while tr: #Note: not checking for other robots in the way, might wanna change that (or modify: add 1 move when travelling "through" a robot)
#                 if (i-1,j) in robotWalls or (i+1,j) in robotWalls:
#                     newGoals.append((i, j))
#                 j -= 1
#                 if board.square(i, j).wall_west_ == True:
#                     tr = False
#         if board.square(target.y_, target.x_).wall_west_ == True:
#             i = target.y_
#             j = target.x_
#             tr=True
#             while tr: #Note: not checking for other robots in the way, might wanna change that (or modify: add 1 move when travelling "through" a robot)
#                 if (i-1,j) in robotWalls or (i+1,j) in robotWalls:
#                     newGoals.append((i, j))
#                 j += 1
#                 if board.square(i, j).wall_east_ == True:
#                     tr = False
#         return newGoals
#     
#     
#     
#     def graph_search2(self, board, target, robots, newGoals):
#         frontier = []
#         expanded = []
#         initialState = copy.deepcopy(robots)
#         initialNode = Node(initialState, 0, 0, 0, 0)
#         frontier.append(initialNode)
#         cutoff = 10
# 
#         for r in robots:
#             if target.color_ == r.color_:
#                 while cutoff > 0:
#                     if (len(frontier) == 0):
#                         return FAILURE
#         
#                     # remove node at top of priority queue
#                     min_index = self.find_min_index(frontier)
#                     currentNode = Node.copyNode(frontier[min_index])
#                     del frontier[min_index]
#                     expanded.append(Node.copyNode(currentNode))
# 
#                     direction = ["NORTH", "SOUTH", "EAST", "WEST"]
#                     for i in range(len(robots)):
#                         if currentNode.robots_[i].color_ == r.color_:
#                              x = currentNode.robots_[i]
#                     for j in range (len(direction)): # for each direction
#                         if (x.move_possible(board, robots, direction[j])): # check if valid move
#                             cutoff -= 1
#                             newNode = Node.copyNode(currentNode)
#                             unique_node = True
#                             newNode.robots_[i] = newNode.robots_[i].move(board, robots, direction[j])
#                     
#                             #print("Moving robot " + str(i) + " " + direction[j] + " at depth " + str(newNode.g_))
#                             newNode.move_tuple_ = (i, direction[j])
#                             newNode.father_ = currentNode
#                             
#                             for m in range (len(frontier)): # check if newNode is already in frontier
#                                 if (Node.compareState(frontier[m],newNode)==True):
#                                     unique_node = False
#                                     break
#                             for n in range(len(expanded)): # check if newNode has already been expanded
#                                 if (Node.compareState(expanded[n],newNode)==True):
#                                     unique_node = False
#                                     break
#                             if(unique_node): frontier.append(Node.copyNode(newNode))
# 
#                     robotPosition = (newNode.robots_[i].y_, newNode.robots_[i].x_)
#                     print(robotPosition)
#                     if robotPosition in newGoals:
#                         print("Success")
#                         return currentNode
#         return FAILURE
#     
#     
#     #def CombinePaths(pathNewGoal):
# =============================================================================
        
        
        
        
        
        