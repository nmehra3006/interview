# Representing graph as a matrix and traversing in dfs and bfs
# search if path exists from start to end in a maze
"""
start = (0, 0), end = (3,3)
maze = [['E', 'E', 'E', 'E'],
['E','W', 'W','E'],
['E','E', 'E','E'],
['E','E', 'W','E'],
]
"""
# 1. Find a path from src to end, both dfs and bfs can be used as search
# 2. If path exists return the path
# 3. shortest path
import copy

class MazeRunner(object):

    def __init__(self):

        self.dirs = [(-1, 0), (1,0), (0, -1), (0, 1)]

    def find_path_util(self, maze, row, col, end, paths, res):

        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and (row, col) not in paths and maze[row][col] == 'E':

            paths.append((row, col))

            if (row, col) == end:
                final_path = copy.deepcopy(paths)
                res.append(final_path) # deep copy

            else:
                for dir in self.dirs:
                    self.find_path_util(maze, row+dir[0], col+dir[1], end, paths, res)
            paths.pop()


    def find_if_path(self, maze, start, end):

        if maze[start[0]][start[1]] == 'W' or maze[end[0]][end[1]] == 'W':
            return False

        visited = set()

        if start == end:
            return True

        if find_path_util(self, maze, start[0], start[1], end, visited):
            return True

        return False

    def find_all_path(self, maze, start, end):

        if maze[start[0]][start[1]] == 'W' or maze[end[0]][end[1]] == 'W':
            return []

        res = []

        if start == end:
            res.append(start)
            return res

        self.find_path_util(maze, start[0], start[1], end, [], res)
        return res

# print find_if_path([['E', 'E', 'E', 'E'],
# ['E','W', 'W','W'],
# ['E','E', 'E','W'],
# ['E','E', 'E','E'],
# ], (0,0), (3,3))

runner = MazeRunner()
all_paths = runner.find_all_path([['E', 'E', 'E', 'E'],
['E','W', 'W','E'],
['E','E', 'E','E'],
['E','E', 'W','E'],
], (0,0), (3,3))

for path in all_paths:
    print path