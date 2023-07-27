import pygame

from code.Scenes.Scene import Scene


class WelcomeScreen(Scene):
    name = "Welcome Screen"

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
        self.screen.fill(color="aliceblue")

    def update(self):
        print("Welcome Screen - update()")

    def recalculate_objects(self):
        pass
