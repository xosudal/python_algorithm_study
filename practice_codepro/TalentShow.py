N, S, M = map(int, input().split())

E = [i for i in range(1, N+1)]

cur = S-1

R = []

while E:
    cur = (cur+M-1)%len(E)
    R.append(E.pop(cur))

print(*R)

# for _ in range(N-1):
#     t = 0
#     while t < M-1:
#         cur = (cur+1)%N
#         if E[cur] > 0:
#             t += 1
#     print(E[cur], end=' ')
#     E[cur] = 0
#     cur = (cur+1)%N
#     while E[cur] <= 0:
#         cur = (cur + 1) % N
#
# for e in E:
#     if e != 0:
#         print(e)