from collections import deque


class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight



nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, dest, weight = [int(x) for x in input().split(' ')]
    graph.append(Edge(source, dest, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.dest]:
            distance[edge.dest] = new_distance
            parent[edge.dest] = edge.source
            updated = True
    if not updated:
        break
for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.dest]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
    print(distance[target])
