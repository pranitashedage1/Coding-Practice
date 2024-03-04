# Topological sorting - Kahn's Algorithm
# A python program to print the topological order using indegrees 

from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.V = vertices # no. of vertices

    # Creating a edges between the vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # printing the graph
    def printGraph(self):
        for i, j in self.graph:
            print(i, j)
    
    def topologicalSort(self):
        # Create a vector to store indegrees of all
        # For all vertices, initialize all vertices to zero
        in_degree = [0]*(self.V)

        # Traverse adjacency lists to fill indegrees of all vertices
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        
        # Create a queue and enque all vertices in the queue which has 0 indegree
        q = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                q.append(i)

        cnt = 0
        topo_order = []        
        while q:
            # popping the left most element and decrease the indegree of the vertices
            u = q.popleft()
            topo_order.append(u)
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
            cnt += 1
            
        # Check if there was a cycle - 
        if cnt != self.V:
            print("There exist a cycle in the graph")
        else:
            print("Topological Order", topo_order)


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topologicalSort()
    
