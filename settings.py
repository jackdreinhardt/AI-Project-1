from human_player import HumanPlayer
from informed_bf_player import Graph_Search_BF
from informed_df_player import Graph_Search_DF
from a_star_player import A_Star_Player
from depth_limited_player import Depth_Limited_Player
from AAI import Advanced_AI_Player
from limited_bfs import LimitedBFS

class Settings:
    def __init__(self, boardsize=16, robots=4, players=['Player 1','Player 2']):
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
                    print("Cannot have more than 4 robots.\n")
                    exit(-1)
                self.robots_ = int(args[i+1])
            elif args[i] == '-t':
                self.test_rounds_ = int(args[i+1])
            elif args[i] == '-p1':
                self.players_[0] = args[i+1]
            elif args[i] == '-p2':
                self.players_[1] = args[i+1]

    def assign_players(self):
        players = []
        for name in self.players_:
            if name == 'dfs':
                players.append(Depth_Limited_Player())
            elif name == 'a-star':
                players.append(A_Star_Player())
            elif name == 'aai':
                players.append(Advanced_AI_Player())
            elif name == 'bfs':
                players.append(Graph_Search_BF())
            elif name == 'i_dfs':
                players.append(Graph_Search_DF())
            elif name == 't_bfs':
                players.append(LimitedBFS())
            else:
                players.append(HumanPlayer(name))
        return players
        
