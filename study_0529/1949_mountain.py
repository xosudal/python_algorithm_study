import sys
sys.stdin = open("input.txt", "r")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, change, cnt):
    global ans
    ans = max(ans, cnt)
    visit[x][y] = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visit[nx][ny] == 1: continue
        if maps[nx][ny] < maps[x][y]:
            dfs(nx, ny, change, cnt+1)
        elif not change and (maps[nx][ny] - maps[x][y] < K):
            temp = maps[nx][ny]
            maps[nx][ny] = maps[x][y] - 1
            dfs(nx, ny, True, cnt+1)
            maps[nx][ny] = temp
    visit[x][y] = 0


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    temp_max = -1
    for a in maps:
        for b in a:
            temp_max = max(temp_max, b)
    start = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == temp_max:
                start.append([i, j])
    ans = -1
    visit = [[0]*N for _ in range(N)]
    for s, e in start:
        dfs(s, e, False, 1)
    print(f'#{tc} {ans}')