import pygame
from Board import Board, Champion
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
    current_start = None
    current_end = None
    SIZE = 800
    WINDOW = pygame.display.set_mode((SIZE, SIZE))
    BOARD = Board()
    #prevColor = DEFAULT_TILE
    #tempColor = DEFAULT_TILE
    tileType = 0
    path = []
    selected_champion = None
    game = None

    def __init__(self, board):
        pygame.init()
        pygame.display.set_caption("HeroClix AI")
        self.BOARD = board
        self.draw_background()
        self.draw_tiles()
        self.run()

    def get_tile(self, x, y):
        x = int(x / 50)
        y = int(y / 50)
        return self.BOARD.grid[x][y]

    def get_position(self, position):
        x = int(position[0]/50)
        y = int(position[1] / 50)
        ret = (x, y)
        return ret

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

    def set_start(self, tile):
        if tile is not None:
            if tile.tile_type != TileType.DIRT:
                self.current_start = tile
                tile.setColor(GREEN)
                if self.current_end is None and self.current_start:
                    self.current_end = tile
        else:
            self.current_start = None

    def set_end(self, tile):
        if tile is not None:
            if tile.tile_type != TileType.DIRT:
                self.current_end = tile
                if self.current_start is None:
                    self.current_start = tile
        else:
            self.current_end = None

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

    def right_mouse_button_event(self):
        self.reset_colors()
        t = self.get_tile(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if self.selected_champion is not None:
            self.BOARD.get_a_star_path(self.BOARD.get_tile(self.selected_champion.position), t)
            path = self.get_path_as_list(t)
            if len(path) < self.selected_champion.speed:
                self.selected_champion.set_position(t.position)
                self.selected_champion = None

    def middle_mouse_button_event(self):
        position = self.get_position((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        self.BOARD.red_team[0].set_position(position)

    def run_checks(self):
        if self.current_start is not None and self.current_end is not None:
            self.BOARD.get_a_star_path(self.current_start, self.current_end)
            self.set_color_for_path()

    def highlight_possible_moves(self):
        position = self.selected_champion.position
        start_tile = self.BOARD.grid[position[0]][position[1]]
        for x in range(16):
            for y in range(16):
                if self.BOARD.grid[x][y].tile_type != TileType.DIRT:
                    self.BOARD.get_a_star_path(start_tile, self.BOARD.grid[x][y])
                    path = self.get_path_as_list(self.BOARD.grid[x][y])
                    if len(path) < self.selected_champion.speed:
                        for tile in path:
                            tile.setColor(GG_DEBRIS)
                            tile.use_default_color = False

    def get_path_as_list(self, end):
        node = end
        path = []
        while node.parent is not node:
            path.append(node)
            node = node.parent
        path.append(node)
        return path

    def set_color_for_path(self):
        node = self.current_end
        node.setColor(PURPLE)
        self.path = []
        while node.parent is not node:
            self.path.append(node)
            node.parent.setColor(PURPLE)
            node = node.parent
        self.path.append(node)
        node.parent.setColor(PURPLE)

    def display_teams(self):
        for champions in self.BOARD.red_team:
            self.WINDOW.blit(champions.image, self.get_tile_pixel_location(champions.position))
        for champions in self.BOARD.blue_team:
            self.WINDOW.blit(champions.image, self.get_tile_pixel_location(champions.position))

    def run(self):
        run = True

        self.draw_background()
        self.draw_walls()

        while run:
            self.run_checks()
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
                    self.middle_mouse_button_event()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # right mouse button
                    self.right_mouse_button_event()
