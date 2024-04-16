import pygame
from pathlib import Path

a = Path(__file__).resolve().parent

# set width and height
WIDTH = 550
HEIGHT = 600

# the background color
background_color = (251, 247, 245)

# element color
original_grid_element_color = (52, 31, 151)

# buffer
buffer = 5

# set the status to menu
status = "Menu"

pygame.init()

# to insert the number
def insert(win, position: tuple):
    # set the i and j to the posotions
    i, j = position[1], position[0]

    # set the fount
    myfont = pygame.font.Font(f"{a}/fonts/comic-sans/comicsans.ttf", 35)

    # check for events
    while True:
        for event in pygame.event.get():
            # if the event is quit, then quit
            if event.type == pygame.QUIT:
                return
            
            # if the event is key down
            if event.type == pygame.KEYDOWN:

                # if the cell clicked on is not empty, return
                if grid_original[i - 1][j - 1] != -1:
                    return
                
                # if the key is 0, then make the cell empty
                if event.key == 48: 

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


def draw_grid():
    # start
    # set width and height
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    # set the caption to the window
    pygame.display.set_caption("Sudoku")

    # set the background color
    win.fill(background_color)

    # set the font
    myfont = pygame.font.Font(f"{a}/fonts/comic-sans/comicsans.ttf", 35)

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

                # set the number to draw
                value = myfont.render(
                    str(grid[i][j]), True, original_grid_element_color
                )

                # draw the number
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))

    # update the screen
    pygame.display.update()

    # while true check for events
    while True:
        for event in pygame.event.get():

            # if the event is mouse button up, and its left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                # get the mouse position
                pos = pygame.mouse.get_pos()

                # check for numbers and insert the value 
                insert(win, (pos[0] // 50, pos[1] // 50))

            # if the event is quit, quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def menu():
    ...


def run_game(grids: list, solved: list):

    global grid
    grid = grids

    global grid_original
    grid_original = solved

    if status == "Menu":
        draw_grid()


    # # start the game loop
    # while True:
    #     if status == "Menu":
    #         menu()

    #     elif status == "Play":
    #         draw_grid()

    #     elif status == "Solve":
    #        pass

    #     # Check for events and update status
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             return