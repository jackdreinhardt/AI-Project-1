# Robot.
#
# This is the main class for the game pieces. This is where the pieces can be
# moved. 

class Robot: 
  def __init__(self, Colour, current_x, current_y, current_square_x, current_square_y): 
    self.colour = Colour 
    self.curX = current_x
    self.curY = current_y 
    self.curSx = current_square_x
    self.curSy = current_square_y

  # updates the position variables of the robot, updates board[][].robot
  # @param d direction to move robot
  # @param l number of pixels to move ('vel' in RicochetRobots.py)
  # returns true if move was successful, false otherwise
  def move(self, board, d, l):
    # test_robot = self
    moved = False
    if d == "NORTH":
      while board[self.curSy][self.curSx].north == 0 and board[self.curSy-1][self.curSx].occ == 0:
        self.curSy -= 1
        self.curY -= l
        moved = True
        # update board[][].robot
    elif d == "SOUTH":
      while board[self.curSy][self.curSx].south == 0 and board[self.curSy+1][self.curSx].occ == 0:
        self.curSy += 1
        self.curY += l
        moved = True
        # update board[][].robot
    elif d == "EAST":
      while board[self.curSy][self.curSx].east == 0 and board[self.curSy][self.curSx+1].occ == 0:
        self.curSx += 1
        self.curX += l
        moved = True
        # update board[][].robot
    elif d == "WEST":
      while board[self.curSy][self.curSx].west == 0 and board[self.curSy][self.curSx-1].occ == 0:
        self.curSx -= 1
        self.curX -= l
        moved = True
        # update board[][].robot
    else:
      print("The key you entered is not a valid direction.")
    return moved # test_robot.curX != self.curX or test_robot.curY != self.curY
