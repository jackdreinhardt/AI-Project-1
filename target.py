import random as rd
from globals import *

class Target:
    def __init__(self, boardSize, board, num_robots):
        self.board_size_ = boardSize
        self.set_target(board, num_robots)

    def set_target(self, board, num_robots):
        colors = [RED, BLUE, GREEN, YELLOW]
        self.color_ = colors[rd.randrange(num_robots)]
        locations = self.valid_locations(board)
        print(locations)
        loc = locations[rd.randrange(len(locations))]
        self.x_ = loc[1]
        self.y_ = loc[0]

    def valid_target_loc(self, board, i, j):
        board = board.board_
        return (board[i][j].wall_north_ and board[i][j].wall_east_) \
            or (board[i][j].wall_north_ and board[i][j].wall_west_) \
            or (board[i][j].wall_south_ and board[i][j].wall_east_) \
            or (board[i][j].wall_south_ and board[i][j].wall_west_) \
            and not (i == 0 and j == 0) \
            and not (i == self.board_size_ - 1 and j == 0) \
            and not (i == 0 and j == self.board_size_ - 1) \
            and not (i == self.board_size_ - 1 and j == self.board_size_ - 1)

    def valid_locations(self, board):
        locations = []
        for i in range(self.board_size_):
            for j in range(self.board_size_):
                if self.valid_target_loc(board, i, j):
                    locations.append((i,j))
        return locations




# def PlaceTarget(self):
#         for i in range(BOARDSIZE):
#             for j in range (BOARDSIZE):
#                 self.board_[i][j].target_ = None
#         rand = random.choice(range(16))

#         # map.target_locations
#         red = [(1,5),(5,9),(9,5),(11,13)]
#         blue = [(2,1),(2,14),(12,6),(14,14)]
#         green = [(1,12),(6,2),(13,9),(14,2)]
#         yellow = [(4,6),(6,11),(9,1),(10,8)]

#         # set location
#         if rand < 4:
#           rand = rand % 4
#           self.board_[red[rand][0]][red[rand][1]].target_ = self.robots_[0]
#         elif rand < 8:
#           rand = rand % 4
#           self.board_[blue[rand][0]][blue[rand][1]].target_ = self.robots_[1]
#         elif rand < 12:
#           rand = rand % 4
#           self.board_[green[rand][0]][green[rand][1]].target_ = self.robots_[2]
#         elif rand < 16:
#           rand = rand % 4
#           self.board_[yellow[rand][0]][yellow[rand][1]].target_ = self.robots_[3]






