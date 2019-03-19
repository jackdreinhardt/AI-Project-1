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
        self.x_ = x
        self.y_ = y
        if d == "NORTH":
            while not board[y][x].north_:
                for r in robots:
                    if r.y_ == y - 1:
                        return Robot(self.color, x, y)
                y -= 1
        elif d == "SOUTH":
            while not board[y][x].south_:
                for r in robots:
                    if r.y_ == y + 1:
                        return Robot(self.color, x, y)
                y += 1
        elif d == "EAST":
            while not board[y][x].east_:
                if r.x_ == x + 1:
                        return Robot(self.color, x, y)
                x += 1
        elif d == "WEST":
            while not board[y][x].west_:
                if r.x_ == x - 1:
                    return Robot(self.color, x, y)
                x -= 1
        else:
          print("The key you entered is not a valid direction.")
        return Robot(self.color, x, y)

    def move_possible(self, board, d):
        self.x_ = x
        self.y_ = y
        if d == "NORTH":
            if not board[y][x].north_:
                for r in robots:
                    if r.y_ == y - 1:
                        return False
        elif d == "SOUTH":
            if not board[y][x].south_:
                for r in robots:
                    if r.y_ == y + 1:
                        return False
        elif d == "EAST":
            if not board[y][x].east_:
                if r.x_ == x + 1:
                        return False
        elif d == "WEST":
            if not board[y][x].west_:
                if r.x_ == x - 1:
                    return False
        else:
          print("The key you entered is not a valid direction.")
        return True
    
    