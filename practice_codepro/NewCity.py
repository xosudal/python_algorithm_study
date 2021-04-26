# 위 아래 좌 우
pipe = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 1, 1],
    '2': [1, 1, 0, 0],
    '3': [0, 1, 0, 1],
    '4': [0, 1, 1, 0],
    '5': [1, 0, 1, 0],
    '6': [1, 0, 0, 1],
    '7': [1, 1, 0, 1],
    '8': [0, 1, 1, 1],
    '9': [1, 1, 1, 0],
    'A': [1, 0, 1, 1],
    'B': [1, 1, 1, 1]
}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 아래 위 우 좌
backward = [1, 0, 3, 2]
N = int(input())
a, b = map(int, input().split())

graph = list()

visit = [[0] * N for _ in range(N)]

total = N * N

for _ in range(N):
    temp = list(map(str, input()))
    graph.append(temp)
    total -= temp.count('0')

cnt = 0
def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visit[nx][ny] == 1: continue
        if pipe[graph[x][y]][i] == 1 and pipe[graph[nx][ny]][backward[i]] == 1:
            dfs(nx, ny)


dfs(b, a)  # holy shit not a b !!

print(total - cnt)
