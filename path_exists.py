from collections import namedtuple

Coordinate = namedtuple('Coordinates', ('x', 'y'))
def check_if_path_exists(grid, src, dest, visited, path):

    if not (0 <= src.x < len(grid) and 0 <= src.y < len(grid[0]) and grid[src.x][src.y] == 1):
        return False

    path.append(src)
    visited[src.x][src.y] = True

    if src == dest:
        return True

    if any(
        map(
            check_if_path_exists,
            
            map(Coordinate, (src.x - 1, src.x+1, src.x, src.x), (src.y, src.y, src.y-1, src.y+1))
        )
    ):
        return True

    del path[-1]
    return False

if __name__ == "__main__":
    grid = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
           [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
           [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
           [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
           [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
    src = Coordinate(0, 0)
    dest = Coordinate(3, 4)
    path = []
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    check_if_path_exists(grid, src, dest, visited, path)