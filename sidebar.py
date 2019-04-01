import pygame
from player import Player

# Sidebar Class
#
# Provides an interface to choose the current player, and display the score,
# and display the current number of moves of the player

class Sidebar:
    def __init__(self, graphics, players):
        self.players_ = players
        self.g_ = graphics
        self.fontsize = 20

        font = pygame.font.SysFont("helvetica", 20)
        self.line_ = 13
        line = self.g_.BoardSize_ * self.line_
        for p in self.players_:
            text = font.render(p.name_, True, (0, 0, 0))
            p.north_click_bound = line - text.get_height()
            p.south_click_bound = line
            p.east_click_bound = self.g_.BoardArea + 0.1 * self.g_.ScoreBoard + text.get_width()
            p.west_click_bound = self.g_.BoardArea + 0.1 * self.g_.ScoreBoard
            line += line

    def DeterminePlayer(self, click):
        players = [None, None]
        for p in self.players_:
            if click[0] > p.west_click_bound and click[0] < p.east_click_bound and click[1] > p.north_click_bound and click[1] < p.south_click_bound:
                p.selected_ = True
                players[0] = p
            else:
                p.selected_ = False
                players[1] = p
        self.drawScoreboard(self.players_)
        return players

    def switchPlayer(self):
        for p in self.players_:
            p.selected_ = not p.selected_
        self.drawScoreboard(self.players_)

    def noPlayer(self):
        for p in self.players_:
            p.selected_ = False
        self.drawScoreboard(self.players_)

    def drawScoreboard(self, players):
        pygame.draw.rect(self.g_.Screen, self.g_.Tile2, (self.g_.BoardArea, 0, self.g_.BoardArea + self.g_.ScoreBoard, 0.66 * self.g_.BoardArea))
        font = pygame.font.SysFont("helvetica", self.fontsize)
        text = font.render("Scoreboard", True, (0, 0, 0))
        self.g_.Screen.blit(text,(self.g_.BoardArea + 0.3 * self.g_.ScoreBoard - 0.5 * text.get_width(), 5))

        line = self.g_.BoardSize_ * self.line_
        for p in players:
            text = font.render(p.name_, True, (0, 0, 0))
            self.g_.Screen.blit(text,(p.west_click_bound, p.north_click_bound))
            text = font.render(str(p.score_), True, (0, 0, 0))
            self.g_.Screen.blit(text,(self.g_.BoardArea + 0.9 * self.g_.ScoreBoard - text.get_width() // 2, p.north_click_bound))
            if p.selected_:
                text = font.render("# moves: " + str(p.move_count_), True, (0, 0, 0))
                self.g_.Screen.blit(text,(self.g_.BoardArea + 0.8 * self.g_.ScoreBoard - text.get_width() // 2, 5))
                s = pygame.Surface((p.east_click_bound - p.west_click_bound, p.south_click_bound - p.north_click_bound))
                s.set_alpha(30)
                s.fill((0,0,0))
                self.g_.Screen.blit(s, (p.west_click_bound,p.north_click_bound))
            line += line
        pygame.display.flip()

    def displayMessage(self, message):
        pygame.draw.rect(self.g_.Screen, self.g_.Tile2, (self.g_.BoardArea, 0.66 * self.g_.BoardArea, self.g_.BoardArea + self.g_.ScoreBoard, self.g_.BoardArea))
        font = pygame.font.SysFont("helvetica", self.fontsize)
        lines = 90
        for m in message:
            text = font.render(m, True, (0, 0, 0))
            self.g_.Screen.blit(text, (self.g_.BoardArea + 0.5 * self.g_.ScoreBoard - 0.5 * text.get_width(), self.g_.BoardArea - lines))
            lines -= 40
        pygame.display.flip()
        self.pygame_update()

    # This is terrible, but the only way the screen updates
    def pygame_update(self):
        for event in pygame.event.get():
            pass
