import pygame

from player import Player

class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name, 0)

    def execute_moves(self, app, limit=99):
        robot = None
        moveCount = 0
        while True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    robot = app.graphics_.DetermineRobo(event.pos, app.robots_)
                if event.type == pygame.KEYDOWN and robot != None:
                    d = app.KeyToDir(event.key)
                    if robot.move_possible(app.board_, app.robots_, d):
                        robot = robot.move(app.board_, app.robots_, d)
                        moveCount += 1
                        print("Moves: " + str(moveCount))
                        for i in range(len(app.robots_)):
                            if robot.color_ == app.robots_[i].color_:
                                app.robots_[i] = robot
                    app.graphics_.drawBoardState(app.board_, app.robots_, app.target_)

                    for r in app.robots_:
                        if r.y_ == app.target_.y_ and r.x_ == app.target_.x_ and r.color_ == app.target_.color_:
                            print("Success!")
                            return moveCount

    # since the user is playing the game, no search algorithm is needed
    def search(self, board, target, robots, limit):
        return None
