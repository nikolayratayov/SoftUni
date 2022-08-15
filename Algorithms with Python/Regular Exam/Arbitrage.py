def dfs(node, graph, visited, visited_money, money, best_false_res):
    global has_cycle
    if node in visited and node == start:
        visited_money.append(money)
        res = 1
        for i in visited_money:
            res *= i
        if res > 1:
            has_cycle = False
            print(True)
            visited.append(start)
            print(' '.join(visited))
            visited.pop()
            return
        visited.pop()
        visited_money.pop()
        visited_money.pop()
        return
    visited.append(node)
    visited_money.append(money)
    res_for_now = 1
    for j in visited_money:
        res_for_now *= j
    if res_for_now > best_false_res[node]:
        best_false_res[node] = res_for_now
    for child in graph[node]:
        dfs(child[0], graph, visited, visited_money, child[1], best_false_res)


has_cycle = True
pairs = int(input())
graph = {}
for _ in range(pairs):
    line = input().split()
    source = line[0]
    dest = line[1]
    price = float(line[2])
    if source not in graph:
        graph[source] = []
    graph[source].append([dest, price])

best_false_res = {}
for eee in graph:
    best_false_res[eee] = 0
start = input()
best_false_res[start] = 1
visited = []
visited_money = []
dfs(start, graph, visited, visited_money, 1, best_false_res)

if has_cycle:
    print(False)
    for k, v in best_false_res.items():
        print(f'{k}: {v:.3f}')
