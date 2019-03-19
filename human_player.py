from player import Player
from RicochetRobots import KeyToDir, board, vel

# not implemented correctly
class HumanPlayer(Player):
    def execute_moves(self, board, moves, vel):
        for event in pygame.event.get():                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = event.pos
                currentRobo = DetermineRobo(click)
            if event.type == pygame.KEYDOWN and currentRobo != 0:
                currentRobo.move(board, KeyToDir(event.key))

  # since the user is playing the game, no search algorithm is needed
  def search(self, board, robots, limit):
    return
