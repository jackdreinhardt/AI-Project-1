from player import Player

class AIPlayer(Player):
  def __init__(self, name, score):
      Player.__init__(self, name, score)

  # moves is an array of (robot, direction) pairs
  #   robot: an instance of the Robot class
  #   direction: a string, "NORTH" "SOUTH" "EAST" or "WEST"
  # vel is a temporary parameter, we will find a way to avoid passing it
  # board is also a temporary parameter, we will include it as a member variable
  def execute_moves(self, board, moves, vel):
    for i in moves:
      i[0].move(board, i[1])
        

  def search(self, board, robots):
    return [(robots[0], "NORTH")]
