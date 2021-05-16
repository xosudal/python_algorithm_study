import copy
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_start(w):
    h = 0
    while h < H:
        if arr[h][w] > 0:
            break
        h += 1
    return h


def rearrange():
    global arr
    for w in range(W):
        start, end = H-1, H-1
        while start >= 0:
            if arr[start][w]:
                arr[start][w], arr[end][w] = 0, arr[start][w]
                start -= 1
                end -= 1
            else:
                start -= 1


def remove_marble(h, w):
    r = arr[h][w]
    arr[h][w] = 0
    ret = 1
    for i in range(4):
        nh, nw = h, w
        for j in range(r):
            if 0 <= nh < H and 0 <= nw < W:
                if arr[nh][nw]:
                    ret += remove_marble(nh, nw)
                nh += dx[i]
                nw += dy[i]
    return ret

def dfs(cnt):
    global arr
    if cnt == N: return 0
    temp = copy.deepcopy(arr)
    ans = 0
    for w in range(W):
        h = find_start(w)
        if h == H:
            continue
        ret = remove_marble(h, w)
        rearrange()
        ans = max(ans, dfs(cnt+1) + ret)
        arr = copy.deepcopy(temp)
    return ans


for tc in range(1, T + 1):
    N, W, H = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(H)]
    total = 0
    for i in arr:
        for j in i:
            if j > 0: total += 1

    print(f'#{tc} {total-dfs(0)}')
