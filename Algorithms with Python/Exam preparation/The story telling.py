# from collections import OrderedDict
#
#
# def find_node_without_dependencies(dependencies_by_node):
#     for node, dependencies in dependencies_by_node.items():
#         if dependencies == 0:
#             return node
#     return None
#
#
# def find_dependencies(graph):
#     result = {}
#     for node, children in graph.items():
#         if node not in result:
#             result[node] = 0
#         for child in children:
#             if child not in result:
#                 result[child] = 1
#             else:
#                 result[child] += 1
#     return result
#
#
# graph = {}
# while True:
#     a = input()
#     if a == 'End':
#         break
#     vhod = a.split('->')
#     node = vhod[0].strip()
#     child = vhod[1].strip().split() if vhod[1] else []
#     graph[node] = child
#
# dependencies_by_node = find_dependencies(graph)
# sorted_nodes = []
# dependencies_by_node = OrderedDict(reversed(list(dependencies_by_node.items())))
# while dependencies_by_node:
#     node_to_remove = find_node_without_dependencies(dependencies_by_node)
#     dependencies_by_node.pop(node_to_remove)
#     sorted_nodes.append(node_to_remove)
#     for child in graph[node_to_remove]:
#         dependencies_by_node[child] -= 1
#
# print(' '.join(sorted_nodes))



def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)
    result.append(node)


graph = {}
while True:
    a = input()
    if a == 'End':
        break
    vhod = a.split('->')
    node = vhod[0].strip()
    child = vhod[1].strip().split() if vhod[1] else []
    graph[node] = child

visited = set()
result = []
for node in graph:
    dfs(node, graph, visited, result)

print(' '.join(reversed(result)))
