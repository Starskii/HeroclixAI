import pygame
from Board import Board, Champion
from Board import TileType
import PySimpleGUI as sg
#from Board import DefaultColor


#WHITE
BACKGROUND = (255, 255, 255)
#SILVER/GREY for regular-type tiles
DEFAULT_TILE = (200, 200, 200)
#DEFAULT_TILE = (145, 220, 250)

RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (128, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
#Water tiles
LTBLUE = (145, 220, 250)
#Dirt tiles
TAN = (210, 180, 140)
#Start_box tiles
LTPINK = (255, 210, 220)
#Grey-Green debris tiles
GG_DEBRIS = (122, 168, 130)


class Display:
    current_start = None
    current_end = None
    SIZE = 800
    WINDOW = pygame.display.set_mode((SIZE, SIZE))
    BOARD = None
    tileType = 0
    path = []
    selected_champion = None
    _game = None

    def __init__(self, board, game):
        pygame.init()
        pygame.display.set_caption("HeroClix AI")
        self.reset_display(board, game)

    def reset_display(self, board, game):
        self._game = game
        self.BOARD = board
        self.draw_background()
        self.draw_tiles()

    def get_tile(self, x, y):
        x = int(x / 50)
        y = int(y / 50)
        return self.BOARD.grid[x][y]

    @staticmethod
    def get_dice_roll():
        event, values = sg.Window('Attack Value',
                                  [[sg.T('Enter Dice Roll'), sg.In(key='-ROLL-')],
                                   [sg.B('OK'), sg.B('Cancel')]]).read(close=True)
        return values['-ROLL-']

    def draw_background(self):
        pygame.draw.rect(self.WINDOW, BLACK, (0, 0, self.SIZE, self.SIZE))

    def draw_walls(self):
        for current in self.BOARD.adjacency:
            for adjacent in self.BOARD.adjacency[current]:
                current_tile = self.get_tile(current[0]*50, current[1]*50)
                adjacent_tile = self.get_tile(adjacent[0]*50, adjacent[1]*50)
                if adjacent_tile.position[0] > current_tile.position[0]:
                    if adjacent_tile.position[1] == current_tile.position[1]:
                        # Adjacent is to the right
                        pygame.draw.rect(self.WINDOW, WHITE, (50 + (current[0] * 50), (current[1] * 50), 3, 50))
                if adjacent_tile.position[1] > current_tile.position[1]:
                    if adjacent_tile.position[0] == current_tile.position[0]:
                        # Adjacent is below
                        pygame.draw.rect(self.WINDOW, WHITE,  (2 + (current[0] * 50), 50 + (current[1] * 50), 50, 3))

    def get_tile_pixel_location(self, tile_position):
        location = [0, 0]
        location[0] = (2 + (tile_position[0] * 50))
        location[1] = (2 + (tile_position[1] * 50))
        return location

    def draw_tiles(self):
        for row in range(16):
            for col in range(16):
                color = (0, 0, 0)
                if self.BOARD.grid[col][row].use_default_color:
                    if self.BOARD.grid[col][row].tile_type == TileType.START_BOX:
                        color = LTPINK
                    elif self.BOARD.grid[col][row].tile_type == TileType.REGULAR:
                        color = DEFAULT_TILE
                    elif self.BOARD.grid[col][row].tile_type == TileType.WATER:
                        color = TURQUOISE
                    elif self.BOARD.grid[col][row].tile_type == TileType.DIRT:
                        color = TAN
                    elif self.BOARD.grid[col][row].tile_type == TileType.DEBRIS:
                        color = RED
                    pygame.draw.rect(self.WINDOW, color, (2 + (col * 50), 2 + (row * 50), 48, 48))
                else:
                    pygame.draw.rect(self.WINDOW, self.BOARD.grid[col][row].color, (2 + (col * 50), 2 + (row * 50), 48, 48))

    def reset_colors(self):
        for x in range(16):
            for y in range(16):
                self.BOARD.grid[x][y].use_default_color = True

    def left_mouse_button_event(self):
        self.reset_colors()
        t = self.get_tile(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        for champion in self.BOARD.red_team:
            if champion.position == t.position:
                self.selected_champion = champion
                self.highlight_possible_moves()
                self.mark_attackable_enemies(self._game.get_targets_in_range(champion))
        for champion in self.BOARD.blue_team:
            if champion.position == t.position:
                self.selected_champion = champion
                self.highlight_possible_moves()
                self.mark_attackable_enemies(self._game.get_targets_in_range(champion))

    def right_mouse_button_event(self):
        self.reset_colors()
        t = self.get_tile(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if self.selected_champion is not None:
            if t.champion is not None:
                self._game.attack(self.selected_champion, t.champion)
            else:
                self._game.move_champion(self.selected_champion, t)

    def middle_mouse_button_event(self):
        self.reset_colors()
        self._game.end_turn()

    def highlight_possible_moves(self):
        for tiles in self._game.get_available_movement(self.selected_champion):
            tiles.setColor(GG_DEBRIS)
            tiles.use_default_color = False

    def show_path(self, start_position, end_position):
        for tiles in self.BOARD.paths[(start_position, end_position)]:
            t = self.BOARD.get_tile(tiles)
            t.setColor(GG_DEBRIS)
            t.use_default_color = False

    def mark_attackable_enemies(self, enemies):
        pass

    def display_teams(self):
        for champions in self.BOARD.red_team:
            if not champions.KO:
                champImg = pygame.image.load(champions.image)
                self.WINDOW.blit(champImg, self.get_tile_pixel_location(champions.position))
            else:
                self.BOARD.get_tile(champions.position).set_champion(None)
                self.BOARD.red_team.remove(champions)
        for champions in self.BOARD.blue_team:
            if not champions.KO:
                champImg = pygame.image.load(champions.image)
                self.WINDOW.blit(champImg, self.get_tile_pixel_location(champions.position))
            else:
                self.BOARD.get_tile(champions.position).set_champion(None)
                self.BOARD.red_team.remove(champions)

    def run(self):
        run = self._game.display_on

        self.draw_background()
        self.draw_walls()

        while run:
            self.draw_tiles()
            self.display_teams()
            pygame.display.update()
            for event in pygame.event.get():
                # Controls loop
                if event.type == pygame.QUIT:
                    # closed out
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # left mouse button
                    self.left_mouse_button_event()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                    # middle mouse button
                    self.reset_colors()
                    self._game.end_turn()
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # right mouse button
                    self.right_mouse_button_event()
