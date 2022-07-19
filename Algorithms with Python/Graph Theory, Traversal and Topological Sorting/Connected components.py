def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


n = int(input())
graph = []

for i in range(n):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split(' ')]
    graph.append(children)

visited = [False] * n

for node in range(n):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join(str(x) for x in component)}")
