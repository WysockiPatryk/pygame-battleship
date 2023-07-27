import sys

import pygame

import code.constants as constants


def close_game():
    pygame.quit()
    sys.exit()


def get_window_size() -> tuple[int, int]:
    """
        :return: tuple(width, height) of the current video mode, or of the desktop mode if called before the
        display.set_mode is called
    """
    info_object = pygame.display.Info()
    return info_object.current_w, info_object.current_h


def limit_window_size(event) -> pygame.Surface:
    width, height = event.size
    if width < constants.MINIMUM_WINDOW_SIZE[0]:
        width = constants.MINIMUM_WINDOW_SIZE[0]
    if height < constants.MINIMUM_WINDOW_SIZE[1]:
        height = constants.MINIMUM_WINDOW_SIZE[1]
    return pygame.display.set_mode((width, height), *constants.DISPLAY_FLAGS)


def load_images() -> dict:
    return {'motorboat': pygame.image.load(constants.PATH_TO_MOTORBOAT_IMAGE),
            'yacht': pygame.image.load(constants.PATH_TO_YACHT_IMAGE),
            'sailing_ship': pygame.image.load(constants.PATH_TO_SAILING_SHIP_IMAGE),
            'container_ship': pygame.image.load(constants.PATH_TO_CONTAINER_SHIP_IMAGE)}
