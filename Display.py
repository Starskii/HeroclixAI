import pygame
from Board import Board
from Board import TileType
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
    currentStart = None
    currentEnd = None
    SIZE = 800
    WINDOW = pygame.display.set_mode((SIZE, SIZE))
    BOARD = Board()
    #prevColor = DEFAULT_TILE
    #tempColor = DEFAULT_TILE
    tileType = 0

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("HeroClix AI")
        self.draw_background()
        self.draw_tiles()
        self.run()

    def get_tile(self, x, y):
        x = int(x / 50)
        y = int(y / 50)
        return self.BOARD.grid[x][y]

    def draw_background(self):
        pygame.draw.rect(self.WINDOW, BLACK, (0, 0, self.SIZE, self.SIZE))

    def draw_walls(self):
        for current in self.BOARD.adjacency:
            for adjacent in self.BOARD.adjacency[current]:
                current_tile = self.get_tile(current[0]*50, current[1]*50)
                adjacent_tile = self.get_tile(adjacent[0]*50, adjacent[1]*50)
                d1 = False
                d2 = False
                if adjacent_tile.position[0] > current_tile.position[0]:
                    if adjacent_tile.position[1] == current_tile.position[1]:
                        # Adjacent is to the right
                        pygame.draw.rect(self.WINDOW, WHITE, (50 + (current[0] * 50), (current[1] * 50), 3, 50))
                if adjacent_tile.position[1] > current_tile.position[1]:
                    if adjacent_tile.position[0] == current_tile.position[0]:
                        # Adjacent is below
                        pygame.draw.rect(self.WINDOW, WHITE,  (2 + (current[0] * 50), 50 + (current[1] * 50), 50, 3))

    def draw_tiles(self, *tiles):
        for row in range(16):
            for col in range(16):
                pygame.draw.rect(self.WINDOW, self.BOARD.grid[col][row].color, (2 + (col * 50), 2 + (row * 50), 48, 48))

    def set_start(self, tile):
        if self.currentStart is not None:
            if self.currentStart.tile_type == 'REGULAR':
                self.currentStart.setColor(DEFAULT_TILE)
            elif self.currentStart.tile_type == 'WATER':
                self.currentStart.setColor(LTBLUE)
            elif self.currentStart.tile_type == 'DIRT':
                self.currentStart.setColor(TAN)
            elif self.currentStart.tile_type == 'START_BOX':
                self.currentStart.setColor(LTPINK)
            elif self.currentStart.tile_type == 'DEBRIS':
                self.currentStart.setColor(GG_DEBRIS)
            #self.currentStart.setColor(DEFAULT_TILE)
        if tile is not None and not (tile.position == (7,7)
                or tile.position == (7,8) or tile.position == (8,7)
                or tile.position == (8,8)):
            self.currentStart = tile
            tile.setColor(GREEN)

    def set_end(self, tile):
        if self.currentEnd is not None:
            if self.currentEnd.tile_type == 'REGULAR':
                self.currentEnd.setColor(DEFAULT_TILE)
            elif self.currentEnd.tile_type == 'WATER':
                self.currentEnd.setColor(LTBLUE)
            elif self.currentEnd.tile_type == 'DIRT':
                self.currentEnd.setColor(TAN)
            elif self.currentEnd.tile_type == 'START_BOX':
                self.currentEnd.setColor(LTPINK)
            elif self.currentEnd.tile_type == 'DEBRIS':
                self.currentEnd.setColor(GG_DEBRIS)
            #self.currentEnd.setColor(DEFAULT_TILE)
        if tile is not None and not (tile.position == (7,7)
                  or tile.position == (7,8) or tile.position == (8,7)
                  or tile.position == (8,8)):
            self.currentEnd = tile
            tile.setColor(RED)

    def left_mouse_button_event(self):
        t = self.get_tile(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.set_start(t)

    def right_mouse_button_event(self):
        t = self.get_tile(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.set_end(t)

    def middle_mouse_button_event(self):
        self.set_start(None)
        self.set_end(None)

    def run_checks(self):
        if self.currentStart is not None and self.currentEnd is not None:
            self.BOARD.get_a_star_path(self.currentStart, self.currentEnd)
            self.display_path()

    def display_path(self):
        for x in range(16):
            for y in range(16):
                node = self.BOARD.grid[x][y]
                if node is not self.currentStart and node is not self.currentEnd:
                    if self.BOARD.grid[x][y].tile_type == 'REGULAR':
                        node.setColor(DEFAULT_TILE)
                    elif self.BOARD.grid[x][y].tile_type == 'WATER':
                        node.setColor(LTBLUE)
                    elif self.BOARD.grid[x][y].tile_type == 'DIRT':
                        node.setColor(TAN)
                    elif self.BOARD.grid[x][y].tile_type == 'START_BOX':
                        node.setColor(LTPINK)
                    elif self.BOARD.grid[x][y].tile_type == 'DEBRIS':
                        node.setColor(GG_DEBRIS)
                    #node.setColor(DEFAULT_TILE)
        self.currentEnd.parent.setColor(TURQUOISE)
        node = self.currentEnd.parent
        while node.parent is not node:
            node.parent.setColor(TURQUOISE)
            node = node.parent
        node.setColor(GREEN)

    def run(self):
        run = True
        while run:
            self.draw_background()
            self.draw_walls()
            self.draw_tiles()
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
                    self.middle_mouse_button_event()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # right mouse button
                    self.right_mouse_button_event()
            self.run_checks()
