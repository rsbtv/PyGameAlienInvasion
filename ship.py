import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # Класс для управления кораблем
    def __init__(self, ai_game):
        # Инициализирует корабль и задает его начальную позицию
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # обновляет позицию корабля с учетом флага
        # обновляется атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        # обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        # рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # размещает корабль в центре нижней стороны
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)