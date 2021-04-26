N = int(input())
E = list()
for _ in range(N):
    E.append(list(map(int, input().split())))

E.sort(key=lambda x: x[1])

e_cnt = 1
e_val = E[0][1]

for i in range(1, len(E)):
    if E[i][0] > e_val:
        e_cnt += 1
        e_val = E[i][1]

print(e_cnt)
