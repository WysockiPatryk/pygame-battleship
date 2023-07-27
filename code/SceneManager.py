from code.Scenes.Scene import Scene


class SceneManager:
    def __init__(self, screen):
        self.screen = screen

    def switch_scene_to(self, scene: Scene) -> Scene:
        scene.render(self.screen)
        return scene
