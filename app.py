import pygame, time
from sys import argv
import random as rd
import copy

from globals import *

from board import Board
from robot import Robot
from target import Target
from drawks import GraphicalBoard
from sidebar import Sidebar
from settings import Settings


from human_player import HumanPlayer
from informed_bf_player import Graph_Search_BF
from informed_df_player import Graph_Search_DF
from a_star_player import A_Star_Player
from depth_limited_player import Depth_Limited_Player
from AAI import Advanced_AI_Player


class App:

    def __init__(self, s):
        self.board_ = Board(s.boardsize_)

        self.robots_ = []
        for i in range(s.robots_):
            self.robots_.append(Robot(COLORS[i], rd.randrange(s.boardsize_), rd.randrange(s.boardsize_)))
        Robot.validate_positions(self.board_, self.robots_)

        self.target_ = Target(s.boardsize_, self.board_, self.robots_)

        if (s.test_rounds_ > 0):
            self.test_rounds_ = s.test_rounds_
        else: self.test_rounds_ = 0

        self.players_ = []
        for p in s.players_:
            if p == 'dfs':
                self.players_.append(Depth_Limited_Player())
            elif p == 'a-star':
                self.players_.append(A_Star_Player())
            elif p == 'aai':
                self.players_.append(Advanced_AI_Player())
            elif p == 'bfs':
                self.players_.append(Graph_Search_BF())
            elif p == 'i_dfs':
                self.players_.append(Graph_Search_DF())
            else:
                self.players_.append(HumanPlayer(p))

        self.graphics_ = GraphicalBoard(s.boardsize_)
        self.sidebar_ = Sidebar(self.graphics_, self.players_)
        self.games_to_win_ = 2


#    def __init__(self,s,m):
#        self.board_ = Board(s.boardsize_)
#
#        self.robots_ = []
#        self.robots_.append(Robot(COLORS[0],0, 1))
#        self.robots_.append(Robot(COLORS[1],1, 0))
#        #self.robots_.append(Robot(COLORS[2],1, 0))
#        #Robot.validate_positions(self.board_, self.robots_)
#
#        self.target_ = Target(s.boardsize_, self.board_, self.robots_)
#        self.target_.color_ = COLORS[m]
#        self.target_.x_=4
#        self.target_.y_=5
#
#
#        if (s.test_rounds_ > 0):
#            self.test_rounds_ = s.test_rounds_
#        else: self.test_rounds_ = 0
#
#        self.players_ = []
#        for p in s.players_:
#            if p == 'dfs':
#                self.players_.append(Depth_Limited_Player())
#            elif p == 'a-star':
#                self.players_.append(A_Star_Player())
#            elif p == 'bfs':
#                self.players_.append(Graph_Search_BF())
#            else:
#                self.players_.append(HumanPlayer(p))
#
#        self.graphics_ = GraphicalBoard(s.boardsize_)

    def KeyToDir(self, key):
        if key == pygame.K_UP:
            return "NORTH"
        elif key == pygame.K_DOWN:
            return "SOUTH"
        elif key == pygame.K_RIGHT:
            return "EAST"
        elif key == pygame.K_LEFT:
            return "WEST"
        else:
            return "NOT SUPPORTED"


    def Run(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)
        self.sidebar_.drawScoreboard(self.players_)
        self.sidebar_.displayMessage(["Click a player name to select."])
        game_over = False

        while True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    # get mouse input to determine player
                    current_player, other_player = self.sidebar_.DeterminePlayer(event.pos)
                    if current_player == None:
                        break

                    # copy robot position for second player to try to find a better solution
                    robot_start_position = copy.deepcopy(self.robots_)

                    self.sidebar_.displayMessage(["Click a robot and move", " with arrow keys."])

                    # execute the moves of the current player
                    cp_move_count = current_player.execute_moves(self, 8)
                    if cp_move_count == 0:
                        print('{cp} was not able to reach the target. If {op} can find a solution, they win the round.'\
                            .format(cp=current_player.name_, op=other_player.name_))
                        cp_move_count = 999
                    else:
                        print('{cp} was able to reach the target in {count} moves. {op} gets 1 minute to find a better solution.'\
                            .format(cp=current_player.name_, count=cp_move_count, op=other_player.name_))
                    pygame.time.delay(1000)

                    # reset board to the original, before any moves in the round
                    self.sidebar_.switchPlayer()
                    first_player_robots = self.robots_
                    self.robots_ = robot_start_position
                    self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

                    # execute moves of the other player
                    op_move_count = other_player.execute_moves(self, 8)
                    if op_move_count == 0:
                        print('{op} was not able to reach the target.'\
                            .format(count=op_move_count, op=other_player.name_))
                        op_move_count = 999
                    else:
                        print('{op} was able to reach the target in {count} moves.'\
                            .format(count=op_move_count, op=other_player.name_))
                    pygame.time.delay(1000)

                    # deselect all players, and calculate the score of the round
                    self.sidebar_.noPlayer()
                    if op_move_count < cp_move_count:
                        other_player.score_ += 1
                    elif cp_move_count == 999 and op_move_count == 999:
                        self.robots = robot_start_position
                        self.sidebar_.displayMessage(["Neither player found a", "solution, no points awarded"])
                        pygame.time.delay(3000)
                    else:
                        current_player.score_ += 1
                        self.robots_ = first_player_robots

                    # final messages of the round
                    self.sidebar_.displayMessage(["Round complete.", "Click a player name to select."])
                    self.sidebar_.drawScoreboard(self.players_)

                    # check if a player won
                    for p in self.players_:
                        if p.score_ == self.games_to_win_:
                            self.sidebar_.displayMessage(["{p} wins!".format(p=p.name_)])
                            game_over = True

                    # reset the target location
                    self.target_.set_target(self.board_, self.robots_)
                    self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)



    def Run_Test(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        for i in range(self.test_rounds_):
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()

            current_player = self.players_[0]

            print("\n\nRunning test " + str(i+1))
            cp_move_count = current_player.execute_moves(self, 15)
            if (cp_move_count == FAILURE or cp_move_count == TIME_CUTOFF or cp_move_count == DEPTH_CUTOFF):
                print(cp_move_count)
                print('{cp} expanded {nodes} nodes.'.format(cp=current_player.name_, nodes=current_player.nodes_expanded_))
            else:
                print('{cp} was able to reach the target in {count} moves.'.format(cp=current_player.name_, count=cp_move_count))
                print('{cp} expanded {nodes} nodes to find the solution.'.format(cp=current_player.name_, nodes=current_player.nodes_expanded_))
            pygame.time.delay(1000)

            self.target_.set_target(self.board_, self.robots_)
            self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)
        print("Finished test")

if __name__ == '__main__':

    print("\nusage: python app.py -b <boardsize> -r <robotcount> -t <testroundss> -p1 <playerone> -p2 <playertwo>\n")
    s = Settings()
    s.set_settings(argv)
    game = App(s)
    if (game.test_rounds_ > 0):
        game.Run_Test()
    else: game.Run()

