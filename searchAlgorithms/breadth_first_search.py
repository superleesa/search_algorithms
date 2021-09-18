from neigh import neigh
from collections import deque # deque is useful to manage data structures, in this case, queue

def breadth_first_traversal(graph, s):
    boundaries = deque([s]) # candidates for next path
    visited = []

    while len(boundaries) > 0:
        v = boundaries.popleft()
        visited.append(v)
        for w in neigh(v, graph):
            if w not in visited and w not in boundaries:
                boundaries.append(w)

    return visited