# searches through a graph (not a tree in this case, but also works with trees)
from neigh import neigh
from depth_first_search import depth_first_traversal, depth_first_distance
from breadth_first_search import breadth_first_traversal

graph = \
[
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
]

print(neigh(1, graph))

print(depth_first_distance(graph,0))
print(breadth_first_traversal(graph,0))