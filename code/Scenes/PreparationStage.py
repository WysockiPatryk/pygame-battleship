from pygame import Surface

from code.Scenes.Scene import Scene


class PreparationStage(Scene):
    def __init__(self):
        self.objects = []

    def render(self, screen: Surface):
        print("Preparation Stage")
        screen.fill(color='green3')

    def recalculate_objects_position(self):
        pass
