from solve import solve_sudoku
from board import createBoard
from gui import run_game

grid_original, grid = createBoard()

run_game(grid, grid_original)