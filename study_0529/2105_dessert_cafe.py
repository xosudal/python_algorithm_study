import sys

sys.stdin = open("input.txt", "r")

direction = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1]
]

dx=[1,-1,-1,1]
dy=[1,1,-1,-1]

def dfs(x, y, t, c):
    global ans
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if t > 3:
        return
    if x == s and y == e and t == 3:
        ans = max(ans, c)
        return

    if dessert[maps[x][y]]:
        return
    dessert[maps[x][y]] = 1

    nx = x + direction[t][0]
    ny = y + direction[t][1]
    print(direction[t][0], dx[t])

    dfs(nx, ny, t, c + 1)
    dfs(nx, ny, t + 1, c + 1)
    dessert[maps[x][y]] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    dessert = [0] * 101
    ans = -1
    for i in range(N):
        for j in range(N):
            s, e = i, j
            dfs(i, j, 0, 0)
    print(f'#{tc} {ans}')
