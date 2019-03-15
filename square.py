class Square(object): 
  def __init__(self): 
    self.north_ = False 
    self.east_ = False 
    self.south_ = False
    self.west_ = False
    self.target_ = None
    self.robot_ = None
    # We always provide both, robots and board, that avoids saving information twice

  def Wall(self, direction):
    if direction == 1:
      self.north = True
    elif direction == 2:
      self.south = True
    elif direction == 3:
      self.east = True
    elif direction == 4:
      self.south = True
