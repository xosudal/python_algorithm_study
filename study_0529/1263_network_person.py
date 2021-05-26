import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    adj = []

    for i in range(N):
        adj.append(temp[N*i+1:N*(i+1)+1])
    for a in adj:
        print(a)
    print(f'#{tc}')