from pygame import Surface

from code.Scenes.Scene import Scene


class EndgameScreen(Scene):
    def __init__(self):
        self.objects = []

    def render(self, screen: Surface):
        print("Endgame Screen")
        screen.fill(color='crimson')

    def recalculate_objects_position(self):
        pass
