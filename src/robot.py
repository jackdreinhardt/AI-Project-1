# Robot
#
# This is the main class for the game pieces. The game pieces can be moved in
# this class.

from random import randrange as rd

class Robot:
    def __init__(self, color, x, y):
        self.color_ = color
        self.x_ = x
        self.y_ = y

    # returns a new instance of robot with updated coordinates
    def move(self, board, robots, d):
        x = self.x_
        y = self.y_
        c = self.color_
        if d == "NORTH":
            while not board.square(y, x).wall_north_:
                for r in robots:
                    if r.y_ == y - 1 and r.x_ == x:
                        return Robot(c, x, y)
                y -= 1
        elif d == "SOUTH":
            while not board.square(y, x).wall_south_:
                for r in robots:
                    if r.y_ == y + 1 and r.x_ == x:
                        return Robot(c, x, y)
                y += 1
        elif d == "EAST":
            while not board.square(y, x).wall_east_:
                for r in robots:
                    if r.x_ == x + 1 and r.y_ == y:
                            return Robot(c, x, y)
                x += 1
        elif d == "WEST":
            while not board.square(y, x).wall_west_:
                for r in robots:
                    if r.x_ == x - 1 and r.y_ == y:
                        return Robot(c, x, y)
                x -= 1
        else:
            print("The key you entered is not a valid direction.")
        return Robot(c,x,y)


    def move_possible(self, board, robots, d):
        x = self.x_
        y = self.y_
        if d == "NORTH":
            if not board.square(y, x).wall_north_:
                for r in robots:
                    if r.y_ == y - 1 and r.x_ == x:
                        return False
            else: return False
        elif d == "SOUTH":
            if not board.square(y, x).wall_south_:
                for r in robots:
                    if r.y_ == y + 1 and r.x_ == x:
                        return False
            else: return False
        elif d == "EAST":
            if not board.square(y, x).wall_east_:
                for r in robots:
                    if r.x_ == x + 1 and r.y_ == y:
                        return False
            else: return False
        elif d == "WEST":
            if not board.square(y, x).wall_west_:
                for r in robots:
                    if r.x_ == x - 1 and r.y_ == y:
                        return False
            else: return False
        else:
            print("The key you entered is not a valid direction.")
        return True

    # static functions ( do not reference self )
    def validate_positions(board, robots):
        for i in range(len(robots)):
            while not Robot.valid_position(board, robots[i], robots[:i] + robots[(i+1):]):
                robots[i].x_ = rd(board.boardsize_)
                robots[i].y_ = rd(board.boardsize_)

    def valid_position(board, r, other_robots):
        return not (r.x_, r.y_) in [(o_r.x_, o_r.y_) for o_r in other_robots] \
                and not board.center(r.y_, r.x_)
