def neigh(v, graph):
    neighbors = []
    for i in range(len(graph)):
        if graph[v][i]:
            neighbors.append(i)
    return neighbors