# depth first search
from neigh import neigh
from collections import deque # deque is useful to manage data structures, in this case, stack
from math import inf

# function to only traverse a graph
def depth_first_traversal(graph, s):
    boundaries = deque([s]) # candidates for next path
    visited = []

    while len(boundaries) > 0:
        v = boundaries.pop()
        visited.append(v)
        for w in neigh(v, graph):
            if w not in visited and w not in boundaries:
                boundaries.append(w)

    return visited

# function to traverse and get the distance of each node
# this function keeps control of distances of visited vertices using "distance" list.
# distance list works as follow: [distance of node 0, distance of node 2, distance of node 3, ... and so on]
def depth_first_distance(graph, s):
    distance = [inf]*len(graph)
    distance[s] = 0
    boundaries = deque([s]) # candidates for next path
    visited = []

    while len(boundaries) > 0:
        v = boundaries.pop()
        visited.append(v)
        for w in neigh(v, graph):
            if w not in visited and w not in boundaries:
                boundaries.append(w)
                distance[w] = distance[v] + 1

    return visited, distance