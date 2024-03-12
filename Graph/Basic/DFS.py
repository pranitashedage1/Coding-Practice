'''
Applications of DFS - 
    i) Cycle Detection
    ii) Topological Order - specifically useful for dependency graphs
    iii) Strongly connected components - Kosoraju's Algoritm and Tarjan's Algorithm
    iv) Solving puzzles like Maze - DFS is always preferred to solve maze as compared to the BFS
    v) Path Finding 
'''
# Time complexity - O(V + E)
from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for i in self.graph[v]:
            if i not in visited:
                self.dfsUtil(i, visited)

    def DFS(self, v):
        visited = set()
        self.dfsUtil(v, visited)
        

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(1, 4)
g.addEdge(3, 4)
g.DFS(0)
