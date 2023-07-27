from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def recalculate_objects_position(self):
        pass
