from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y, dist):
    if x == n-1 and y == m-1:
        print("arrived")
        return

    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if graph[x][y] == 0:
        return

    if graph[x][y] == 1:
        graph[x][y] = dist + 1
        dfs(x + 1, y, graph[x][y])
        dfs(x - 1, y, graph[x][y])
        dfs(x, y + 1, graph[x][y])
        dfs(x, y - 1, graph[x][y])


dfs(0, 0, graph[0][0])

for i in range(n):
    print(graph[i])
