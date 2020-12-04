import time
from enum import Enum
from random import randint

from Board import Board, TileType
from Champions import *
from Display import Display
from Player import Player, currentPlayer


class Team(Enum):
    RED_TEAM = 0
    BLUE_TEAM = 1


class Game:
    _board = Board()
    _current_turn = Team.RED_TEAM
    _display_on = True
    _display = None
    _player = None
    _is_AI = True
    counter = 0

    @property
    def is_AI_game(self):
        return self._is_AI

    @property
    def display_on(self):
        return self._display_on

    @property
    def current_turn(self):
        return self._current_turn

    @property
    def red_team(self):
        return self._red_team

    @property
    def blue_team(self):
        return self._blue_team

    @property
    def board(self):
        return self._board

    @staticmethod
    def determine_cost_of_movement(champion, path):
        cost = 0
        if type(champion) is CaptainAmerica:
            for tiles in path:
                if tiles.tile_type is TileType.WATER:
                    cost += 2
                else:
                    cost += 1
        else:
            cost = len(path)-2
        return cost

    def __init__(self):
        self._player = Player(self, self._board)
        self._display = Display(self._board, self)
        self.run_game()

    def get_current_team(self):
        if self._current_turn is Team.RED_TEAM:
            return self._board.red_team
        else:
            return self._board.blue_team

    def reset_game(self):
        self._board.reset_board()
        self._current_turn = Team.RED_TEAM
        Game.counter = 0

    def get_available_movement(self, champion):
        available_movement = []
        position = champion.position
        start_tile = self._board.grid[position[0]][position[1]]
        for x in range(16):
            for y in range(16):
                if self._board.grid[x][y].tile_type != TileType.DIRT and (start_tile.position, self._board.grid[x][y].position) in self._board.paths:
                    path = self._board.paths[(start_tile.position, self._board.grid[x][y].position)]
                    if len(path) < champion.speed:
                        tile_path = []
                        for values in path:
                            tile_path.append((self._board.get_tile(values)))
                        cost = self.determine_cost_of_movement(champion, tile_path)
                        if cost < champion.speed:
                            for tile in tile_path:
                                if tile not in available_movement and tile.champion is None:
                                    available_movement.append(tile)
        return available_movement

    def check_for_breakaway(self, champion):
        breakaway = False
        enemy_team = None
        if self._current_turn == Team.RED_TEAM:
            enemy_team = self._board.blue_team
        else:
            enemy_team = self._board.red_team
        for enemies in enemy_team:
            if len(self._board.paths[(champion.position, enemies.position)]) == 2:
                if self.get_breakaway_roll() == 1:
                    breakaway = True
        return breakaway

    def get_breakaway_roll(self):
        if self._is_AI:
            return randint(0, 1)
        else:
            # Get roll from user
            pass

    def move_champion(self, champion, tile):
        print("\n")
        if self.check_for_breakaway(champion):
            print(champion.name + "'s move failed due to failing breakaway")
        else:
            available_moves = self.get_available_movement(champion)
            if tile in available_moves:
                print(champion.name + " moves from " + str(champion.position) + " to " + str(tile.position))
                self._display.show_path(champion.position, tile.position)
                self._board.get_tile(champion.position).set_champion(None)
                tile.set_champion(champion)

    @staticmethod
    def minimum_distance(champion, enemy):
        x_dif = abs(champion.position[0] - enemy.position[0])
        y_dif = abs(champion.position[1] - enemy.position[1])
        leftover = abs(x_dif - y_dif)
        if x_dif < y_dif:
            return x_dif + leftover
        else:
            return y_dif + leftover

    def attack(self, champion, enemy):
        if self._is_AI:
            roll = randint(2, 12)
        else:
            # get roll from user
            pass
        if roll == 12:
            enemy.set_click_value(champion.damage + 1)
            print(champion.name + " hits " + enemy.name + " for critical damage")
            print(enemy.name + " is now at click level: " + str(enemy.click_value))
        elif roll == 2:
            champion.set_click_value(1)
            print(champion.name + " hits himeself for 1 damage")
            print(champion.name + " is now at click level: " + str(champion.click_value))
        else:
            if champion.attack + roll > enemy.defense:
                enemy.set_click_value(champion.damage)
                print(champion.name + " hits " + enemy.name)
                print(enemy.name + " is now at click level: " + str(enemy.click_value))

    def get_targets_in_range(self, champion):
        if self._current_turn == Team.RED_TEAM:
            enemy_team = self._board.blue_team
        else:
            enemy_team = self._board.red_team
        target_in_range_list = []
        for enemies in enemy_team:
            if len(self._board.paths[(champion.position, enemies.position)]) == self.minimum_distance(champion, enemies) + 1:
                if len(self._board.paths[(champion.position, enemies.position)]) < champion.range:
                    target_in_range_list.append(enemies)
        return target_in_range_list

    def get_current_player(self):
        if self._is_AI:
            return currentPlayer.AI
        if self._current_turn == Team.RED_TEAM:
            return currentPlayer.PLAYER
        else:
            return currentPlayer.AI

    def end_turn(self):
        if self._current_turn == Team.RED_TEAM:
            self._current_turn = Team.BLUE_TEAM
        else:
            self._current_turn = Team.RED_TEAM

    def check_win(self):
        win = True
        if self._current_turn == Team.RED_TEAM:
            enemy_team = self._board.blue_team
        else:
            enemy_team = self._board.red_team
        for champion in enemy_team:
            if not champion.KO:
                win = False
        return win

    @staticmethod
    def game_broken():
        Game.counter += 1
        if Game.counter > 250:
            return True
        else:
            return False

    def run_game(self):
        red_wins = 0
        blue_wins = 0
        run = True
        while run:
            if self._display_on:
                self._display.run()
            self._player.make_move()
            run = not self.check_win()
        if self._current_turn == Team.RED_TEAM:
            red_wins += 1
        else:
            blue_wins += 1
        print("Red: " + str(red_wins) + ", Blue: " + str(blue_wins))
        self.reset_game()



