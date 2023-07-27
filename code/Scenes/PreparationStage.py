import pygame

from code.Scenes.Scene import Scene


class PreparationStage(Scene):
    name = "Preparation Stagen"

    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        self.objects = []
        self.background_color = "green3"

    @property
    def shortcuts(self):
        return {pygame.K_LEFT: self.change_color_to_black}

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    def render(self):
        self.screen.fill(color=self.background_color)

    def update(self):
        print("Preparation Stage - update()")

    def recalculate_objects(self):
        print("PreparationStage - recalculate_objects()")

    def change_color_to_black(self):
        self.background_color = "black"
