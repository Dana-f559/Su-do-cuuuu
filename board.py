import random


def createBoard(dificutly: int = 50):
    temp = []
    for i in range(9):
        temp.append([-1, -1, -1, -1, -1, -1, -1, -1, -1])

    a = generate_board_full(temp)
    if not a:
        return False


    solved = [temp[x][y] for y in range(len(temp[0])) for x in range(len(temp))]
    # how many numbers to remove
    remove_numbers(temp, dificutly)

    return solved, temp


def generate_board_full(puzzle: list) -> bool:
    # find the row and column where the number is -1
    row, col = find_next_empty(puzzle)

    # if row is None, then we solved it
    if row is None:
        return True

    # for numbers from 1 to 9, try this guess
    for guesses in range(1, 10):
        # if the guess is valid
        guess = random.randint(1, 9)
        if is_valid(puzzle, guess, row, col):

            # set it in the list
            puzzle[row][col] = guess

            # use recursion to continue
            if generate_board_full(puzzle):
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


def remove_numbers(board: list, difficulty: int):
    # Remove numbers from the grid to create the puzzle
    num_to_remove = 81 - difficulty
    while num_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            # Temporarily store the cell value
            temp = board[row][col]
            # Remove the number from the grid
            board[row][col] = -1
            
            num_to_remove -= 1


if __name__ == "__main__":
    a, b = createBoard()
    print(a)
    print(b)
