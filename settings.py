class Settings:
    # класс для хранения всех настроек игры

    def __init__(self):
        # инициализирует статические настройки игры
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо а -1 - влево
        self.fleet_direction = 1
        self.ship_limit = 3

        # Темп ускорения игры
        self.speedup_scale = 1.5
        # ТЕм роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # инициализирует настройки, изменяющиеся в ходе игры
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение вправо,а -1 - влево
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        # увеличивает настройки скорости и стоиимость пришельцев
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
