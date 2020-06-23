# n_queens = []
# for i in range(row):
#
#     for j in range(col):
#     if isValid(grid[row][col]):
#         nqueens.append((row,col))
#         n_queens -=1


def printGrid(grid):
    print "-------------"
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                print "1",
            else:
                print "0",
        print


def isValid(grid, row, col):

    for i in range(col):
        if grid[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if grid[i][j] == 1:
            return False

    for i, j in zip(range(row, 4, -1), range(col, -1, -1)):
        if grid[i][j] == 1:
            return False

    return True


def place_n_queens(grid, col):
    if col == 4:
        return True # WHAT!!!!!!!

    for i in range(4):
        if isValid(grid, i, col):
            grid[i][col] = 1

            if place_n_queens(grid, col+1) == True:
                return True

    grid[i][col] = 0

    return False


if __name__ == "__main__":

    grid = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
    ]

    N = 4
    printGrid(grid)
    place_n_queens(grid, 0)
    printGrid(grid)