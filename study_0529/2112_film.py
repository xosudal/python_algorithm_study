import sys
sys.stdin = open("input.txt", "r")

import copy
visit = [0] * 13
def check_film():
    flag = True
    for w in range(W):
        cnt = 1
        for d in range(D-1):
            if maps[d][w] == maps[d+1][w]:
                cnt += 1
            else:
                cnt = 1
                flag = False
            if cnt >= K:
                flag = True
                break
        if not flag:
            return flag
    return flag


def dfs(s, c):
    global min_cnt

    if c >= min_cnt:
        return
    if check_film():
        min_cnt = min(min_cnt, c)
        return
    for i in range(s, D):
        for j in ab:
            if visit[i] == 1: continue
            visit[i] = 1
            maps[i] = j
            dfs(i, c+1)
            maps[i] = backup[i]
            visit[i] = 0


for tc in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(D)]
    backup = copy.deepcopy(maps)
    ab = [[0]*W, [1]*W]
    min_cnt = K
    if K > 1:
        dfs(0, 0)
    else:
        ans = 0
    print(f'#{tc} {min_cnt}')