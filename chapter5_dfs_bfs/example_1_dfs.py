n, m = map(int, input().split())

mapArr = []
for i in range(n):
    mapArr.append(list(map(int, input())))

cnt = 0


def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if mapArr[x][y] == 0:
        mapArr[x][y] = 1
        cnt += 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)


for i in range(n):
    for j in range(m):
        if mapArr[i][j] == 0:
            dfs(i, j)

print(cnt)
