class Tile:
    _position = (0, 0)
    _value = 0
    _color = (200, 200, 200)

    def __init__(self, position, value):
        self._position = position
        self._value = value

    def setColor(self, value):
        self._color = value

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position


class Board:
    _grid = [[]]
    _size = (0, 0)
    _adjacency = {}
    _walled = {}

    def __init__(self):
        cols = 16
        rows = 16
        self._size = (cols, rows)
        self._grid = [[0 for i in range(self._size[0])] for j in range(self._size[1])]
        for x in range(self._size[0]):
            for y in range(self._size[1]):
                self._grid[x][y] = Tile((x, y), 0)
        for x in range(self._size[0]):
            for y in range(self._size[1]):
                self.add_adjacency(self._grid[x][y])
                self.add_walls()

    def add_walls_helper(self, *tiles):
        current = tiles[0]
        for x in range(len(tiles)):
            if x is 0:
                pass
            else:
                try:
                    self.adjacency[current.position].remove(tiles[x].position)
                except:
                    pass
                try:
                    self.adjacency[tiles[x].position].remove(current.position)
                except:
                    pass

    def add_walls(self):
        grid = self._grid
        self.add_walls_helper(grid[7][0], grid[8][0], grid[8][1])
        self.add_walls_helper(grid[3][1], grid[4][2])
        self.add_walls_helper(grid[4][1], grid[4][2], grid[5][2])
        self.add_walls_helper(grid[5][1], grid[6][1], grid[6][2], grid[5][2])
        self.add_walls_helper(grid[7][1], grid[8][0], grid[8][1], grid[8][2])
        self.add_walls_helper(grid[9][1], grid[10][1])
        self.add_walls_helper(grid[10][1], grid[9][1], grid[9][2], grid[10][2], grid[11][2])
        self.add_walls_helper(grid[11][1], grid[10][2], grid[11][2])
        self.add_walls_helper(grid[12][1], grid[11][2])
        self.add_walls_helper(grid[3][2], grid[4][2], grid[4][3])
        self.add_walls_helper(grid[4][2], grid[3][2], grid[3][3], grid[4][1], grid[5][1], grid[3][1])
        self.add_walls_helper(grid[5][2], grid[4][1], grid[5][1])
        self.add_walls_helper(grid[6][2], grid[5][1])
        self.add_walls_helper(grid[7][2], grid[8][1], grid[8][2])
        self.add_walls_helper(grid[8][2], grid[7][2], grid[7][1])
        self.add_walls_helper(grid[9][2], grid[10][1])
        self.add_walls_helper(grid[10][2], grid[10][1], grid[11][1])
        self.add_walls_helper(grid[11][2], grid[10][1], grid[11][1], grid[12][1], grid[12][2], grid[12][3])
        self.add_walls_helper(grid[12][2], grid[11][2], grid[11][3])
        self.add_walls_helper(grid[1][3], grid[2][4])
        self.add_walls_helper(grid[2][3], grid[2][4], grid[3][4])
        self.add_walls_helper(grid[3][3], grid[2][4], grid[3][4], grid[4][4], grid[4][3], grid[4][2])
        self.add_walls_helper(grid[4][3], grid[3][2], grid[3][3], grid[3][4])
        self.add_walls_helper(grid[5][3], grid[6][4])
        self.add_walls_helper(grid[6][3], grid[6][4])
        self.add_walls_helper(grid[10][3], grid[10][4], grid[11][4])
        self.add_walls_helper(grid[11][3], grid[12][3], grid[12][4], grid[11][4], grid[10][4], grid[12][2])
        self.add_walls_helper(grid[12][3], grid[11][3], grid[11][4], grid[11][2], grid[12][4], grid[13][4])
        self.add_walls_helper(grid[13][3], grid[12][4], grid[13][4])
        self.add_walls_helper(grid[14][3], grid[13][4])
        self.add_walls_helper(grid[1][4], grid[2][5], grid[2][4])
        self.add_walls_helper(grid[2][4], grid[1][4], grid[1][3], grid[2][3], grid[3][3], grid[1][5])
        self.add_walls_helper(grid[3][4], grid[2][3], grid[3][3], grid[4][3], grid[4][4])
        self.add_walls_helper(grid[4][4], grid[3][4], grid[3][3])
        self.add_walls_helper(grid[5][4], grid[6][4], grid[6][5])
        self.add_walls_helper(grid[6][4], grid[5][5], grid[5][4], grid[5][3], grid[6][3])
        self.add_walls_helper(grid[10][4], grid[10][3], grid[9][3])
        self.add_walls_helper(grid[11][4], grid[10][3], grid[11][3], grid[12][3])
        self.add_walls_helper(grid[12][4], grid[11][3], grid[12][3], grid[13][3])
        self.add_walls_helper(grid[13][4], grid[12][3], grid[13][3], grid[14][3], grid[14][4], grid[14][5])
        self.add_walls_helper(grid[14][4], grid[13][4], grid[13][5])
        self.add_walls_helper(grid[1][5], grid[2][4], grid[2][5], grid[2][6])
        self.add_walls_helper(grid[2][5], grid[1][5], grid[1][4], grid[1][6])
        self.add_walls_helper(grid[5][5], grid[6][4], grid[6][5], grid[6][6])
        self.add_walls_helper(grid[6][5], grid[5][4], grid[5][5], grid[5][6])
        self.add_walls_helper(grid[7][5], grid[7][6], grid[8][6])
        self.add_walls_helper(grid[8][5], grid[7][6], grid[8][6], grid[9][6])
        self.add_walls_helper(grid[9][5], grid[8][6], grid[9][6], grid[10][6])
        self.add_walls_helper(grid[10][5], grid[9][6], grid[10][6], grid[11][6])
        self.add_walls_helper(grid[11][5], grid[10][6], grid[11][6])
        self.add_walls_helper(grid[12][5], grid[14][4], grid[14][5])
        self.add_walls_helper(grid[14][5], grid[13][5], grid[13][4], grid[13][6], grid[14][6])
        self.add_walls_helper(grid[1][6], grid[2][5], grid[2][6], grid[2][7])
        self.add_walls_helper(grid[2][6], grid[1][5], grid[1][6], grid[1][7], grid[2][7], grid[3][7])
        self.add_walls_helper(grid[3][6], grid[2][7], grid[3][7])
        self.add_walls_helper(grid[5][6], grid[6][5], grid[6][6], grid[6][7])
        self.add_walls_helper(grid[6][6], grid[5][5], grid[5][6], grid[5][7])
        self.add_walls_helper(grid[7][6], grid[7][5], grid[8][5])
        self.add_walls_helper(grid[8][6], grid[7][5], grid[8][5], grid[9][5])
        self.add_walls_helper(grid[9][6], grid[8][5], grid[9][5], grid[10][5], grid[10][6], grid[10][7])
        self.add_walls_helper(grid[10][6], grid[9][7], grid[9][6], grid[9][5], grid[10][5], grid[11][5])
        self.add_walls_helper(grid[11][6], grid[10][5], grid[11][5])
        self.add_walls_helper(grid[13][6], grid[14][5])
        self.add_walls_helper(grid[14][6], grid[14][5])
        self.add_walls_helper(grid[1][7], grid[2][6], grid[2][7])
        self.add_walls_helper(grid[2][7], grid[3][6], grid[2][6], grid[1][6], grid[1][7])
        self.add_walls_helper(grid[3][7], grid[2][6], grid[3][6])
        self.add_walls_helper(grid[5][7], grid[6][6], grid[6][7])
        self.add_walls_helper(grid[6][7], grid[5][6], grid[5][7])
        self.add_walls_helper(grid[9][7], grid[10][6], grid[10][7], grid[10][8])
        self.add_walls_helper(grid[10][7], grid[9][6], grid[9][7], grid[9][8])
        self.add_walls_helper(grid[12][7], grid[12][8], grid[13][8])
        self.add_walls_helper(grid[13][7], grid[12][8], grid[13][8], grid[14][8])
        self.add_walls_helper(grid[14][7], grid[13][8], grid[14][8], grid[15][8])
        self.add_walls_helper(grid[15][7], grid[14][8], grid[15][8])
        self.add_walls_helper(grid[0][8], grid[0][9], grid[1][9])
        self.add_walls_helper(grid[1][8], grid[0][9], grid[1][9], grid[2][9])
        self.add_walls_helper(grid[2][8], grid[1][9], grid[2][9], grid[3][9])
        self.add_walls_helper(grid[3][8], grid[2][9], grid[3][9])
        self.add_walls_helper(grid[9][8], grid[10][8], grid[10][7])
        self.add_walls_helper(grid[10][8], grid[9][8], grid[9][7])
        self.add_walls_helper(grid[12][8], grid[12][7], grid[13][7])
        self.add_walls_helper(grid[13][8], grid[12][7], grid[13][7], grid[14][7])
        self.add_walls_helper(grid[14][8], grid[13][7], grid[14][7], grid[15][7])
        self.add_walls_helper(grid[15][8], grid[14][7], grid[15][7])
        self.add_walls_helper(grid[0][9], grid[0][8], grid[1][8])
        self.add_walls_helper(grid[1][9], grid[0][8], grid[1][8], grid[2][8], grid[2][9], grid[2][10])
        self.add_walls_helper(grid[2][9], grid[1][8], grid[2][8], grid[3][8], grid[1][9], grid[1][10])
        self.add_walls_helper(grid[3][9], grid[2][8], grid[3][8])
        self.add_walls_helper(grid[5][9], grid[6][9], grid[6][10])
        self.add_walls_helper(grid[6][9], grid[5][9], grid[5][10], grid[6][10], grid[7][10])
        self.add_walls_helper(grid[7][9], grid[6][10], grid[7][10])
        self.add_walls_helper(grid[9][9], grid[9][10], grid[10][10])
        self.add_walls_helper(grid[10][9], grid[9][10], grid[10][10], grid[11][10])
        self.add_walls_helper(grid[11][9], grid[10][10], grid[11][10])
        self.add_walls_helper(grid[13][9], grid[14][10])
        self.add_walls_helper(grid[14][9], grid[14][10])
        self.add_walls_helper(grid[1][10], grid[2][9], grid[2][10], grid[2][11])
        self.add_walls_helper(grid[2][10], grid[1][9], grid[1][10], grid[1][11])
        self.add_walls_helper(grid[5][10], grid[6][9], grid[6][10])
        self.add_walls_helper(grid[6][10], grid[5][10], grid[5][9], grid[6][9], grid[7][9])
        self.add_walls_helper(grid[7][10], grid[6][9], grid[7][9])
        self.add_walls_helper(grid[9][10], grid[9][9], grid[10][9])
        self.add_walls_helper(grid[10][10], grid[9][9], grid[10][9], grid[11][9])
        self.add_walls_helper(grid[11][10], grid[10][9], grid[11][9])
        self.add_walls_helper(grid[13][10], grid[14][10], grid[14][11])
        self.add_walls_helper(grid[14][10], grid[13][10], grid[13][11], grid[13][9], grid[14][9])
        self.add_walls_helper(grid[1][11], grid[2][10], grid[2][11])
        self.add_walls_helper(grid[2][11], grid[1][10], grid[1][11], grid[1][12], grid[2][12])
        self.add_walls_helper(grid[3][11], grid[4][11], grid[4][12])
        self.add_walls_helper(grid[4][11], grid[3][11], grid[3][12])
        self.add_walls_helper(grid[10][11], grid[10][12], grid[11][12])
        self.add_walls_helper(grid[11][11], grid[10][12], grid[11][12], grid[12][12])
        self.add_walls_helper(grid[12][11], grid[11][12], grid[12][12], grid[13][12])
        self.add_walls_helper(grid[13][11], grid[12][12], grid[13][12], grid[14][12], grid[14][11], grid[14][10])
        self.add_walls_helper(grid[14][11], grid[13][11], grid[13][10])
        self.add_walls_helper(grid[1][12], grid[2][11])
        self.add_walls_helper(grid[2][12], grid[2][11])
        self.add_walls_helper(grid[3][12], grid[4][11], grid[4][12], grid[4][13])
        self.add_walls_helper(grid[4][12], grid[3][11], grid[3][12], grid[3][13])
        self.add_walls_helper(grid[5][12], grid[6][12], grid[6][13])
        self.add_walls_helper(grid[6][12], grid[5][12], grid[5][13])
        self.add_walls_helper(grid[7][12], grid[8][12], grid[8][13])
        self.add_walls_helper(grid[8][12], grid[7][12], grid[7][13])
        self.add_walls_helper(grid[10][12], grid[10][11], grid[11][11], grid[11][12])
        self.add_walls_helper(grid[11][12], grid[10][12], grid[10][11], grid[11][11], grid[12][11])
        self.add_walls_helper(grid[12][12], grid[11][11], grid[12][11], grid[13][11])
        self.add_walls_helper(grid[13][12], grid[12][11], grid[13][11])
        self.add_walls_helper(grid[14][12], grid[13][11])
        self.add_walls_helper(grid[3][13], grid[4][12], grid[4][13], grid[4][14])
        self.add_walls_helper(grid[4][13], grid[3][12], grid[3][13], grid[3][14], grid[4][14], grid[5][14])
        self.add_walls_helper(grid[5][13], grid[6][12], grid[6][13], grid[6][14], grid[5][14], grid[4][14])
        self.add_walls_helper(grid[6][13], grid[5][12], grid[5][13])
        self.add_walls_helper(grid[7][13], grid[8][12], grid[8][13], grid[8][14])
        self.add_walls_helper(grid[8][13], grid[7][12], grid[7][13], grid[7][14], grid[8][14])
        self.add_walls_helper(grid[3][14], grid[4][13], grid[4][14])
        self.add_walls_helper(grid[4][14], grid[3][14], grid[3][13], grid[4][13], grid[5][13])
        self.add_walls_helper(grid[5][14], grid[4][13], grid[5][13])
        self.add_walls_helper(grid[7][14], grid[8][13], grid[8][14], grid[8][15])
        self.add_walls_helper(grid[8][14], grid[7][15], grid[7][14], grid[7][13], grid[8][13])
        self.add_walls_helper(grid[10][14], grid[11][14], grid[11][15])
        self.add_walls_helper(grid[11][14], grid[10][14], grid[10][15])
        self.add_walls_helper(grid[7][15], grid[8][15], grid[8][14])
        self.add_walls_helper(grid[8][15], grid[7][15], grid[7][14])
        self.add_walls_helper(grid[10][15], grid[11][15], grid[11][14])
        self.add_walls_helper(grid[11][15], grid[10][14], grid[10][15])

    def add_adjacency(self, tile):
        for x in range(self._size[0]):
            for y in range(self._size[1]):
                xdif = abs(x - tile.position[0])
                ydif = abs(y - tile.position[1])
                if xdif is 1 and ydif is 1 \
                        or xdif is 1 and ydif is 0 \
                        or xdif is 0 and ydif is 1:
                    if tile.position not in self.adjacency:
                        self.adjacency[tile.position] = [self._grid[x][y].position]
                    else:
                        self.adjacency[tile.position].append(self._grid[x][y].position)

    @property
    def grid(self):
        return self._grid

    @property
    def adjacency(self):
        return self._adjacency
