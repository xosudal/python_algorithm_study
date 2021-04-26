import sys
sys.stdin = open("input.txt", "r")

T = 10

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    #print(x, y)
    graph[x][y] = 5

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 16 or ny >= 16: continue
        if graph[nx][ny] == 0:
            dfs(nx, ny)

        elif graph[nx][ny] == 3:
            global ans
            ans = 1
            return


for test_case in range(1, T + 1):
    tc = int(input())
    ans = 0
    graph = list()
    for _ in range(16):
        graph.append(list(map(int, input())))
    start_x = 0
    start_y = 0
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start_x = i
                start_y = j
    dfs(start_y, start_x)
    print("#" + str(test_case) + " ", end='')
    print(ans)
