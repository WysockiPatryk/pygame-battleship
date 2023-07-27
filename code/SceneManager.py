from code.Scenes.Scene import Scene


class SceneManager:
    def __init__(self):
        self.active_scene = None

    def set_scene(self, scene: Scene):
        self.active_scene = scene
