import random

from square import Square

class Board:
    def __init__(self, boardSize):
        self.board_ = [[Square() for j in range(boardSize)] for i in range(boardSize)]
        self.PlaceWalls(boardSize)

    def PlaceWalls(self, boardSize):
        # outer walls
        for i in range(boardSize):
            self.board_[0][i].north_ = 1
            self.board_[15][i].south_ = 1
            self.board_[i][0].west_ = 1
            self.board_[i][15].east_ = 1

            # Add inner square walls
            self.board_[6][7].south_ = self.board_[6][8].south_ = 1
            self.board_[7][6].east_ = self.board_[8][6].east_ = 1
            self.board_[7][9].west_ = self.board_[8][9].west_ = 1
            self.board_[9][7].north_ = self.board_[9][8].north_ = 1

            # Add vertical walls
            self.board_[0][3].east_ = self.board_[0][4].west_ = 1
            self.board_[0][10].east_ = self.board_[0][11].west_ = 1
            self.board_[1][5].east_ = self.board_[1][6].west_ = 1
            self.board_[1][11].east_ = self.board_[1][12].west_ = 1
            self.board_[2][0].east_ = self.board_[2][1].west_ = 1
            self.board_[2][13].east_ = self.board_[2][14].west_ = 1
            self.board_[3][7].east_ = self.board_[3][8].west_ = 1
            self.board_[4][6].east_ = self.board_[4][7].west_ = 1
            self.board_[5][9].east_ = self.board_[5][10].west_ = 1
            self.board_[6][2].east_ = self.board_[6][3].west_ = 1
            self.board_[6][11].east_ = self.board_[6][12].west_ = 1
            self.board_[9][1].east_ = self.board_[9][2].west_ = 1
            self.board_[9][4].east_ = self.board_[9][5].west_ = 1
            self.board_[10][8].east_ = self.board_[10][9].west_ = 1
            self.board_[11][12].east_ = self.board_[11][13].west_ = 1
            self.board_[12][6].east_ = self.board_[12][7].west_ = 1
            self.board_[13][8].east_ = self.board_[13][9].west_ = 1
            self.board_[14][1].east_ = self.board_[14][2].west_ = 1
            self.board_[14][14].east_ = self.board_[14][15].west_ = 1
            self.board_[15][5].east_ = self.board_[15][6].west_ = 1
            self.board_[15][11].east_ = self.board_[15][12].west_ = 1
            

            # Add horizontal walls
            self.board_[0][5].south_ = self.board_[1][5].north_ = 1
            self.board_[0][12].south_ = self.board_[1][12].north_ = 1
            self.board_[2][1].south_ = self.board_[3][1].north_ = 1
            self.board_[2][14].south_ = self.board_[3][14].north_ = 1
            self.board_[3][0].south_ = self.board_[4][0].north_ = 1
            self.board_[3][8].south_ = self.board_[4][8].north_ = 1
            self.board_[4][6].south_ = self.board_[5][6].north_ = 1
            self.board_[4][15].south_ = self.board_[5][15].north_ = 1
            self.board_[5][9].south_ = self.board_[6][9].north_ = 1
            self.board_[5][11].south_ = self.board_[6][11].north_ = 1
            self.board_[6][2].south_ = self.board_[7][2].north_ = 1
            self.board_[8][1].south_ = self.board_[9][1].north_ = 1
            self.board_[8][5].south_ = self.board_[9][5].north_ = 1
            self.board_[9][15].south_ = self.board_[10][15].north_ = 1
            self.board_[10][0].south_ = self.board_[11][0].north_ = 1
            self.board_[10][8].south_ = self.board_[11][8].north_ = 1
            self.board_[10][13].south_ = self.board_[11][13].north_ = 1
            self.board_[12][6].south_ = self.board_[13][6].north_ = 1
            self.board_[13][9].south_ = self.board_[14][9].north_ = 1
            self.board_[13][14].south_ = self.board_[14][14].north_ = 1
            self.board_[14][2].south_ = self.board_[15][2].north_ = 1

