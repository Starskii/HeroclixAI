from Board import Board

size = (16, 16)

board = Board(size[0], size[1])

for x in range(size[0]):
    line = ""
    for y in range(size[1]):
        line += "(" + str(board.grid[x][y].position[0]) + "," + str(board.grid[x][y].position[1]) + ") "
    print(line)