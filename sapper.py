import random

BOARD_SIZE = 10
NUM_MINES = 10
CELL_HIDDEN = -1
CELL_MINE = -2
CELL_FLAG = -3

board = [[CELL_HIDDEN for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
revealed = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
flagged = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
remainingCells = BOARD_SIZE * BOARD_SIZE - NUM_MINES

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

def isValidCell(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

def placeMines():
    minesToPlace = NUM_MINES
    while minesToPlace > 0:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] == CELL_HIDDEN:
            board[row][col] = CELL_MINE
            minesToPlace -= 1

def calculateNumbers():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != CELL_MINE:
                count = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if isValidCell(ii, jj) and board[ii][jj] == CELL_MINE:
                            count += 1
                board[i][j] = count

def revealCell(row, col):
    global remainingCells
    if not isValidCell(row, col) or revealed[row][col]:
        return
    revealed[row][col] = True
    remainingCells -= 1
    if board[row][col] == CELL_MINE:
        return
    if board[row][col] == 0:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                revealCell(i, j)

def flagCell(row, col):
    if not isValidCell(row, col):
        return
    if not revealed[row][col]:
        flagged[row][col] = not flagged[row][col]

def isGameWon():
    return remainingCells == 0

def isGameLost():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == CELL_MINE and revealed[i][j]:
                return True
    return False

def main():
    random.seed()
    placeMines()
    calculateNumbers()
    while not isGameWon() and not isGameLost():
        print("\033c")
        printBoard()
        row, col = map(int, input("Enter row and column: ").split())
        action = int(input("Enter action (0 for reveal, 1 for flag/unflag): "))
        if action == 0:
            revealCell(row, col)
        elif action == 1:
            flagCell(row, col)
    
    if isGameWon():
        print("Congratulations, you won!")
    elif isGameLost():
        print("Game over, you lost!")
    printBoard()

if __name__ == "__main__":
    main()
