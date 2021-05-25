import sys
sys.stdin = open("input.txt", "r")
max_cpu = 5


def process(p_cnt, cpu_cnt):
    if p_cnt == N:
        return 1

    wait_time = [0] * max_cpu

    for i in range(cpu_cnt):
        arrived, p_len = P[p_cnt]
        if arrived <= C[i]:
            wait_time[i] = C[i] - arrived
    temp = wait_time[:]
    temp.insert(0, p_cnt)
    save = tuple(temp)
    if save in Memo:
        if Memo[save] == cpu_cnt:
            return 0
    Memo[save] = cpu_cnt

    for i in range(cpu_cnt):
        if wait_time[i] + P[p_cnt][1] > 10:
            continue
        temp = C[i]
        C[i] = wait_time[i] + P[p_cnt][0] + P[p_cnt][1]
        if process(p_cnt+1, cpu_cnt) == 1:
            C[i] = temp
            return 1
        C[i] = temp
    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    C = [0] * max_cpu
    ans = -1
    Memo = dict()
    for cpu in range(1, 6):
        if process(0, cpu) == 1:
            ans = cpu
            break

    print(f'#{tc} {ans}')