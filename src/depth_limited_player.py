import time
import copy
from random import shuffle

from globals import *

from ai_player import AIPlayer

# DFS class
#
# Algorithm to find a solution to ricochet robots using recursive DFS tree search

class Depth_Limited_Player(AIPlayer):
    def __init__(self):
        AIPlayer.__init__(self, 'Depth First Search', 0)

    def search(self, board, target, robots, limit, heuristic=None):
        moves = [] # empty list to store history of moves
        self.start_time = time.time()
        solution = self.recursive_DLS(board, target, robots, limit, moves)
        if solution != FAILURE and solution != DEPTH_CUTOFF and solution != TIME_CUTOFF:
            solution = self.optimize_solution(board, target, robots, solution)
        return solution

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

    def recursive_DLS(self, board, target, robots, limit, moves):
        self.nodes_expanded_ += 1
        for r in robots:
          if target.color_ == r.color_ and target.x_ == r.x_ and target.y_ == r.y_:
            return moves # return solution
        if time.time() - self.start_time > CUTOFF_TIME:
            return TIME_CUTOFF
        if limit == 0: # if depth limit was reached
            return DEPTH_CUTOFF
        else:
            cutoff_occurred = False
            time_cutoff_occurred = False
            direction = ["NORTH", "SOUTH", "EAST", "WEST"]
            for i in range(len(robots)): # for each robot in robots
                shuffle(direction) # randomize order of directions
                for j in range(len(direction)): # for each direction
                    if robots[i].move_possible(board, robots, direction[j]): # check if move successful
                        if len(moves) > 0 \
                            and robots[i].color_ == moves[len(moves)-1][0] \
                            and ((direction[j] == "NORTH" and moves[len(moves)-1][1] == "SOUTH") \
                            or (direction[j] == "SOUTH" and moves[len(moves)-1][1] == "NORTH") \
                            or (direction[j] == "EAST" and moves[len(moves)-1][1] == "WEST") \
                            or (direction[j] == "WEST" and moves[len(moves)-1][1] == "EAST")):
                            break # don't allow the opposite of the previous move

                        new_robots = copy.copy(robots)
                        new_moves = copy.copy(moves)
                        new_robots[i] = new_robots[i].move(board, new_robots, direction[j])

                        new_moves.append((new_robots[i].color_, direction[j])) # add move to history
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
