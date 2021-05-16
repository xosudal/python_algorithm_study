import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def dfs(py, px, y, x, cnt):
    global ans
    if x == ex and y == ey:
        ans = min(ans, cnt)
        return
    if x < 0 or x >= N or y < 0 or y >= N: return
    if visit[y][x] == 1: return
    visit[y][x] = 1

    if px == x and py == y - 1:
        if cnt < v[y][x][0]:
            v[y][x][0] = cnt
            if 1 <= graph[y][x] <= 2:
                dfs(y, x, y + 1, x, cnt + 1)
            elif graph[y][x] >= 3:
                dfs(y, x, y, x - 1, cnt + 1)
                dfs(y, x, y, x + 1, cnt + 1)

    elif px == x and py == y + 1:
        if cnt < v[y][x][1]:
            v[y][x][1] = cnt
            if 1 <= graph[y][x] <= 2:
                dfs(y, x, y - 1, x, cnt + 1)
            elif graph[y][x] >= 3:
                dfs(y, x, y, x + 1, cnt + 1)
                dfs(y, x, y, x - 1, cnt + 1)

    elif px == x + 1 and py == y:
        if cnt < v[y][x][2]:
            v[y][x][2] = cnt
            if 1 <= graph[y][x] <= 2:
                dfs(y, x, y, x - 1, cnt + 1)
            elif graph[y][x] >= 3:
                dfs(y, x, y + 1, x, cnt + 1)
                dfs(y, x, y - 1, x, cnt + 1)
    elif px == x - 1 and py == y:
        if cnt < v[y][x][3]:
            v[y][x][3] = cnt
            if 1 <= graph[y][x] <= 2:
                dfs(y, x, y, x + 1, cnt + 1)
            elif graph[y][x] >= 3:
                dfs(y, x, y + 1, x, cnt + 1)
                dfs(y, x, y - 1, x, cnt + 1)
    visit[y][x] = 0


for test_case in range(1, T + 1):
    N = int(input())
    graph = list()
    ans = 2 ** 32
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    ey, ex = 0, -1
    visit = [[0] * N for _ in range(N)]
    v = [[[2**32] * 4 for _ in range(N)] for _ in range(N)]
    dfs(N - 1, N, N - 1, N - 1, 0)

    ey, ex = N-1, N
    visit = [[0] * N for _ in range(N)]
    v = [[[2**32] * 4 for _ in range(N)] for _ in range(N)]
    dfs(0, -1, 0, 0, 0)
    print(f'#{test_case} {ans}')
