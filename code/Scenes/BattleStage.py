from pygame import Surface

from code.Scenes.Scene import Scene


class BattleStage(Scene):
    def __init__(self):
        self.objects = []

    def render(self, screen: Surface):
        print("Battle Stage")
        screen.fill(color='aqua')

    def recalculate_objects_position(self):
        pass
