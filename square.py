class Square(object): 
  def __init__(self): 
    self.north_ = False 
    self.east_ = False 
    self.south_ = False
    self.west_ = False
    self.target_ = None
    self.robot_ = None

  def Wall(self, direction):
    if direction == NORTH:
      self.north_ = True
    elif direction == SOUTH:
      self.south_ = True
    elif direction == EAST:
      self.east_ = True
    elif direction == WEST:
      self.south_ = True
