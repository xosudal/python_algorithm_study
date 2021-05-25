import sys

sys.stdin = open("input.txt", "r")

'''
def allVisit(v):
    if (1 << N) - 1 == v:
        return True
    else:
        return False
 
 
def dfs(start, visited, dist):
    global ans
 
    if allVisit(visited):
        ans = min(ans, dist + D[start][N])
        return
 
    for i in range(N):
        if visited & (1 << i) == 0 and D[start][i] != 0:
            dfs(i, visited | (1 << i), dist + D[start][i])
'''


def dfs(last, visited):

    if visited == (1 << N)-1:
        return D[last][N]

    if dp[last][visited] != 0:
        return dp[last][visited]

    temp = 2**43

    for i in range(N):
        if visited & (1 << i) == 0 and D[last][i] != 0:
            temp = min(temp, dfs(i, visited | (1 << i)) + D[last][i])
            dp[last][visited] = temp
    return temp

for tc in range(1, int(input()) + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    company = temp[:2]  # N
    home = temp[2:4]  # N+1
    client = [[temp[i], temp[i + 1]] for i in range(4, len(temp) - 1, 2)]
    D = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            if i != j:
                temp = abs(client[i][0] - client[j][0]) + abs(client[i][1] - client[j][1])
                D[i][j] = temp
                D[j][i] = temp
    for i in range(N):
        c = abs(company[0] - client[i][0]) + abs(company[1] - client[i][1])
        h = abs(home[0] - client[i][0]) + abs(home[1] - client[i][1])
        D[N][i] = c
        D[i][N] = c
        D[N + 1][i] = h
        D[i][N + 1] = h
    ans = 2 ** 43
    dp = [[0] * (1<<N) for _ in range(N)]
    for i in range(N):
        ans = min(ans, (dfs(i, 1 << i) + D[N+1][i]))

    print(f'#{tc} {ans}')
