import sys
sys.stdin = open("input.txt", "r")
from collections import deque


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

backward = [1, 0, 3, 2]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    cnt = 0
    q = deque()
    time = 1
    q.append([R, C, time])

    while q:
        x, y, t = q.popleft()

        if t == L+1:
            break
        visit[x][y] = 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visit[nx][ny] == 1 or maps[nx][ny] == 0: continue
            if pipe[maps[x][y]][d] == 1 and pipe[maps[nx][ny]][backward[d]] == 1:
                q.append([nx, ny, t+1])

    for i in visit:
        for j in i:
            if j == 1:
                cnt += 1
    print(f'#{tc} {cnt}')