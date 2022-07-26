from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight


edges = int(input())
graph = {}
for _ in range(edges):
    source, dest, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if dest not in graph:
        graph[dest] = []
    graph[source].append(Edge(source, dest, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break
    for edge in graph[node]:
        new_dist = min_distance + edge.weight
        if new_dist < distance[edge.dest]:
            distance[edge.dest] = new_dist
            parent[edge.dest] = node
            pq.put((new_dist, edge.dest))

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
