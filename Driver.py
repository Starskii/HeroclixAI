from Game import Game
from Board import Board
from Player import Player
import cProfile

pr = cProfile.Profile()
pr.enable()

game = Game()
board = game.board
player = Player(game, board)

pr.disable()
# after your program ends
pr.print_stats(sort="calls")