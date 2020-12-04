from abc import abstractmethod


class Champion:
    name = ""
    _position = (0, 0)
    _click_value = 0
    _speed = 0
    _attack = 0
    _defense = 0
    _damage = 0
    _range = 0
    _action_tokens = 0
    _KO = False
    _img = None

    def __init__(self, position):
        self._position = position
        self._click_value = 1
        self.update_stat_page()

    def set_champion_image(self, img):
        self._img = img

    def reset_champion(self):
        self._click_value = 1
        self.update_stat_page()

    def get_stat_page(self):
        return [self._click_value,  # Position 0
                self._speed,  # Position 1
                self._attack,  # Position 2
                self._defense,  # Position 3
                self._damage,   # Position 4
                self._range]    #position 5

    def set_click_value(self, value):
        self._click_value += value
        self.update_stat_page()

    @property
    def action_tokens(self):
        return self._action_tokens

    @property
    def KO(self):
        return self._KO

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def damage(self):
        return self._damage

    @abstractmethod
    def update_stat_page(self):
        pass

    @property
    def speed(self):
        return self._speed

    @property
    def position(self):
        return self._position

    @property
    def image(self):
        return self._img

    @property
    def range(self):
        return self._range

    def set_position(self, position):
        self._position = position

    def set_action_tokens(self, value):
        self._action_tokens = value


class CaptainAmerica(Champion):
    def update_stat_page(self):
        self._range = 5
        if self._click_value is 1:
            self._KO = False
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
        if self._click_value > 7:
            self._KO = True


class IronMan(Champion):
    def update_stat_page(self):
        self._range = 7
        if self._click_value is 1:
            self._KO = False
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
        if self._click_value > 7:
            self._KO = True


class Thor(Champion):
    def update_stat_page(self):
        self._range = 6
        if self._click_value is 1:
            self._KO = False
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
        if self._click_value > 7:
            self._KO = True

