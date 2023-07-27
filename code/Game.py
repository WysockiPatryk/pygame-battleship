import sys

import pygame

import code.constants as constants
import code.utilities as utilities
from code.Player import Player
from code.SceneManager import SceneManager
from code.Scenes.BattleStage import BattleStage
from code.Scenes.EndgameScreen import EndgameScreen
from code.Scenes.PreparationStage import PreparationStage
from code.Scenes.Scene import Scene
from code.Scenes.WelcomeScreen import WelcomeScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Battleship')

        screen_width, screen_height = utilities.get_window_size()
        self.screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), *constants.DISPLAY_FLAGS)
        self.clock = pygame.time.Clock()

        # self.images = utilities.load_images()
        self.players = []
        self.player1 = Player('Player 1')
        self.players.append(self.player1)
        # y1 = Yacht(self.images['yacht'], (100, 100))
        # self.player1.ships.append(y1)
        self.scene_manager = SceneManager(self.screen)
        self.active_scene = self.scene_manager.switch_scene_to(WelcomeScreen())

    def update_objects(self, active_scene: Scene):
        active_scene.render(self.screen)
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.active_scene = self.scene_manager.switch_scene_to(PreparationStage())
                    elif event.key == pygame.K_2:
                        self.active_scene = self.scene_manager.switch_scene_to(BattleStage())
                    elif event.key == pygame.K_3:
                        self.active_scene = self.scene_manager.switch_scene_to(EndgameScreen())
            self.update_objects(self.active_scene)
            pygame.display.update()
            self.clock.tick(60)
