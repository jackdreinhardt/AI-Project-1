# Player class
#
# Base class for the human and AI players. Includes shared variables and
# required functions

class Player:
    def __init__(self, name, score):
        self.name_ = name
        self.score_ = score
        self.move_count_ = 0

        self.north_click_bound = None
        self.south_click_bound = None
        self.east_click_bound = None
        self.west_click_bound = None

        self.selected_ = False

    # pure virtual, implemented by child class
    def execute_moves(self, app, limit):
        raise TypeError('Abstract method `' + self._class.__name__ \
                            + '.' + self._function + '\' called')

    # pure virtual, implemented by child class
    def search(self, board, target, robots, limit, heuristic):
        raise TypeError('Abstract method `' + self._class.__name__ \
                            + '.' + self._function + '\' called')
