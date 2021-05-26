import sys
sys.stdin = open("input.txt", "r")

def bfs(start):
    q = [start]
    visit[start] = 1
    while q:
        t = q.pop(0)
        for i in adj[t]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
                dist[i] = dist[t] + 1


for tc in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    adj = dict()
    for i in range(N):
        T = temp[N*i+1:N*(i+1)+1]
        adj[i] = []
        for j in range(len(T)):
            if T[j] == 1:
                adj[i].append(j)
    ans = 2**43

    for i in range(N):
        dist = [0] * N
        visit = [0] * N
        bfs(i)
        ans = min(ans, sum(dist))

    print(f'#{tc} {ans}')
