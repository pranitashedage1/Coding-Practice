# Adding edge
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Printing graph
def printing_graph(adj, V):
    for i in range(0, V):
        print(i, '-> ', end = ' ')
        for i in  adj[i]:
            print(i, end= ', ')
        print()

# Graph Initialization
def graph_init(V, edges, noOfEdges):
    adj = []
    for _ in range(V):
        adj.append([])
    for i in range(0, noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])
    printing_graph(adj, V)
    print(adj)

if __name__ == '__main__':
    v = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    noOfEdges = 3
    graph_init(v, edges, noOfEdges)
