from player import Player

# not implemented correctly
class HumanPlayer(Player):
  # pure virtual, implemented by child class
  def execute_moves():
    for event in pygame.event.get():                    
      if event.type == pygame.QUIT:  
        pygame.display.quit()                 
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        click = event.pos  
        currentRobo = DetermineRobo(click)
      if event.type == pygame.KEYDOWN and currentRobo != 0:
        key = event.key
        RoboMove = RoboMoves(currentRobo, key)
    

  # since the user is playing the game, no search algorithm is needed
  def compute_moves():
    return
