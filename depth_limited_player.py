from ai_player import AIPlayer

SUCCESS = "SUCCESS"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

class Depth_Limited_Player:
    def __init__(self):
        AIPlayer.__init__(self, None, None)

    def search(self, board, robots, limit):
        moves = [] # empty list to store history of moves
        return self.recursive_DLS(board, robots, limit, moves)

    def recursive_DLS(self, board, robots, limit, moves):
        for r in robots:
          if board[r.y_][r.x_].target_ != None and board[r.y_][r.x_].target_.color_ == r.color_:
            return moves # return solution
        if limit == 0: # if depth limit was reached
            return CUTOFF
        else:
            cutoff_occurred = False
            direction = ["NORTH", "SOUTH", "EAST", "WEST"]
            for i in range(len(robots)): # for each robot in robots
                for j in range(len(direction)): # for each direction
                    if robots[i].move(board, direction[j]): # check if move successful
                        #print("Moving robot " + str(i) + " " + direction[j])
                        new_robots = robots
                        moves.append((i, direction[j])) # add move to history
                        result = self.recursive_DLS(board, new_robots, limit-1, moves)
                        if result == CUTOFF:
                            cutoff_occurred = True
                        elif result != FAILURE:
                            return result
            if cutoff_occurred:
                return CUTOFF
            else: return FAILURE
