import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    screw = []
    temp = list(map(int, input().split()))
    for i in range(N):
        screw.append([temp[2*i], temp[2*i+1]])

    res = []

    for i in range(N):
        b = 0
        cur = screw[i]
        res.append(screw[i][0])
        res.append(screw[i][1])
        while 1:
            found = 0
            for s in screw:
                if s[0] == cur[1]:
                    cur = s
                    res.append(s[0])
                    res.append(s[1])
                    found = 1
                    break
            if len(res) == N*2:
                b = 1
                break
            if found == 0:
                res.clear()
                break
        if b == 1:
            break
    print(f'#{tc}', *res)