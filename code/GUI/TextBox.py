from typing import Literal

import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, font,
                 text_color: tuple[int, int, int] = (0, 0, 0),
                 background_color: tuple[int, int, int] | None = None,
                 border_color: tuple[int, int, int] | None = (0, 0, 0),
                 text_type: Literal["text", "password"] = "text",
                 max_length: int = 10):
        super().__init__()
        self._position = (pos_x, pos_y)
        self._width = width
        self._font = font
        self._text_color = text_color
        self._background_color = background_color
        self._border_color = border_color
        self._text_type = text_type
        self._max_length = max_length
        self._visible_text = ""
        self._text_value = ""
        self._active = False
        self.image = None
        self.rect = None
        self.render_text()

    def render_text(self):
        t_surf = self._font.render(self._visible_text, True, self._text_color, self._background_color)
        self.image = pygame.Surface((max(self._width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                    pygame.SRCALPHA)
        if self._background_color:
            self.image.fill(self._background_color)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self._border_color, self.image.get_rect().inflate(0, 0), 2)
        self.rect = self.image.get_rect(topleft=self._position)

    def update(self, events: list[pygame.event]):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self._active:
                if event.key == pygame.K_RETURN:
                    self._active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.__remove_last_character()
                else:
                    self.__update_text(event)
                self.render_text()

    def __remove_last_character(self):
        self._text_value = self._text_value[:-1]
        self._visible_text = self._visible_text[:-1]

    def __update_text(self, event):
        if len(self._text_value) < self._max_length:
            self._text_value += event.unicode
            if self._text_type == "password":
                self._visible_text += "x"
            else:
                self._visible_text += event.unicode
