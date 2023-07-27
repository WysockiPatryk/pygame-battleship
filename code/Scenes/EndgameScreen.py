import pygame

from code.Scenes.Scene import Scene


class EndgameScreen(Scene):
    name = "Endgame Screen"

    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        self.objects = []

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
        self.screen.fill(color="crimson")

    def update(self):
        print("Endgame Screen - update()")

    def recalculate_objects(self):
        pass
