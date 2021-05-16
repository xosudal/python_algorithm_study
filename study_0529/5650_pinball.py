import sys

sys.stdin = open("input.txt", "r")

# 0: 위 1: 아래 2: 좌 3: 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direction = [
    [0, 0, 0, 0],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]


def dfs(x, y, d):
    start, end = x, y
    nx, ny = x, y
    cnt = 0
    while True:
        nx, ny = nx + dx[d], ny + dy[d]
        if (nx == start and ny == end) or ball_map[nx][ny] == -1: return cnt
        if ball_map[nx][ny] == 0: continue
        if 1 <= ball_map[nx][ny] <= 5:
            d = direction[ball_map[nx][ny]][d]
            cnt += 1
        elif ball_map[nx][ny] >= 6:
            h_idx = ball_map[nx][ny] - 6
            if hall[h_idx][0][0] == nx and hall[h_idx][0][1] == ny:
                nx, ny = hall[h_idx][1]
            else:
                nx, ny = hall[h_idx][0]


for tc in range(1, int(input()) + 1):
    N = int(input())
    ball_map = [[5] * (N + 2) for _ in range(N + 2)]
    hall = [[] * 2 for _ in range(5)]
    for i in range(1, N + 1):
        temp = list(map(int, input().rstrip().split()))
        for j in range(N):
            ball_map[i][j + 1] = temp[j]
            if temp[j] >= 6:
                hall[temp[j] - 6].append([i, j + 1])
    ans = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if ball_map[i][j] == 0:
                for d in range(4):
                    ans = max(ans, dfs(i, j, d))

    print(f'#{tc} {ans}')
