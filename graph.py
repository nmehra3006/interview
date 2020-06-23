global graph
global vertices

def addVertex(v):
    global graph
    global vertices
    if v in graph:
        print "already exists!"
    else:
        vertices += 1
        graph[v] = []


def addEdge(v1, v2, e):

    global graph

    if v1 not in graph:
        print v1 + "not in graph"

    elif v2 not in graph:
        print v2 + "not in graph"

    else:
        temp = [v2, e]
        graph[v1].append(temp)


def printGraph():
    global graph






