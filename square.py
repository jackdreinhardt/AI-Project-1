class Square(object): 
  def __init__(self, North, East, South, West, Occupied, Target): 
    self.north = North 
    self.east = East 
    self.south = South 
    self.west = West
    self.occ = Occupied
    self.tar = Target
# We always provide both, robots and board, that avoids saving information twice