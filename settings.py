

class Settings:
    def __init__(self, boardsize=16, robots=4, players=['bfs','Player 2']):
        self.boardsize_ = boardsize
        self.robots_ = robots
        self.players_ = players
        self.test_rounds_ = 0

    def set_settings(self, args):
        for i in range(len(args)):
            if args[i] == '-b':
                self.boardsize_ = int(args[i+1])
            elif args[i] == '-r':
                if int(args[i+1]) > 4:
                    raise "Cannot have more than 4 robots"
                self.robots_ = int(args[i+1])
            elif args[i] == '-t':
                if int(args[i+1]) < 1:
                    raise "Cannot test less 1 round"
                self.test_rounds_ = int(args[i+1])
            elif args[i] == '-p1':
                self.players_[0] = args[i+1]
            elif args[i] == '-p2':
                self.players_[1] = args[i+1]
