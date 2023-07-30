from unit import Unit
import random
ROWS = 10
COLS = 50

board = [[Unit() for i in range(COLS)] for j in range(ROWS)]


def main():

    print("Scrambled")
    scramble()
    print_board()


def logic():
    for i in board:
        for cell in i:
            print("wtf do i do")


    # Any live cell with 0 or 1 live neighbors dies (underpopulation)
    # Any live cell with 2 or 3 live neighbors stays alive
    # any live cell with more than 3 live neighbors dies (overpopulation)
    # any dead cell with exactly 3 neighbors becomes alive, by reproduction



def print_board():
    global board
    for i in board:
        for j in i:
            if j.state == True:
                print("#", end='')
            elif j.state == False:
                print(" ", end='')
            else:
                raise TypeError("Unit isnt the correct type")
        print("")

def scramble():
    for i in board:
        for j in i:
            int = random.randint(0,1)
            if int == 0:
                j.state = False
            elif int == 1:
                j.state = True
            else:
                raise Exception("wtf happened")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
