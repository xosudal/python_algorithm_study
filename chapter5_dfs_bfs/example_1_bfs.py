from collections import deque

n, m = map(int, input().split())

mapArr = []
for i in range(n):
    mapArr.append(list(map(int, input())))

cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * m for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        q = queue.popleft()
        for d in range(4):
            nx = q[0] + dx[d]
            ny = q[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if mapArr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if mapArr[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)
