def updateBoard(board, click):
    # depending on the click => E, M, B update the rest of the board using dfs

    m = len(board)
    n = len(board[0])
    queue  = [click]
    visited = set()
    visited.add(click)

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    while queue:

        i, j = queue.pop(0)

        if board[i][j] == "M":

        elif board[i][j] == "E":

        elif board[i][j] == "B":


        for x, y  in zip(x, y):
            if i+x, j+y




    return board




