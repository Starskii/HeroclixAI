from abc import abstractmethod


class Champion:
    _positionX, _positionY = 0
    _click_value = 0
    _speed = 0
    _attack = 0
    _defense = 0
    _damage = 0

    def __init__(self):
        self._click_value = 1
        self.update_stat_page()

    def get_stat_page(self):
        return [self._click_value,  # Position 0
                self._speed,  # Position 1
                self._attack,  # Position 2
                self._defense,  # Position 3
                self._damage]      # Position 4

    @abstractmethod
    def update_stat_page(self):
        pass


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


class IronMan(Champion):
    def update_stat_page(self):
        pass


class Thor(Champion):
    def update_stat_page(self):
        pass
