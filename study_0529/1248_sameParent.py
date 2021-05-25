import sys
sys.stdin = open("input.txt", "r")


def calDepth(x, d):
    visit[x] = 1
    depth[x] = d

    for i in range(V+1):
        if visit[i] == 1:
            continue
        if x == parent[i]:
            calDepth(i, d+1)


def findParent(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

def subTreeNum(id):
    global cnt
    for i in range(V+1):
        if parent[i] == id:
            cnt += 1
            subTreeNum(i)


for tc in range(1, int(input()) + 1):
    V, E, A, B = map(int, input().split())
    T = []
    temp = list(map(int, input().split()))
    parent = [0] * (V+1)
    depth = [0] * (V+1)
    graph = [0] * (V+1)
    visit = [0] * (V+1)
    for i in range(0, len(temp)-1, 2):
        p, c = temp[i], temp[i+1]
        parent[c] = p
    calDepth(1, 0)
    idx = findParent(A, B)
    cnt = 1
    subTreeNum(idx)
    print(f'#{tc} {idx} {cnt}')
