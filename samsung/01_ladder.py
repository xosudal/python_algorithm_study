T = 10
dx = [0, 0, -1]
dy = [-1, 1, 0]


def dfs(x, y, _map):
    _map[x][y] = 0

    if x == 0:
        global Y
        Y = y
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 100 or ny < 0 or ny >= 100: continue
        if _map[nx][ny] == 1:
            return dfs(nx, ny, _map)


for test_case in range(1, T + 1):
    tc = int(input())
    graph = list()
    for _ in range(100):
        graph.append(list(map(int, input().split())))

    X = 99
    Y = -1
    for i in range(100):
        if graph[99][i] == 2:
            Y = i
    dfs(X, Y, graph)
    print("#" + str(tc) + " ", end='')
    print(Y)
