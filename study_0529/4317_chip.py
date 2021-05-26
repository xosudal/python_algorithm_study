import sys

sys.stdin = open("input.txt", "r")


def dfs(x, y, cnt, idx):
    global ans
    ans = max(ans, cnt)
    if y >= W-1:
        return
    if x >= H-1:
        print(x, y, idx)
        if dp[idx][y] >= cnt:
            return
        else:
            dp[idx][y] = cnt
        dfs(0, y + 1, cnt, 0)
        return
    if maps[x][y] == 0 and maps[x][y + 1] == 0 \
            and maps[x + 1][y] == 0 and maps[x + 1][y + 1] == 0:
        maps[x][y] = maps[x + 1][y] = maps[x][y + 1] = maps[x + 1][y + 1] = 1
        dfs(x+2, y, cnt+1, (idx | 1 << x))
        maps[x][y] = maps[x+1][y] = maps[x][y+1] = maps[x+1][y+1] = 0
    dfs(x+1, y, cnt, idx)


for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    dp = [[-1] * W for _ in range(1 << H)]
    dfs(0, 0, 0, 0)
    for d in dp:
        print(d)

    print(f'#{tc} {ans}')
