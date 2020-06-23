#search a maze to see if a path exists from entry to exit
def search_maze(maze):

    m = len(maze)
    n = len(maze[0])
    res = []
    def search_maze_helper(maze, row, col, entry, exit):
        x, y = entry[0], entry[1]

        if x < 0 or x >= row or y < 0 or y >= col or maze[x][y] == 1:
            return False

        maze[x][y] = 1
        res.append((x,y))

        if x == exit[0] and y == exit[1]:
            return True

        for coord in [(x, y+1),(x+1, y),(x-1, y),(x, y-1)]:
            if search_maze_helper(maze, m, n, coord, exit):
                return True

        del res[-1]
        return False


    search_maze_helper(maze, m, n, [0, 0], [3,3])
    return res


print search_maze()