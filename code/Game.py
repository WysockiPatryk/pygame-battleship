import sys

import pygame

from code.utilities import get_window_size


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Battleship')
        
        screen_width, screen_height = get_window_size()
        self.screen = pygame.display.set_mode((screen_width - 100, screen_height - 100),
                                              pygame.RESIZABLE, pygame.SCALED)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)
