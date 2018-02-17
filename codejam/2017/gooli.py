from collections import deque
import sys

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def minDistance(v, dist, sptSet):
    minimum_d = sys.maxint
    min_index = -1
    for vertex in range(v):
        if dist[vertex] < minimum_d and sptSet[vertex] == False:
            minimum_d = dist[vertex]
            min_index = vertex
    return min_index

def dijkstra(g, v, source):
    sptSet = [False] * v
    distances = [sys.maxint] * v
    distances[source] = 0

    for vertex in range(v):
        u = minDistance(v, distances, sptSet)
        vert_u = g.getVertex(u)
        sptSet[u] = True
        print(vert_u)
        for vertex in range(v):
            try:
                vert_v = g.getVertex(vertex)
                uvw = vert_u.getWeight(vert_v)
            except:
                print ("no edge between {} and {}".format(source, vertex))
                continue
            if uvw > 0 and sptSet[vertex] == False and distances[vertex] > distances[u] + uvw:
                distances[vertex] = distances[u] + uvw

    longest_path = max(distances)

    return longest_path


def gooli(v, edges):
    g = Graph()
    best_distance = 0.0
    for i in range(v):
        g.addVertex(i)

    for index, edge_list in enumerate(edges):
        for jindex, weight in enumerate(edge_list):
            if weight == -1:
                continue
            else:
                g.addEdge(index + 1, jindex, weight)

    for vx in g:
        for n in vx.getConnections():
            print("( %s , %s, %s )" % (vx.getId(), n.getId(), vx.getWeight(n)))

    unused_vertices = g.getVertices()
    # print(unused_vertices)
    visited = set()
    first = unused_vertices.pop()
    q = deque([first])
    # print(q)
    bfs = []
    while len(q) > 0:
        vi = q.popleft()
        # print(vi)
        vertex = g.getVertex(vi)
        # print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            neighbors = vertex.getConnections()
            for n in neighbors:
                q.append(n.getId())
            bfs.append(vi)
            # print(bfs)

    end = bfs.pop()
    # visited = set()
    # q = deque([end])
    # nq = deque()
    diameter = dijkstra(g, v, end)

    # while len(q) > 0:
    #     nq = deque()
    #     while len(q) > 0:
    #         vi = q.popleft()
    #         vertex = g.getVertex(vi)
    #         # print(vertex)
    #         if vertex not in visited:
    #             visited.add(vertex)
    #             neighbors = vertex.getConnections()
    #             for n in neighbors:
    #                 nq.append(n.getId())
    #     q = nq
    #     diameter += 1

    best_distance = diameter / 2


    return best_distance


def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        B = int(raw_input())
        adj = []
        for x in range(B - 1):
            adj.append([int(s) for s in raw_input().split()])
        result = gooli(B, adj)
        print("Case #{}: {}".format(i, result))

driver()
