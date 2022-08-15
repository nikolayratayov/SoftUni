def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)

all_nodes = set()
nodes = int(input())
edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes + 1)]
for _ in range(edges):
    source, dest = [int(x) for x in input().split()]
    all_nodes.add(source)
    all_nodes.add(dest)
    graph[source].append(dest)
start = int(input())
visited = set()

dfs(start, graph, visited)
result = []
for i in all_nodes:
    if i not in visited:
        result.append(i)
if len(result) == 0:
    pass
else:
    print(*sorted(result), sep=' ')