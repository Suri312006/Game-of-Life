from unit import Unit
import random
import pygame
import pygame.gfxdraw



ROWS = 500
COLS = 500
SIZE = 2

board = [[Unit() for i in range(COLS)] for j in range(ROWS)]

pygame.display.set_caption("Game of Life")
def main():


    screen = pygame.display.set_mode((ROWS*SIZE, COLS*SIZE))
    clock = pygame.time.Clock()
    running = True
    scramble()
    logic()
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                cell.draw(i*SIZE, j*SIZE, SIZE, screen=screen)


        # RENDER YOUR GAME HERE
        logic()
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()



def logic():
    for i in range(len(board)):
        for j in range(len(board[i])):
            cell = board[i][j]
            # print(f'cell: {i},{j}')
            neighbors = []
            # corner cases
            if i == 0 and j == 0:
                neighbors = [
                    board[i][j + 1],
                    board[i + 1][j], board[i + 1][j + 1]]
            elif i == 0 and j == len(board[i])-1:
                neighbors = [
                    board[i][j - 1],
                    board[i + 1][j - 1], board[i + 1][j]]

            elif i == len(board) - 1 and j == 0:
                neighbors = [board[i - 1][j], board[i - 1][j+1],
                             board[i][j + 1],
                             ]

            elif i == len(board) - 1 and j == len(board[i])-1:
                neighbors = [board[i - 1][j - 1], board[i - 1][j],
                             board[i][j - 1]
                             ]

            # top and bottom rows
            elif i == 0:
                neighbors = [
                    board[i][j - 1], board[i][j+1],
                    board[i + 1][j - 1], board[i + 1][j], board[i + 1][j + 1]]

            elif i == len(board) - 1:
                neighbors = [board[i - 1][j - 1], board[i - 1][j], board[i - 1][j],
                             board[i][j - 1], board[i][j + 1],
                             ]

            # left and right columns

            elif j == 0:
                neighbors = [board[i - 1][j], board[i - 1][j+1],
                             board[i][j + 1],
                             board[i + 1][j], board[i + 1][j + 1]]

            elif j == len(board[i])-1:
                neighbors = [board[i - 1][j - 1], board[i - 1][j],
                             board[i][j - 1],
                             board[i + 1][j - 1], board[i + 1][j]]

            else:
                neighbors = [board[i - 1][j - 1], board[i - 1][j], board[i - 1][j+1],
                             board[i][j - 1], board[i][j + 1],
                             board[i + 1][j - 1], board[i + 1][j], board[i + 1][j + 1]]

            living = 0
            for neighbor in neighbors:
                if neighbor.state:
                    living += 1

            # Any live cell with 0 or 1 live neighbors dies (underpopulation)
            if living == 0 or living == 1:
                cell.die()
            # Any live cell with 2 or 3 live neighbors stays alive
            if cell.state and (living == 2 or living == 3):
                cell.alive()
            # any live cell with more than 3 live neighbors dies (overpopulation)
            if living > 3:
                cell.die()
            # any dead cell with exactly 3 neighbors becomes alive, by reproduction
            if not cell.state and living == 3:
                cell.alive()


def print_board():
    global board
    for i in range(len(board[0])):
        print("_", end = '')
    print('')
    for i in board:
        for j in i:
            if j.state == True:
                print("#", end='')
            elif j.state == False:
                print(" ", end='')
            else:
                raise TypeError("Unit isnt the correct type")
        print("")
    for i in range(len(board[len(board)-1])):
        print("_", end='')
    print('')


def scramble():
    for i in board:
        for j in i:
            int = random.randint(0, 100)
            if int < 95:
                j.state = False
            elif int >= 95:
                j.state = True
            else:
                raise Exception("wtf happened")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    pygame.init()
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
