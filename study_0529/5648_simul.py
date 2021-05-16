import sys

sys.stdin = open("input.txt", "r")

direction = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0]
]
maps = [[0] * 4001 for _ in range(4001)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list()
    for _ in range(N):
        x, y, d, e = list(map(int, input().split()))
        arr.append([x * 2 + 2000, y * 2 + 2000, d, e])
    cnt, time = 0, 0
    energy = 0
    while cnt < N:
        d1 = []
        if time > 4000:
            break
        for n in range(N):
            if arr[n][0] != -1:
                nx, ny = arr[n][0] + direction[arr[n][2]][0], arr[n][1] + direction[arr[n][2]][1]
                a = maps[arr[n][0]][arr[n][1]]
                if a != 0:
                    print(a)
                if 0 <= nx <= 4000 and 0 <= ny <= 4000:
                    maps[nx][ny] += 1
                    arr[n][0], arr[n][1] = nx, ny
                    d1.append([nx, ny])
                else:
                    cnt += 1
                    arr[n][0], arr[n][1] = -1, -1

        for n in range(N):
            x, y = arr[n][0], arr[n][1]
            if x != -1:
                if maps[x][y] > 1:
                    cnt += 1
                    energy += arr[n][3]
                    arr[n][0], arr[n][1] = -1, -1

        for n in range(N):
            a, b = arr[n][0], arr[n][1]
            if a != -1:
                maps[a][b] = 0

        for a, b in d1:
            maps[a][b] = 0

        time += 1
    print(f'#{tc} {energy}')
