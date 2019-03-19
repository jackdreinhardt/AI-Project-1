import random

from square import Square
from globals import BOARDSIZE

class Board:
    def __init__(self, robots):
        self.board_ = [[Square() for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]
        self.robots_ = robots

    def PlaceTarget(self):
        for i in range(BOARDSIZE):
            for j in range (BOARDSIZE):
                self.board_[i][j].target_ = None
        rand = random.choice(range(16))

        # map.target_locations
        red = [(1,5),(5,9),(9,5),(11,13)]
        blue = [(2,1),(2,14),(12,6),(14,14)]
        green = [(1,12),(6,2),(13,9),(14,2)]
        yellow = [(4,6),(6,11),(9,1),(10,8)]

        # set location
        if rand < 4:
          rand = rand % 4
          self.board_[red[rand][0]][red[rand][1]].target_ = self.robots_[0]
        elif rand < 8:
          rand = rand % 4
          self.board_[blue[rand][0]][blue[rand][1]].target_ = self.robots_[1]
        elif rand < 12:
          rand = rand % 4
          self.board_[green[rand][0]][green[rand][1]].target_ = self.robots_[2]
        elif rand < 16:
          rand = rand % 4
          self.board_[yellow[rand][0]][yellow[rand][1]].target_ = self.robots_[3]

    def border(self, x, y):
        return x == BOARDSIZE - 1 or x == 0 or y == BOARDSIZE - 1 or y == 0

    def PlaceWall(self, x, y, direction):
        if direction == NORTH:
          self.board_[x][y].Wall(direction)
          if not border(x, y):
            self.board_[x+1][y].Wall(SOUTH)
        if direction == SOUTH:
          self.board_[x][y].Wall(direction)
          if not border(x, y):
            self.board_[x-1][y].Wall(NORTH)
        if direction == EAST:
          self.board_[x][y].Wall(direction)
          if not border(x, y):
            self.board_[x][y-1].Wall(WEST)
        if direction == WEST:
          self.board_[x][y].Wall(direction)
          if not border(x, y):
            self.board_[x][y+1].Wall(EAST)

    def PlaceRobots(self):
        for r in self.robots_:
            self.board_[r.y_][r.x_].robot_ = r

    def PlaceWalls(self):
        # outer walls
        for i in range(BOARDSIZE):
            self.board_[0][i].north_ = 1
            self.board_[15][i].south_ = 1
            self.board_[i][0].west_ = 1
            self.board_[i][15].east_ = 1

            # Add inner square walls
            self.board_[6][7].south_ = self.board_[6][8].south_ = 1
            self.board_[7][6].east_ = self.board_[8][6].east_ = 1
            self.board_[7][9].west_ = self.board_[8][9].west_ = 1
            self.board_[9][7].north_ = self.board_[9][8].north_ = 1

            # Add vertical walls
            self.board_[0][3].east_ = self.board_[0][4].west_ = 1
            self.board_[0][10].east_ = self.board_[0][11].west_ = 1
            self.board_[1][5].east_ = self.board_[1][6].west_ = 1
            self.board_[1][11].east_ = self.board_[1][12].west_ = 1
            self.board_[2][0].east_ = self.board_[2][1].west_ = 1
            self.board_[2][13].east_ = self.board_[2][14].west_ = 1
            self.board_[3][7].east_ = self.board_[3][8].west_ = 1
            self.board_[4][6].east_ = self.board_[4][7].west_ = 1
            self.board_[5][9].east_ = self.board_[5][10].west_ = 1
            self.board_[6][2].east_ = self.board_[6][3].west_ = 1
            self.board_[6][11].east_ = self.board_[6][12].west_ = 1
            self.board_[9][1].east_ = self.board_[9][2].west_ = 1
            self.board_[9][4].east_ = self.board_[9][5].west_ = 1
            self.board_[10][8].east_ = self.board_[10][9].west_ = 1
            self.board_[11][12].east_ = self.board_[11][13].west_ = 1
            self.board_[12][6].east_ = self.board_[12][7].west_ = 1
            self.board_[13][8].east_ = self.board_[13][9].west_ = 1
            self.board_[14][1].east_ = self.board_[14][2].west_ = 1
            self.board_[14][14].east_ = self.board_[14][15].west_ = 1
            self.board_[15][5].east_ = self.board_[15][6].west_ = 1
            self.board_[15][11].east_ = self.board_[15][12].west_ = 1

            

            # Add horizontal walls
            self.board_[0][5].south_ = self.board_[1][5].north_ = 1
            self.board_[0][12].south_ = self.board_[1][12].north_ = 1
            self.board_[2][1].south_ = self.board_[3][1].north_ = 1
            self.board_[2][14].south_ = self.board_[3][14].north_ = 1
            self.board_[3][0].south_ = self.board_[4][0].north_ = 1
            self.board_[3][8].south_ = self.board_[4][8].north_ = 1
            self.board_[4][6].south_ = self.board_[5][6].north_ = 1
            self.board_[4][15].south_ = self.board_[5][15].north_ = 1
            self.board_[5][9].south_ = self.board_[6][9].north_ = 1
            self.board_[5][11].south_ = self.board_[6][11].north_ = 1
            self.board_[6][2].south_ = self.board_[7][2].north_ = 1
            self.board_[8][1].south_ = self.board_[9][1].north_ = 1
            self.board_[8][5].south_ = self.board_[9][5].north_ = 1
            self.board_[9][15].south_ = self.board_[10][15].north_ = 1
            self.board_[10][0].south_ = self.board_[11][0].north_ = 1
            self.board_[10][8].south_ = self.board_[11][8].north_ = 1
            self.board_[10][13].south_ = self.board_[11][13].north_ = 1
            self.board_[12][6].south_ = self.board_[13][6].north_ = 1
            self.board_[13][9].south_ = self.board_[14][9].north_ = 1
            self.board_[13][14].south_ = self.board_[14][14].north_ = 1
            self.board_[14][2].south_ = self.board_[15][2].north_ = 1

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

