import random

from square import Square
from globals import BOARDSIZE

class Board:
    def __init__(self):
        self.board_ = [[Square() for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]
        

        

#        # map.target_locations
#        red = [(1,5),(5,9),(9,5),(11,13)]
#        blue = [(2,1),(2,14),(12,6),(14,14)]
#        green = [(1,12),(6,2),(13,9),(14,2)]
#        yellow = [(4,6),(6,11),(9,1),(10,8)]


   

    def PlaceRobots(self,robots):
        for r in robots:
            self.board_[r.y_][r.x_].robot_ = r

    def PlaceWalls(self,boardsize):
        
        if (boardsize==16):
            
            # outer walls
            for i in range(BOARDSIZE):
                self.board_[0][i].wall_north_ = 1
                self.board_[15][i].wall_south_ = 1
                self.board_[i][0].wall_west_ = 1
                self.board_[i][15].wall_east_ = 1
    
            # Add inner square walls
            self.board_[6][7].wall_south_ = self.board_[6][8].wall_south_ = 1
            self.board_[7][6].wall_east_ = self.board_[8][6].wall_east_ = 1
            self.board_[7][9].wall_west_ = self.board_[8][9].wall_west_ = 1
            self.board_[9][7].wall_north_ = self.board_[9][8].wall_north_ = 1
    
            # Add vertical walls
            self.board_[0][3].wall_east_ = self.board_[0][4].wall_west_ = 1
            self.board_[0][10].wall_east_ = self.board_[0][11].wall_west_ = 1
            self.board_[1][5].wall_east_ = self.board_[1][6].wall_west_ = 1
            self.board_[1][11].wall_east_ = self.board_[1][12].wall_west_ = 1
            self.board_[2][0].wall_east_ = self.board_[2][1].wall_west_ = 1
            self.board_[2][13].wall_east_ = self.board_[2][14].wall_west_ = 1
            self.board_[3][7].wall_east_ = self.board_[3][8].wall_west_ = 1
            self.board_[4][6].wall_east_ = self.board_[4][7].wall_west_ = 1
            self.board_[5][9].wall_east_ = self.board_[5][10].wall_west_ = 1
            self.board_[6][2].wall_east_ = self.board_[6][3].wall_west_ = 1
            self.board_[6][11].wall_east_ = self.board_[6][12].wall_west_ = 1
            self.board_[9][1].wall_east_ = self.board_[9][2].wall_west_ = 1
            self.board_[9][4].wall_east_ = self.board_[9][5].wall_west_ = 1
            self.board_[10][8].wall_east_ = self.board_[10][9].wall_west_ = 1
            self.board_[11][12].wall_east_ = self.board_[11][13].wall_west_ = 1
            self.board_[12][6].wall_east_ = self.board_[12][7].wall_west_ = 1
            self.board_[13][8].wall_east_ = self.board_[13][9].wall_west_ = 1
            self.board_[14][1].wall_east_ = self.board_[14][2].wall_west_ = 1
            self.board_[14][14].wall_east_ = self.board_[14][15].wall_west_ = 1
            self.board_[15][5].wall_east_ = self.board_[15][6].wall_west_ = 1
            self.board_[15][11].wall_east_ = self.board_[15][12].wall_west_ = 1

            

            # Add horizontal walls
            self.board_[0][5].wall_south_ = self.board_[1][5].wall_north_ = 1
            self.board_[0][12].wall_south_ = self.board_[1][12].wall_north_ = 1
            self.board_[2][1].wall_south_ = self.board_[3][1].wall_north_ = 1
            self.board_[2][14].wall_south_ = self.board_[3][14].wall_north_ = 1
            self.board_[3][0].wall_south_ = self.board_[4][0].wall_north_ = 1
            self.board_[3][8].wall_south_ = self.board_[4][8].wall_north_ = 1
            self.board_[4][6].wall_south_ = self.board_[5][6].wall_north_ = 1
            self.board_[4][15].wall_south_ = self.board_[5][15].wall_north_ = 1
            self.board_[5][9].wall_south_ = self.board_[6][9].wall_north_ = 1
            self.board_[5][11].wall_south_ = self.board_[6][11].wall_north_ = 1
            self.board_[6][2].wall_south_ = self.board_[7][2].wall_north_ = 1
            self.board_[8][1].wall_south_ = self.board_[9][1].wall_north_ = 1
            self.board_[8][5].wall_south_ = self.board_[9][5].wall_north_ = 1
            self.board_[9][15].wall_south_ = self.board_[10][15].wall_north_ = 1
            self.board_[10][0].wall_south_ = self.board_[11][0].wall_north_ = 1
            self.board_[10][8].wall_south_ = self.board_[11][8].wall_north_ = 1
            self.board_[10][13].wall_south_ = self.board_[11][13].wall_north_ = 1
            self.board_[12][6].wall_south_ = self.board_[13][6].wall_north_ = 1
            self.board_[13][9].wall_south_ = self.board_[14][9].wall_north_ = 1
            self.board_[13][14].wall_south_ = self.board_[14][14].wall_north_ = 1
            self.board_[14][2].wall_south_ = self.board_[15][2].wall_north_ = 1
        
        if (boardsize==6):
        
        # outer walls
            for i in range(boardsize):
                self.board_[0][i].wall_north_ = 1
                self.board_[boardsize-1][i].wall_south_ = 1
                self.board_[i][0].wall_west_ = 1
                self.board_[i][boardsize-1].wall_east_ = 1

            # Add inner square walls
            self.board_[1][2].wall_south_ = self.board_[1][3].wall_south_ = 1
            
            self.board_[3][2].wall_south_ = self.board_[3][3].wall_south_ = 1
            
            self.board_[2][2].wall_north_ = self.board_[2][3].wall_north_ = 1
            
            self.board_[4][2].wall_north_ = self.board_[4][3].wall_north_ = 1
            
            
            self.board_[2][1].wall_east_=self.board_[2][2].wall_west_=1
            self.board_[3][1].wall_east_=self.board_[3][2].wall_west_=1
            self.board_[2][3].wall_east_=self.board_[2][4].wall_west_=1
            self.board_[3][3].wall_east_=self.board_[3][4].wall_west_=1
            
                
            self.board_[1][0].wall_east_= self.board_[2][0].wall_north_=1
            self.board_[1][0].wall_east_=self.board_[1][1].wall_west_=1
            self.board_[3][0].wall_south_=self.board_[3][1].wall_north_=1
            self.board_[4][3].wall_south_=self.board_[5][3].wall_north_=1
            
            
            self.board_[4][1].wall_east_=self.board_[4][2].wall_west_=1
            self.board_[1][1].wall_east_=self.board_[1][2].wall_west_=1
            self.board_[0][4].wall_east_=self.board_[0][5].wall_west_=1
            self.board_[3][4].wall_east_=self.board_[3][5].wall_west_=1
            self.board_[5][2].wall_east_=self.board_[5][3].wall_west_=1
        
        
        
                
            

    # def PlaceWalls2(self):
        #   # outer walls
        #   for i in range(16):
        #     self.board_[0][i].north = 1
        #     self.board_[15][i].south_ = 1
        #     self.board_[i][0].west = 1
        #     self.board_[i][15].east = 1

        #   # inner walls
        #   center_north = [(9,7),(9,8)]
        #   center_south_ = [(6,7),(6,8)]
        #   center_east = [(7,6),(8,6)]
        #   center_west = [(7,9),(8,9)]

        #   center = (center_north, center_south_, center_east, center_west)

        #   d = 0
        #   for direction in center:
        #     d += 1
        #     for wall_location in direction:
        #       print(wall_location)
        #       self.PlaceWall(wall_location[1], wall_location[0], d)

