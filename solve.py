# to solve sudocu
# mutates the list when solving.
# returns a bool true if it was solved, if it was not returns false
def solve_sudoku(puzzle: list) -> bool:
    # find the row and column where the number is -1
    row, col = find_next_empty(puzzle)

    # if row is None, then we solved it
    if row is None:
        return True

    # for numbers from 1 to 9, try this guess
    for guess in range(1, 10):
        # if the guess is valid
        if is_valid(puzzle, guess, row, col):

            # set it in the list
            puzzle[row][col] = guess

            # use recursion to continue
            if solve_sudoku(puzzle):
                return True

        # if the guess is not valid, set -1 in the list
        puzzle[row][col] = -1

    # return false if there was a mistake in previos cells.
    return False


# DO NOT IMPORT HELPER
def find_next_empty(puzzle: list) -> tuple:

    # for each element is the 2d list
    for r in range(9):
        for c in range(9):
            # if the element is == -1 return its location
            if puzzle[r][c] == -1:
                return r, c

    # else it will return none
    return None, None


# DO NOT IMPORT HELPER
def is_valid(puzzle: list, guess: int, row: int, col: int) -> bool:

    # get the row
    row_vals = puzzle[row]

    # if guess is in the row then the guess is False
    if guess in row_vals:
        return False

    # get the column
    col_vals = [puzzle[i][col] for i in range(9)]

    # if guess is in the column then the guess is False
    if guess in col_vals:
        return False

    # get the 3 by 3 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # checks if the guess is in the 3 by 3 grid
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):

            # if yes then the guess is False
            if puzzle[r][c] == guess:
                return False

    # return True is passed
    return True
