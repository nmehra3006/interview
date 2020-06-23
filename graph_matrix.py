# graph implementation using adjacency matrix
class Graph(object):
    def __init__(self, no_of_vertices):
        self.matrix = [[-1] * no_of_vertices for _ in range(no_of_vertices)]
        self.vertices = {}
        self.no_vertices = no_of_vertices
        self.vertice_list = [0] * no_of_vertices

    def set_vertices(self, v, id):
        if 0 <= v <= self.no_vertices:
            self.vertices[id] = v
            self.vertice_list[v] = id

    def get_vertices(self):
        return self.vertice_list

    def set_edges(self, frm, to, cost):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.matrix[frm][to] = cost
        # for directed graph do not add this
        self.matrix[to][frm] = cost

    def get_edges(self):
        edges = []
        for i in range(self.no_vertices):
            for j in range(self.no_vertices):
                if self.matrix[i][j] != -1:
                    edges.append((self.vertice_list[i], self.vertice_list[j], self.matrix[i][j]))
        return edges

    def get_matrix(self):
        return self.matrix

G =Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)

print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())