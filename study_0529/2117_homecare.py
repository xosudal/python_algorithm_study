import sys

sys.stdin = open("input.txt", "r")


def cal(x, y):
    r = 0
    for k in range(1, 22):
        cnt = 0
        oper = k * k + (k - 1) * (k - 1)
        for h in home:
            d = abs(h[0] - x) + abs(h[1] - y)
            if d <= k-1:
                cnt += 1
        res = M * cnt - oper
        if res >= 0:
            r = cnt
    return r


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    home = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                home.append([i, j])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, cal(i, j))
    print(f'#{tc} {ans}')
