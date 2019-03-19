# Robot
#
# This is the main class for the game pieces. This is where the pieces can be
# moved.

import math

class Robot:
    def __init__(self, color, x, y):
        self.color_ = color
        self.x_ = x
        self.y_ = y

    # updates the position variables of the robot, updates board[][].robot
    # @param d direction to move robot
    # @param l number of pixels to move ('vel' in RicochetRobots.py)
    # returns true if move was successful, false otherwise
    def move(self, board, robots, d):
        x = self.x_
        y = self.y_
        if d == "NORTH":
            while not board.square(y, x).wall_north_:
                for r in robots:
                    if r.y_ == y - 1 and r.x_ == x:
                        return Robot(self.color_, x, y)
                y -= 1
        elif d == "SOUTH":
            while not board.square(y, x).wall_south_:
                for r in robots:
                    if r.y_ == y + 1 and r.x_ == x:
                        return Robot(self.color_, x, y)
                y += 1
        elif d == "EAST":
            while not board.square(y, x).wall_east_:
                for r in robots:
                    if r.x_ == x + 1 and r.y_ == y:
                            return Robot(self.color_, x, y)
                x += 1
        elif d == "WEST":
            while not board.square(y, x).wall_west_:
                for r in robots:
                    if r.x_ == x - 1 and r.y_ == y:
                        return Robot(self.color_, x, y)
                x -= 1
        else:
          print("The key you entered is not a valid direction.")
        return Robot(self.color_, x, y)

    def move_possible(self, board, robots, d):
        x = self.x_
        y = self.y_
        if d == "NORTH":
            if not board.square(y, x).wall_north_:
                for r in robots:
                    if r.y_ == y - 1 and r.x_ == x:
                        return False
        elif d == "SOUTH":
            if not board.square(y, x).wall_south_:
                for r in robots:
                    if r.y_ == y + 1 and r.x_ == x:
                        return False
        elif d == "EAST":
            if not board.square(y, x).wall_east_:
                for r in robots:
                    if r.x_ == x + 1 and r.y_ == y:
                        return False
        elif d == "WEST":
            if not board.square(y, x).wall_west_:
                for r in robots:
                    if r.x_ == x - 1 and r.y_ == y:
                        return False
        else:
          print("The key you entered is not a valid direction.")
        return True
    
    