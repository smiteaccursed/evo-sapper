import random

BOARD_SIZE = 10
NUM_MINES = 10
CELL_HIDDEN = -1
CELL_MINE = -2
CELL_FLAG = -3

board = [[CELL_HIDDEN for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
revealed = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
flagged = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def printBoard():
    print("    " + " ".join(map(str, range(BOARD_SIZE))))
    for i in range(BOARD_SIZE):
        row_str = f"{i} | "
        for j in range(BOARD_SIZE):
            if not revealed[i][j]:
                if flagged[i][j]:
                    row_str += "F "
                else:
                    row_str += "- "
            else:
                if board[i][j] == CELL_MINE:
                    row_str += "* "
                elif board[i][j] == 0:
                    row_str += "  "
                else:
                    row_str += str(board[i][j]) + " "
        print(row_str)


def main():
    random.seed()
    printBoard()
    row, col = map(int, input("Enter row and column: ").split())
    action = int(input("Enter action (0 for reveal, 1 for flag/unflag): "))

if __name__ == "__main__":
    main()
