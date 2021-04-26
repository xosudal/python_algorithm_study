import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = 10

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 5

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100: continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 5
                q.append((nx, ny))
            elif graph[nx][ny] == 3:
                global ans
                ans = 1
                return


for test_case in range(1, T + 1):
    tc = int(input())
    ans = 0
    graph = list()
    for _ in range(100):
        graph.append(list(map(int, input())))
    start_x = 0
    start_y = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] == 2:
                start_x = i
                start_y = j
    bfs(start_y, start_x)
    print("#" + str(test_case) + " ", end='')
    print(ans)
