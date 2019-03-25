import pygame, time
from sys import argv
import random as rd
import copy

from globals import *

from board import Board
from robot import Robot
from target import Target
from drawks import GraphicalBoard
from settings import Settings


from human_player import HumanPlayer
from informed_bf_player import Graph_Search_BF
from informed_df_player import Graph_Search_DF
from a_star_player import A_Star_Player


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
            elif p == 'bfs':
                self.players_.append(Graph_Search_BF())
            elif p == 'i_dfs':
                self.players_.append(Graph_Search_DF())    
            else:
                self.players_.append(HumanPlayer(p))

        self.graphics_ = GraphicalBoard(s.boardsize_)
        
    
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


    def RunAI(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        pygame.time.delay(100)
        ai_player = Depth_Limited_Player()
        print("Searching for solution")
        start_time = time.time()
        solution = ai_player.search(self.board_, self.target_, self.robots_, 7)
        if (solution != "FAILURE" and solution != "CUTOFF"):
            print("Found solution of length " + str(len(solution)))
            solution_time = time.time() - start_time
            print("The algorithm took " + str(solution_time) + " seconds to find a solution")
            for m in range(len(solution)):
                #print(solution)
                self.robots_[solution[m][0]] = self.robots_[solution[m][0]].move(self.board_, self.robots_, solution[m][1]) # move robot
                self.graphics_.drawRobots(self.board_, self.robots_, self.target_)
                time.sleep(1)
        else:
            print("No solution found")

    def RunAStar(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        pygame.time.delay(100)
        ai_player = A_Star_Player()
        print("Searching for solution")
        start_time = time.time()
        solution = ai_player.search(self.board_, self.target_, self.robots_)
        if (solution != "FAILURE"):
            print("Found solution of length " + str(len(solution)))
            solution_time = time.time() - start_time
            print("The algorithm took " + str(solution_time) + " seconds to find a solution")
            for m in range(len(solution)):
                #print(solution)
                self.robots_[solution[m][0]] = self.robots_[solution[m][0]].move(self.board_, self.robots_, solution[m][1]) # move robot
                self.graphics_.drawRobots(self.board_, self.robots_, self.target_)
                time.sleep(1)
        else:
            print("No solution found")

    def RunBF(self):
        self.graphics_.drawBoardState(self.board_, self.robots_,self.target_)
        player = Graph_Search_BF()
        print("running")
        solution = player.search(self.board_, self.robots_, self.target_,5)


        for i in solution:
            print(i)

        input()
        pygame.display.quit()
        pygame.quit()


    def Run1(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        moveCount = 0
        robot = None

        while True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    robot = self.graphics_.DetermineRobo(event.pos, self.robots_)
                if event.type == pygame.KEYDOWN and robot != None:
                    d = self.KeyToDir(event.key)
                    if robot.move_possible(self.board_, self.robots_, d):
                        robot = robot.move(self.board_, self.robots_, d)
                        moveCount += 1
                        print("Moves: " + str(moveCount))
                        for i in range(len(self.robots_)):
                            if robot.color_ == self.robots_[i].color_:
                                self.robots_[i] = robot
                    self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

                    for r in self.robots_:
                        if r.y_ == self.target_.y_ and r.x_ == self.target_.x_ and r.color_ == self.target_.color_:
                            print("Success! New target placed")
                            print("You took " + str(moveCount) + " moves to find a solution")
                            moveCount = 0
                            self.target_.set_target(self.board_, self.robots_)
                            self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

    def Run(self):
        self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

        while True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
            while True:
                print("Type 1 or 2 to select player.\n\nplayer1: {p1} or player2: {p2}"\
                        .format(p1=self.players_[0].name_, p2=self.players_[1].name_))
                p = input()
                if not (p != '1' and p != '2'):
                    p = int(p)
                    break
                print("Invalid Player, try again")
            current_player = self.players_[p-1]
            other_player = self.players_[2-p]
            robot_start_position = copy.deepcopy(self.robots_)

            cp_move_count = current_player.execute_moves(self, LIMIT)
            if cp_move_count == 0:
                print('{cp} was not able to reach the target. If {op} can find a solution, they win the round.'\
                    .format(cp=current_player.name_, op=other_player.name_))
                cp_move_count = 999
            else:
                print('{cp} was able to reach the target in {count} moves. {op} gets 1 minute to find a better solution.'\
                    .format(cp=current_player.name_, count=cp_move_count, op=other_player.name_))
            pygame.time.delay(1000)

            first_player_robots = self.robots_
            self.robots_ = robot_start_position
            self.graphics_.drawBoardState(self.board_, self.robots_, self.target_)

            op_move_count = other_player.execute_moves(self, LIMIT)
            if op_move_count == 0:
                print('{op} was not able to reach the target.'\
                    .format(count=op_move_count, op=other_player.name_))
                op_move_count == 999
            else:
                print('{op} was able to reach the target in {count} moves.'\
                    .format(count=op_move_count, op=other_player.name_))
            pygame.time.delay(1000)

            if op_move_count < cp_move_count:
                other_player.score_ += 1
            elif cp_move_count == 999 and op_move_count == 999:
                self.robots = robot_start_position
                print("Neither player was able to find a solution, no points awarded")
            else:
                current_player.score_ += 1
                self.robots_ = first_player_robots

            print("Round complete.")
            print("Scores: {p1} - {p1p}, {p2} - {p2p}"\
                .format(p1=self.players_[0].name_, p1p=self.players_[0].score_,
                        p2=self.players_[1].name_, p2p=self.players_[1].score_))

            for p in self.players_:
                if p.score_ == 2:
                    print("{p} wins!".format(p=p.name_))
                    exit()

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
            cp_move_count = current_player.execute_moves(self, LIMIT)
            print('{cp} was able to reach the target in {count} moves.'.format(cp=current_player.name_, count=cp_move_count))
            print('{cp} expanded {nodes} to find the solution.'.format(cp=current_player.name_, nodes=current_player.nodes_expanded_))
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
    
