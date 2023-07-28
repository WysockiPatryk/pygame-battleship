import pygame

import code.constants as constants
import code.utilities as utilities
from code.Player import Player
from code.SceneManager import SceneManager
from code.Scenes.WelcomeScreen import WelcomeScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Battleship')

        screen_width, screen_height = utilities.get_window_size()
        self.screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), *constants.DISPLAY_FLAGS)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(constants.PATH_TO_FONT, size=48)

        # self.images = utilities.load_images()
        self.players = []
        self.player1 = Player('Player 1')
        self.players.append(self.player1)
        # y1 = Yacht(self.images['yacht'], (100, 100))
        # self.player1.ships.append(y1)
        self.scene_manager = SceneManager()
        self.scene_manager.set_scene(WelcomeScreen(self.screen, self.font))

    def update(self, events: list[pygame.event]):
        # ToDo: DO NOT REMOVE THIS COMMENT - can be used for debugging
        # for event in events:
        #     print(f"event: {event}")
        self.scene_manager.active_scene.update(events)
        for player in self.players:
            for ship in player.ships:
                self.screen.blit(ship.image, ship.position)

    def render(self):
        self.scene_manager.active_scene.render()
        # Other things to render (?)

    def run(self):
        while True:
            events = pygame.event.get()
            # for event in events:
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_1:
            #             self.scene_manager.set_scene(PreparationStage(self.screen))
            #         elif event.key == pygame.K_2:
            #             self.scene_manager.set_scene(BattleStage(self.screen))
            #         elif event.key == pygame.K_3:
            #             self.scene_manager.set_scene(EndgameScreen(self.screen))
            self.scene_manager.active_scene.handle_inputs(events)
            self.update(events)
            self.render()
            pygame.display.update()
            self.clock.tick(60)
