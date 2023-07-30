from unit import Unit

ROWS = 10
COLS = 10

board = [[Unit() for i in range(COLS)] for j in range(ROWS)]


def main():
    print_board()


def print_board():
    global board
    for i in board:
        for j in i:

            if j.state == True:
                print("#", end='')
            elif j.state == False:
                print("", end='')
            else:
                raise TypeError("Unit isnt the correct type")
        print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
