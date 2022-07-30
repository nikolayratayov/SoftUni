from collections import deque


nodes = int(input())
pairs = int(input())
graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(':')
    children = [int(x) for x in children_str.split(' ')] if children_str else []
    node = int(node_str)
    graph[node] = children

for _ in range(pairs):
    source, dest = [int(x) for x in input().split('-')]
    queue = deque([source])
    visited = [False] * (max(graph) + 1)
    visited[source] = True
    parent = [None] * (max(graph) + 1)
    while queue:
        node = queue.popleft()
        if node == dest:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            queue.append(child)
            visited[child] = True
            parent[child] = node
    path = deque()
    node = dest
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    if len(path) == 1:
        print(f'{{{source}, {dest}}} -> -1')
    else:
        print(f'{{{source}, {dest}}} -> {len(path) - 1}')
