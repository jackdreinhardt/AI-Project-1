import ai_player.py

CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

class Depth_Limited_Player:
    def __init__(self, thing):
        self.thing_ = thing
        AIPlayer.__init__(self, thing)

    def search(board, robots, limit):
        moves = [] # empty list to store history of moves
        recursive_DLS(board, robots, limit, moves)

    def recursive_DLS(board, robots, limit, moves):
        if board[i][j].occ == board[i][j].tar and board[i][j].occ != 0: # if solution was found
            return moves # return solution
        elif limit == 0 # if depth limit was reached
            return CUTOFF
        else
            cutoff_occurred = False
            direction = ["NORTH", "SOUTH", "EAST", "WEST"]
            for i in range(len(robots)): # for each robot in robots
                for j in range(len(direction)): # for each direction
                    if robots[i].move(board, direction[j]): # check if move successful
                        moves.append((robots[i], direction[j]) # add move to history
                        result = recursive_DLS(board, robots, limit-1, moves)
                        if result == CUTOFF:
                            cutoff_occurred = True
                        elif result != FAILURE:
                            return result
            if cutoff_occurred:
                return CUTOFF
            else return FAILURE
