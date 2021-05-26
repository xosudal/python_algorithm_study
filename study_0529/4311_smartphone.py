import sys
sys.stdin = open("input.txt", "r")

def cal(a, b, op):
    if op == 1:
        return a + b
    elif op == 2:
        return a - b
    elif op == 3:
        return a * b
    elif op == 4:
        if b == 0:
            return -1
        return a // b

def touch():
    # 계산 없이
    if W in num:
        return num_cnt[W]

    # 계산 해서
    num_copy = num[:]
    while num_copy:
        temp = set()
        for x in num_copy:
            for y in num:
                for op in op_input:
                    res = cal(x, y, op)
                    if res > 999 or res < 0:
                        continue
                    cnt = num_cnt[x] + num_cnt[y] + 1  # op
                    if cnt > M: continue
                    if cnt < num_cnt[res]:
                        num_cnt[res] = cnt
                        temp.add(res)
        num_copy = temp
    if num_cnt[W] + 1 > M:
        return -1
    return num_cnt[W] + 1


for tc in range(1, int(input())+1):
    N, O, M = map(int, input().split())
    num_input = list(map(int, input().split()))
    op_input = list(map(int, input().split()))
    W = int(input())
    num_cnt = [M+1] * 1000
    num = []
    for i in num_input:
        if i == 0:
            num_cnt[i] = 1
            num.append(i)
            continue
        num_cnt[i] = 1
        num.append(i)
        for j in num_input:
            n = 10*i + j
            num.append(n)
            num_cnt[n] = 2
            for k in num_input:
                n = 100*i + 10*j + k
                num.append(n)
                num_cnt[n] = 3

    print(f'#{tc} {touch()}')
