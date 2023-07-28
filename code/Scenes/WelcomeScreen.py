import pygame

from code.GUI.TextBox import TextBox
from code.Scenes.Scene import Scene


class WelcomeScreen(Scene):
    name = "Welcome Screen"

    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self._screen = screen
        self.font = font
        self.objects = []

        text_color = (100, 100, 255)
        self.textbox_player1_name = TextBox(50, 50, 400, font)
        self.textbox_player1_password = TextBox(50, 150, 400, font, text_color, border_color=text_color,
                                                text_type="password")
        self.textbox_player2_name = TextBox(50, 250, 400, font, (0, 0, 0), (255, 255, 255), (10, 120, 245))
        self.textbox_player2_password = TextBox(50, 350, 400, font, (255, 255, 255), (240, 165, 165), (10, 120, 245))
        self.group = pygame.sprite.Group(self.textbox_player1_name, self.textbox_player1_password,
                                         self.textbox_player2_name, self.textbox_player2_password)

    @property
    def shortcuts(self):
        return {}

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    def render(self):
        self.screen.fill(color="aliceblue")
        self.group.draw(self.screen)

    def update(self, events: list[pygame.event]):
        self.group.update(events)

    def recalculate_objects(self):
        pass
