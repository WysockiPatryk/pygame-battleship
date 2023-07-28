import pygame

from code.Scenes.Scene import Scene


class BattleStage(Scene):
    name = "Battle Stage"

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
        self.screen.fill(color="aqua")

    def update(self, events: list[pygame.event]):
        pass

    def recalculate_objects(self):
        pass
