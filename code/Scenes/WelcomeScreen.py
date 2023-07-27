from pygame import Surface

from code.Scenes.Scene import Scene


class WelcomeScreen(Scene):
    def __init__(self):
        self.objects = []

    def render(self, screen: Surface):
        print("Welcome Screen")
        screen.fill(color='aliceblue')

    def recalculate_objects_position(self):
        pass
