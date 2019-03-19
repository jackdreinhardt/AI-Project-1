class Square(object): 
    def __init__(self): 
        self.wall_north_ = False 
        self.wall_east_ = False 
        self.wall_south_ = False
        self.wall_west_ = False

    def Wall(self, direction):
        if direction == NORTH:
            self.north_ = True
        elif direction == SOUTH:
            self.south_ = True
        elif direction == EAST:
            self.east_ = True
        elif direction == WEST:
            self.south_ = True
