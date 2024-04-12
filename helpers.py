import re

# DO NOT IMPORT HELPER 
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

# DO NOT IMPORT HELPER
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

# to solve sudocu
# mutates the list when solving. 
# returns a bool true if it was solved, if it was not returns false
def solve_sudoku(puzzle: list) -> bool:
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = -1

    return False

def checkInput(text: str) -> bool:

    # set the charachter to search only for number or .
    letter = r"(\d|\.)"

    # try to find all matches
    matches = re.search(r"^(?:\d|\.){9}$", text)

    # if matches then return true, that the input is correct
    if matches:
        return True

    # else return false
    return False