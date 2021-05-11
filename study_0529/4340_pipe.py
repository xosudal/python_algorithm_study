import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def dfs(px, py, x, y, cnt):
    global ans
    if x == ex and y == ey:
        ans = min(ans, cnt)
        return
    if x < 0 or x >= N or y < 0 or y >= N: return
    if visit[x][y] == 1: return
    visit[x][y] = 1
    if px == x and py == y - 1:
        if 1 <= graph[x][y] <= 2:
            dfs(x, y, x, y + 1, cnt + 1)
        elif graph[x][y] >= 3:
            dfs(x, y, x + 1, y, cnt + 1)
            dfs(x, y, x - 1, y, cnt + 1)

    elif px == x and py == y + 1:
        if 1 <= graph[x][y] <= 2:
            dfs(x, y, x, y - 1, cnt + 1)
        elif graph[x][y] >= 3:
            dfs(x, y, x + 1, y, cnt + 1)
            dfs(x, y, x - 1, y, cnt + 1)

    elif px == x + 1 and py == y:
        if 1 <= graph[x][y] <= 2:
            dfs(x, y, x - 1, y, cnt + 1)
        elif graph[x][y] >= 3:
            dfs(x, y, x, y + 1, cnt + 1)
            dfs(x, y, x, y - 1, cnt + 1)
    elif px == x - 1 and py == y:
        if 1 <= graph[x][y] <= 2:
            dfs(x, y, x + 1, y, cnt + 1)
        elif graph[x][y] >= 3:
            dfs(x, y, x, y + 1, cnt + 1)
            dfs(x, y, x, y - 1, cnt + 1)
    visit[x][y] = 0


for test_case in range(1, T + 1):
    N = int(input())
    graph = list()
    ans = 2 ** 32
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    ex, ey = 0, -1
    visit = [[0] * N for _ in range(N)]
    dfs(N - 1, N, N - 1, N - 1, 0)

    # ex, ey = N-1, N
    # visit = [[0] * N for _ in range(N)]
    # dfs(0, -1, 0, 0, 0)
    print(f'#{test_case} {ans}')
