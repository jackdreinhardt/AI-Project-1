# Square class
#
# Simple object to represent each space in the board. Includes the variables
# needed to represent the walls on each board space

class Square(object): 
    def __init__(self): 
        self.wall_north_ = False 
        self.wall_east_ = False 
        self.wall_south_ = False
        self.wall_west_ = False