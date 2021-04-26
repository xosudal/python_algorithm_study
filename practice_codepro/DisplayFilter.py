from itertools import combinations
from itertools import permutations

import sys
N = int(input())

C = list()

R = [0] * N
P = [0] * N

for i in range(N):
    C.append(i)
    R[i], P[i] = map(int, input().split())

cnt = 0
diff = sys.maxsize

visit = [[False] * N for _ in range(N)]

def comb_func(start, r):
    if r == 0:
        temp = list()
        for i in range(N):
            if visit[i] is False:
                temp.append(i)
        comb.append(temp)
    else:
        for i in range(start, N):
            visit[i] = True
            comb_func(i+1, r-1)
            visit[i] = False


for i in range(1, N):
    comb = list(combinations(C, i))
    for n in range(len(comb)):
        temp_r = 1
        temp_p = 0
        for j in range(i):
            temp_r *= R[comb[n][j]]
            temp_p += P[comb[n][j]]
        if diff > abs(temp_r-temp_p):
            diff = abs(temp_r-temp_p)
            cnt = i

print(N-cnt)
