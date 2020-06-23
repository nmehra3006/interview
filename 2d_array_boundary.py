def arr_boundary(matrix):
    def bfs(row, col):
        from collections import deque
        queue = deque([(row, col)])
        while queue:
            (row, col) = queue.popleft()
            if matrix[row][col] != 'O':
                continue
            # mark this cell as escaped
            matrix[row][col] = 'E'
            # check its neighbor cells
            if col < cols - 1: queue.append((row, col + 1))
            if row < rows - 1: queue.append((row + 1, col))
            if col > 0: queue.append((row, col - 1))
            if row > 0: queue.append((row - 1, col))


    if not matrix or not matrix[0]:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    from itertools import product
    border_cells = list(product(range(rows), [0, cols-1])) \
                + list(product([0, rows-1], range(cols)))

    for row, col in border_cells:
        bfs(row, col)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'O':
                matrix[r][c] = 'X'  # captured
            elif matrix[r][c] == 'E':
                matrix[r][c] = 'O'

    return matrix

matrix = [['B','B','B','B'],['W','B','W','B'],['B','W','W','B'],['B','B','B','B']]

print arr_boundary(matrix)

