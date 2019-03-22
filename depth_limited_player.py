from ai_player import *
import copy
import random

class Depth_Limited_Player(AIPlayer):
    def __init__(self):
        AIPlayer.__init__(self, 'DFS', 0)

    def search(self, board, target, robots, limit):
        moves = [] # empty list to store history of moves
        return self.recursive_DLS(board, target, robots, limit, moves)

    def recursive_DLS(self, board, target, robots, limit, moves):
        self.nodes_expanded_ += 1
        for r in robots:
          #if board[r.y_][r.x_].target_ != None and board[r.y_][r.x_].target_.color_ == r.color_:
          if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_ == r.y_):
            return moves # return solution
        if limit == 0: # if depth limit was reached
            return CUTOFF
        else:
            cutoff_occurred = False
            direction = ["NORTH", "SOUTH", "EAST", "WEST"]
            for i in range(len(robots)): # for each robot in robots
                random.shuffle(direction) # randomize order of directions
                for j in range(len(direction)): # for each direction
                    if robots[i].move_possible(board, robots, direction[j]): # check if move successful
                        if len(moves) > 0 \
                        and robots[i].color_ == moves[len(moves)-1][0] \
                        and ((direction[j] == "NORTH" and moves[len(moves)-1][1] == "SOUTH") \
                        or (direction[j] == "SOUTH" and moves[len(moves)-1][1] == "NORTH") \
                        or (direction[j] == "EAST" and moves[len(moves)-1][1] == "WEST") \
                        or (direction[j] == "WEST" and moves[len(moves)-1][1] == "EAST")):
                            break # don't allow the opposite of the previous move

                        new_robots = copy.deepcopy(robots)
                        # new_board = copy.deepcopy(board)
                        new_moves = copy.deepcopy(moves)
                        new_robots[i] = new_robots[i].move(board, new_robots, direction[j])

                        #print("Moving robot " + str(i) + " " + direction[j])
                        new_moves.append((new_robots[i].color_, direction[j])) # add move to history
                        result = self.recursive_DLS(board, target, new_robots, limit-1, new_moves)
                        if result == CUTOFF:
                            cutoff_occurred = True
                        elif result != FAILURE:
                            return result
            if cutoff_occurred:
                return CUTOFF
            else: return FAILURE
