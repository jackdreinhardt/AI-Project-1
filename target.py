import random as rd
from globals import *
from board import Board

class Target:
    def __init__(self, boardSize, board, robots):
        self.board_size_ = boardSize
        self.set_target(board, robots)

    def set_target(self, board, robots):
        self.color_ = robots[rd.randrange(len(robots))].color_
        locations = self.valid_locations(board, robots)
        loc = locations[rd.randrange(len(locations))]
        self.x_ = loc[1]
        self.y_ = loc[0]

    def valid_target_loc(self, board, robots, i, j):
        return ((board.square(i, j).wall_north_ and board.square(i, j).wall_east_) \
            or (board.square(i, j).wall_north_ and board.square(i, j).wall_west_) \
            or (board.square(i, j).wall_south_ and board.square(i, j).wall_east_) \
            or (board.square(i, j).wall_south_ and board.square(i, j).wall_west_)) \
            and not board.center(i, j) \
            and not (i,j) in [(r.y_,r.x_) for r in robots]
            # and not (i == 0 or i ==  self.board_size_ - 1) \
            # and not (j == 0 or j == self.board_size_ - 1) \
            

    def valid_locations(self, board, robots):
        locations = []
        for i in range(self.board_size_):
            for j in range(self.board_size_):
                if self.valid_target_loc(board, robots, i, j):
                    locations.append((i,j))
        return locations






