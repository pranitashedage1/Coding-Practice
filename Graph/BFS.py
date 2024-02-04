from collections import defaultdict
class graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printgraph(self):
        print(self.graph)

    def BFS(self, s):
        visited = [False] * (max(self.graph)+1)
        q = []
        q.append(s)
        visited[s] = True

        while q:
            vertex = q.pop(0)
            print(vertex, end=' ')
            for i in self.graph[vertex]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.printgraph()
    g.BFS(0)
    print()
    g.BFS(2)
