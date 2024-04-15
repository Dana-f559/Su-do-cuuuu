import pygame

from board import createBoard

# create the grid only for testing
grid = createBoard()

# set width and height
WIDTH = 550
HEIGHT = 600
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


def insert(win, position):
    i, j = position[1], position[0]
    myfont = pygame.font.Font("fonts/comic-sans/comicsans.ttf", 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                print("\nKEYDOWN")
                if grid_original[i - 1][j - 1] != 0:
                    return
                if event.key == 48:  # checking with 0
                    grid[i - 1][j - 1] = event.key - 48
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
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10:  # We are checking for valid input
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
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return


def draw_grid():
    # start
    pygame.init()

    # set width and height
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    # set the caption to the window
    pygame.display.set_caption("Sudoku")

    # set the background color
    win.fill(background_color)

    # set the font
    myfont = pygame.font.Font("fonts/comic-sans/comicsans.ttf", 35)

    # draw the sudocu grid
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    # update the screen
    pygame.display.update()

    # for the puzzle
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):

            # if the number is between 1 and 9 add it to the display
            if 0 < grid[i][j] < 10:
                value = myfont.render(
                    str(grid[i][j]), True, original_grid_element_color
                )
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    # while true check for events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0] // 50, pos[1] // 50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    draw_grid()
