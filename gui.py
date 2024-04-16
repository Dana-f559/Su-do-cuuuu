from pathlib import Path

import pygame

from vars import *

a = Path(__file__).resolve().parent


# set the status to menu


pygame.init()

myfont = pygame.font.Font(f"{a}/fonts/comic-sans/comicsans.ttf", 35)
win = pygame.display.set_mode((WIDTH, HEIGHT))


# to insert the number
def insert(win, position: tuple, event: pygame.event, grid_original:list, grid: list)->None:

    # set the i and j to the posotions
    i, j = position[1], position[0]

    try:
        # try to see if the cell the user is a populated one
        if grid_original[i - 1][j - 1] != -1:
            return

    # except index error is key was pressed outside the board
    except IndexError:
        return

    # if the key is 0, then make the cell empty
    if event.key == 48 or event.key == 8:
        # "reset" the grid cell
        grid[i - 1][j - 1] = event.key - 48

        # draw empty rectangle on the screen
        pygame.draw.rect(
            win,
            background_color,
            (
                position[0] * 50 + buffer,
                position[1] * 50 + buffer,
                50 - 2 * buffer,
                50 - 2 * buffer,
            ),
        )

        # update the screen
        pygame.display.update()
        return

    # if the key is a number add it to the
    if 0 < event.key - 48 < 10:
        # draw the empty value
        pygame.draw.rect(
            win,
            background_color,
            (
                position[0] * 50 + buffer,
                position[1] * 50 + buffer,
                50 - 2 * buffer,
                50 - 2 * buffer,
            ),
        )

        # set the number to draw
        value = myfont.render(str(event.key - 48), True, (0, 0, 0))

        # draw the number
        win.blit(value, (position[0] * 50 + 15, position[1] * 50))

        # update the grid
        grid[i - 1][j - 1] = event.key - 48

        # update the screen
        pygame.display.update()
        return
    return


def draw_grid(grid: list) -> None:
    # start
    # set width and height

    # set the caption to the window
    pygame.display.set_caption("Sudoku")

    # set the background color
    win.fill(background_color)

    # set the font
    myfont = pygame.font.Font(f"{a}/fonts/comic-sans/comicsans.ttf", 35)

    # draw the sudocu grid
    for i in range(0, 10):
        bigboi = 50 * (i + 1)
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (bigboi, 50), (bigboi, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, bigboi), (500, bigboi), 4)

        pygame.draw.line(win, (0, 0, 0), (bigboi, 50), (bigboi, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, bigboi), (500, bigboi), 2)
    # update the screen
    pygame.display.update()

    # for the puzzle
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):

            # if the number is between 1 and 9 add it to the display
            if 0 < grid[i][j] < 10:

                # set the number to draw
                value = myfont.render(
                    str(grid[i][j]), True, original_grid_element_color
                )

                # draw the number
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))

    # update the screen
    pygame.display.update()


def menu(): ...


def run_game(grid: list, solved: list, solve_sudocu: function) -> None:

    grid_original = [
        [grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))
    ]
    draw = True

    status = "Play"
    # start the game loop
    while True:
        if status == "Menu":
            menu()

        if status == "Play" and draw:
            draw_grid(grid)
            draw = False

        if status == "Solve":
            pass

        # Check for events and update status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # if the status is play
            if status == "Play":

                # check for keydown 
                if event.type == pygame.KEYDOWN:

                    # can the mouse position
                    pos = pygame.mouse.get_pos()

                    # insert the number
                    insert(
                        win, (pos[0] // 50, pos[1] // 50), event, grid_original, grid
                    )

                # if the grid on the screen is the same as
                # the solved version of it, then quit for now
                if grid == solved:
                    pygame.quit()
