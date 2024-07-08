import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # класс представляющий одного пришельца
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
        self.settings = ai_game.settings

    def check_edges(self):
        # возвращает True если пришелец находится у края экрана
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # перемещает пришельца вправо или влево
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
