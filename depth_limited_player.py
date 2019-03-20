from ai_player import AIPlayer
import copy
import random

SUCCESS = "SUCCESS"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

class Depth_Limited_Player:
    def __init__(self):
        AIPlayer.__init__(self, None, None, None)

    def search(self, board, target, robots, limit):
        moves = [] # empty list to store history of moves
        return self.recursive_DLS(board, target, robots, limit, moves)

    def recursive_DLS(self, board, target, robots, limit, moves):
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
                        and i == moves[len(moves)-1][0] \
                        and ((direction[j] == "NORTH" and moves[len(moves)-1][1] == "SOUTH") \
                        or (direction[j] == "SOUTH" and moves[len(moves)-1][1] == "NORTH") \
                        or (direction[j] == "EAST" and moves[len(moves)-1][1] == "WEST") \
                        or (direction[j] == "WEST" and moves[len(moves)-1][1] == "EAST")):
                            break # don't allow the opposite of the previous move

                        new_robots = copy.deepcopy(robots)
                        new_board = copy.deepcopy(board)
                        new_moves = copy.deepcopy(moves)
                        new_robots[i] = new_robots[i].move(new_board, new_robots, direction[j])

                        print("Moving robot " + str(i) + " " + direction[j])
                        new_moves.append((i, direction[j])) # add move to history
                        result = self.recursive_DLS(new_board, target, new_robots, limit-1, new_moves)
                        if result == CUTOFF:
                            cutoff_occurred = True
                        elif result != FAILURE:
                            return result
            if cutoff_occurred:
                return CUTOFF
            else: return FAILURE
