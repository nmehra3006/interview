
#implement directed and undirected graph using adjacency lists
from collections import defaultdict
from collections import deque
from enum import Enum


class Order(Enum):
    DFS = 0
    BFS = 1


class DirectedGraph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        self.graph[u].append(v)
        # for undirected graph add
        self.graph[v].append(u)

    def traverse(self, order, vertex):

        path = []
        visited = set()
        if order == Order.DFS.value:
            self._dfs(vertex, visited, path)

        elif order == Order.BFS.value:
            self._bfs(vertex, visited, path)

        return path

    def _dfs(self, v, visited, path):
       path.append(v)
       visited.add(v)

       for next_v in self.graph[v]:
            if next_v not in visited:
                self._dfs(next_v, visited, path)


    def _bfs(self, v, visited, path):

        q = deque([v])

        while q:
            next_v = q.popleft()
            path.append(next_v)
            visited.add(next_v)

            for neighbor in self.graph[next_v]:
                if neighbor not in visited:
                    q.append(neighbor)


    def _detect_cycle_helper(self, v, visited, parent):

        visited.add(v)
        print v, parent
        for next_v in self.graph[v]:

            if next_v not in visited:
                self._detect_cycle_helper(next_v, visited, v)

            elif parent != next_v:
                return True

        return False

    #detect cycle using dfs
    def detect_cycle(self):
        visited = set()

        for v in self.graph.keys():
            if v not in visited:
                if self._detect_cycle_helper(v, visited, -1):
                    return True

        return False


dg = DirectedGraph()
edges = [(1, 2), (2, 4), (1, 3), (3, 4), (3, 5)]
for u, v in edges:
    dg.add_edge(u,v)

# print dg.traverse(0, 1)
# print dg.traverse(1, 1)
print dg.detect_cycle()

