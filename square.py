class Square(object): 
    def __init__(self): 
        self.wall_north_ = False 
        self.wall_east_ = False 
        self.wall_south_ = False
        self.wall_west_ = False
        
        
    def number_walls(self):
        
        n =0
        if (self.wall_north_): n=n+1
        if self.wall_east_: n+=1
        if self.wall_south_: n+=1
        if self.wall_west_: n+=1
        
        return n