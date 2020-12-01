from abc import abstractmethod
import pygame


class Champion:
    _position = (0, 0)
    _click_value = 0
    _speed = 0
    _attack = 0
    _defense = 0
    _damage = 0
    _img = None

    def __init__(self, position):
        self._position = position
        self._click_value = 1
        self.update_stat_page()
        self.set_champion_image()

    def get_stat_page(self):
        return [self._click_value,  # Position 0
                self._speed,  # Position 1
                self._attack,  # Position 2
                self._defense,  # Position 3
                self._damage]      # Position 4

    @abstractmethod
    def set_champion_image(self):
        pass

    @abstractmethod
    def update_stat_page(self):
        pass

    @property
    def position(self):
        return self._position

    @property
    def image(self):
        return self._img

    def set_position(self, position):
        self._position = position


class CaptainAmerica(Champion):
    def update_stat_page(self):
        if self._click_value is 1:
            self._speed = 8
            self._attack = 11
            self._defense = 17
            self._damage = 3
        elif 1 < self._click_value < 4:
            self._speed = 7
            self._attack = 10
            self._defense = 17
            self._damage = 3
        elif 3 < self._click_value < 6:
            self._speed = 6
            self._attack = 9
            self._defense = 16
            self._damage = 2
        else:
            self._speed = 5
            self._attack = 9
            self._defense = 17
            self._damage = 2

    def set_champion_image(self):
        self._img = pygame.image.load('images/captain_america.png')


class IronMan(Champion):
    def update_stat_page(self):
        if self._click_value is 1:
            self._speed = 10
            self._attack = 10
            self._defense = 18
            self._damage = 4
        elif 1 < self._click_value < 4:
            self._speed = 10
            self._attack = 10
            self._defense = 17
            self._damage = 3
        elif 3 < self._click_value < 6:
            self._speed = 9
            self._attack = 9
            self._defense = 17
            self._damage = 2
        else:
            self._speed = 8
            self._attack = 9
            self._defense = 16
            self._damage = 2

    def set_champion_image(self):
        self._img = pygame.image.load('images/iron_man.png')


class Thor(Champion):
    def update_stat_page(self):
        if self._click_value is 1:
            self._speed = 10
            self._attack = 11
            self._defense = 18
            self._damage = 4
        elif 1 < self._click_value < 4:
            self._speed = 10
            self._attack = 11
            self._defense = 17
            self._damage = 4
        elif 3 < self._click_value < 7:
            self._speed = 10
            self._attack = 10
            self._defense = 17
            self._damage = 3
        elif 6 < self._click_value < 9:
            self._speed = 9
            self._attack = 9
            self._defense = 17
            self._damage = 3
        else:
            self._speed = 9
            self._attack = 9
            self._defense = 16
            self._damage = 3

    def set_champion_image(self):
        self._img = pygame.image.load('images/thor.png')

