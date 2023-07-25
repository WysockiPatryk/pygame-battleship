import pygame


def get_window_size() -> tuple:
    """
        :return: tuple(width, height) of the current video mode, or of the desktop mode if called before the
        display.set_mode is called
    """
    info_object = pygame.display.Info()
    return info_object.current_w, info_object.current_h
