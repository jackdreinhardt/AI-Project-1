# Robot
#
# This is the main class for the game pieces. This is where the pieces can be
# moved.

class Robot:
    def __init__(self, color, x, y):
        self.color_ = color
        self.x_ = x
        self.y_ = y

    # updates the position variables of the robot, updates board[][].robot
    # @param d direction to move robot
    # @param l number of pixels to move ('vel' in RicochetRobots.py)
    # returns true if move was successful, false otherwise
    def move(self, board, d):
        moved = False
        if d == "NORTH":
            self.move_north(board)
            moved = True
        elif d == "SOUTH":
            self.move_south(board)
            moved = True
        elif d == "EAST":
            self.move_east(board)
            moved = True
        elif d == "WEST":
            self.move_west(board)
            moved = True
        else:
          print("The key you entered is not a valid direction.")
        return moved # test_robot.curX != self.curX or test_robot.curY != self.curY

    def move_possible(self, board, d):
        if d == "NORTH":
            if not board[self.y_][self.x_].north_ and board[self.y_-1][self.x_].robot_ == None:
                return True
        elif d == "SOUTH":
            if not board[self.y_][self.x_].south_ and board[self.y_+1][self.x_].robot_ == None:
                return True
        elif d == "EAST":
            if not board[self.y_][self.x_].east_ and board[self.y_][self.x_+1].robot_ == None:
                return True
        elif d == "WEST":
            if not board[self.y_][self.x_].west_ and board[self.y_][self.x_-1].robot_ == None:
                return True
        else:
            return False

    def move_north(self, board):
        while not board[self.y_][self.x_].north_ and board[self.y_-1][self.x_].robot_ == None:
            board[self.y_][self.x_].robot_ = None
            board[self.y_-1][self.x_].robot_ = self
            self.y_ -= 1

    def move_south(self, board):
        while not board[self.y_][self.x_].south_ and board[self.y_+1][self.x_].robot_ == None:
            board[self.y_][self.x_].robot_ = None
            board[self.y_+1][self.x_].robot_ = self
            self.y_ += 1

    def move_east(self, board):
        while not board[self.y_][self.x_].east_ and board[self.y_][self.x_+1].robot_ == None:
            board[self.y_][self.x_].robot_ = None
            board[self.y_][self.x_+1].robot_ = self
            self.x_ += 1

    def move_west(self, board):
        while not board[self.y_][self.x_].west_ and board[self.y_][self.x_-1].robot_ == None:
          board[self.y_][self.x_].robot_ = None
          board[self.y_][self.x_-1].robot_ = self
          self.x_ -= 1
    
    def moveRobot (self,board,direction,newRobots):
        newRobots = self
        moved = False
        if direction == "NORTH":
            newRobots.move_north(board)
            moved = True
        elif direction == "SOUTH":
            newRobots.move_south(board)
            moved = True
        elif direction == "EAST":
            newRobots.move_east(board)
            moved = True
        elif direction == "WEST":
            newRobots.move_west(board)
            moved = True
        else:
          print("The key you entered is not a valid direction.")
        return moved # test_robot.curX != self.curX or test_robot.curY != self.curY
