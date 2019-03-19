from player import Player

class AIPlayer(Player):
  def __init__(self, name, score):
      Player.__init__(self, name, score)

  # moves is an array of (robot, direction) pairs
  #   robot: an instance of the Robot class
  #   direction: a string, "NORTH" "SOUTH" "EAST" or "WEST"
  def execute_moves(self, board, moves):
    for i in moves:
      i[0].move(board, i[1])

  def search(self, board, robots, limit):
    return [(robots[0], "NORTH")]
