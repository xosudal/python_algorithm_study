import sys
from collections import deque

N = int(input())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input())))

min_dist = [[sys.maxsize] * N for _ in range(N)]

q = deque()

q.append((0, 0))
min_dist[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if min_dist[nx][ny] > min_dist[x][y] + graph[nx][ny]:
                min_dist[nx][ny] = min_dist[x][y] + graph[nx][ny]
                q.append((nx, ny))

print(min_dist[N - 1][N - 1])
