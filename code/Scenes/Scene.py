from abc import ABC, abstractmethod

import pygame

import code.utilities as utilities


class Scene(ABC):
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def shortcuts(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @screen.setter
    @abstractmethod
    def screen(self, value: pygame.Surface):
        self.screen = value

    @abstractmethod
    def render(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, events: list[pygame.event]):
        raise NotImplementedError

    @abstractmethod
    def recalculate_objects(self):
        """ Recalculate the sizes and positions of objects """
        raise NotImplementedError

    def handle_inputs(self, events: list[pygame.event]):
        for event in events:
            if event.type == pygame.QUIT:
                utilities.close_game()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = utilities.limit_window_size(event)
                self.recalculate_objects()
            elif event.type == pygame.KEYDOWN and event.key in self.shortcuts:
                self.shortcuts[event.key]()
