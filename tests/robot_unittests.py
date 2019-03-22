# how to run in command line
#   python -m unittest robot_unittests.py

import unittest

from ..robot import Robot

class TestRobotMethods(unittest.TestCase):

    def setUp(self):
        self.r = Robot(RED,0,0)
        self.b = Robot(BLUE,4,5)
        self.robots = [r, b]

    def test_move(self):
        r.move(Board(6), robots, "NORTH")
        

    def test_move_possible(self):
        pass

    def test_possible_moves(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()