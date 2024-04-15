import pygame
from board import createBoard
import os
temp = [

]
for i in range(9):
    temp.append([-1, -1, -1, -1, -1, -1, -1, -1, -1])

createBoard(temp)

# font_path = os.path.join('fonts', 'comic-sans', 'COMICSANS.ttf')

# # Check if the font file exists
# if not os.path.exists(font_path):
#     raise FileNotFoundError(f"Font file '{font_path}' not found")

# set width and height
WIDTH = 550
HEIGHT = 600
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5



def draw_board(board: list):
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

    # draw the sudocu board
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    # update the screen
    pygame.display.update()

    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            if 0 < board[i][j] < 10:
                value = myfont.render(
                    str(board[i][j]), True, original_grid_element_color
                )
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()


# while true check for events
    while True:
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #     pos = pygame.mouse.get_pos()
            #     insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    draw_board(temp)
