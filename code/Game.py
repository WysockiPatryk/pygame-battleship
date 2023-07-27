import sys

import pygame

import code.constants as constants
import code.utilities as utilities
from code.Player import Player
from code.Yacht import Yacht


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Battleship')

        screen_width, screen_height = utilities.get_window_size()
        self.screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), *constants.DISPLAY_FLAGS)
        self.clock = pygame.time.Clock()

        self.images = utilities.load_images()
        self.players = []
        self.player1 = Player('Player 1')
        self.players.append(self.player1)
        y1 = Yacht(self.images['yacht'], (100, 100))
        self.player1.ships.append(y1)

    def update_objects(self):
        for player in self.players:
            for ship in player.ships:
                self.screen.blit(ship.image, ship.position)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = utilities.limit_window_size(event)
            self.update_objects()
            pygame.display.update()
            self.clock.tick(60)
