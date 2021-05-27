import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    N, P = map(int, input().split())
    n = N // P
    m = N % P
    cal = [n for _ in range(P)]
    for i in range(P):
        if m != 0:
            cal[i] += 1
            m -= 1
        else:
            break

    res = 1
    for c in cal:
        res *= c
    print(f'#{tc} {res}')
