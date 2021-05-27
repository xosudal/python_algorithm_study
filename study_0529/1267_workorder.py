import copy
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    V, E = map(int, input().split())
    _input = list(map(int, input().split()))
    adj = [[0] * (V+1) for _ in range(V+1)]
    work = [0] * (V+1)
    for e in range(E):
        adj[_input[2*e]][_input[2*e+1]] = 1
        work[_input[2*e+1]] += 1
    ans = []
    q = []
    for start in range(1, V+1):
        if work[start] == 0:
            q.append(start)

    while q:
        temp = q.pop(0)
        ans.append(temp)

        for i in range(1, V+1):
            if adj[temp][i] == 1:
                work[i] -= 1
                if work[i] == 0:
                    q.append(i)

    print(f'#{tc}', *ans)