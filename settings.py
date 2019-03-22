

class Settings:
    def __init__(self, boardsize=16, robots=4, players=['Player 1','Player 2']):
        self.boardsize_ = boardsize
        self.robots_ = robots
        self.players_ = players

    def set_settings(self, args):
        for i in range(len(args)):
            if args[i] == '-b':
                self.boardsize_ = int(args[i+1])
            elif args[i] == '-r':
                if int(args[i+1]) > 4:
                    raise "Cannot have more than 4 robots"
                self.robots_ = int(args[i+1])
            elif args[i] == '-p1':
                self.players_[0] = args[i+1]
            elif args[i] == '-p2':
                self.players_[1] = args[i+1]