def check(num):
    t = int(num**(1/2))
    for a in range(2, t+1):
        if num % a == 0:
            return False
    return True

P = [2, 3]

i = 5
cnt = 0
while cnt < 250:
    if check(i):
        cnt += 1
        P.append(i)
    i += 1

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    ans = 2**43
    data.sort()
    for i in range(len(P)):
        total, c = 0, 0
        for j in range(len(data)):
            total += abs(data[j]-P[i+j])
            if data[j] <= P[i+j]:
                c += 1
        ans = min(ans, total)
        if c == n:
            break
    print(ans)