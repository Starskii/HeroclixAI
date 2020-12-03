from enum import Enum

from Board import Board, TileType
from Champions import *
from Display import Display


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

    @property
    def red_team(self):
        return self._red_team

    @property
    def blue_team(self):
        return self._red_team

    def __init__(self):
        if self._display_on:
            self._display = Display(self._board)
        self.reset_game()

    def reset_game(self):
        self._board = Board()
        self._current_turn = Team.RED_TEAM

    def get_available_movement(self, champion):
        available_movement = []
        if champion is type(Champion):
            position = champion.position
            start_tile = self._board.grid[position[0]][position[1]]
            for x in range(16):
                for y in range(16):
                    if self._board.grid[x][y].tile_type != TileType.DIRT:
                        self._board.get_a_star_path(start_tile, self._board.grid[x][y])
                        path = self._board.get_path_as_list(self._board.grid[x][y])
                        if len(path) < champion.speed:
                            for tile in path:
                                if tile not in available_movement:
                                    available_movement.append(tile)
        return available_movement

    def move_champion(self, champion):



game = Game()


