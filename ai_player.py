from player import Player

SUCCESS = "SUCCESS"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

class AIPlayer(Player):
  def __init__(self, name, score, board):
      Player.__init__(self, name, score, board)

  # moves is an array of (robot, direction) pairs
  #   robot: an instance of the Robot class
  #   direction: a string, "NORTH" "SOUTH" "EAST" or "WEST"
  def search(self, board, robots, limit):
    return None
