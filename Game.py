from enum import Enum

from Board import Board, TileType
from Champions import *
from Display import Display
from Player import Player


class Team(Enum):
    RED_TEAM = 0
    BLUE_TEAM = 1


class Game:
    _board = Board()
    _red_team = []
    _blue_team = []
    _current_turn = Team.RED_TEAM
    _display_on = True
    _display = None
    _player = None

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
            cost = len(path)
        return cost

    def __init__(self):
        self._player = Player(self, self._board)
        if self._display_on:
            self._display = Display(self._board, self)
        self.run_game()

    def reset_game(self):
        self._board.reset_board()
        self._current_turn = Team.RED_TEAM

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

    def move_champion(self, champion, tile):
        available_moves = self.get_available_movement(champion)
        if tile in available_moves:
            self._board.get_tile(champion.position).set_champion(None)
            tile.set_champion(champion)

    def run_game(self):
        run = True
        i = 0
        while run:
            if i != 0:
                self._player.make_move()
            if self._display_on:
                self._display.run()
            i += 1




