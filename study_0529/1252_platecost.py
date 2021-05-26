import sys
sys.stdin = open("input.txt", "r")

# 2 4 7


def check(x, y, size):
    cnt = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if maps[i][j] == 1:
                cnt += 1
    return cnt


def makeZero(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            maps[i][j] = 0


def plate():
    global ans
    for s in range(9, 4, -1):
        for i in range(1, S-1):
            for j in range(1, S-1):
                c = check(i, j, 3)
                if c == s:
                    ans+=1
                    makeZero(i, j, 3)
                    plate_list.append(i)
                    plate_list.append(j)
                    plate_list.append(3)

    for s in range(4, 1, -1):
        for i in range(1, S):
            for j in range(1, S):
                c = check(i, j, 2)
                if c == s:
                    ans += 1
                    makeZero(i, j, 2)
                    plate_list.append(i)
                    plate_list.append(j)
                    plate_list.append(2)

    for i in range(1, S+1):
        for j in range(1, S+1):
            if maps[i][j] == 1:
                ans += 1
                maps[i][j] = 0
                plate_list.append(i)
                plate_list.append(j)
                plate_list.append(1)


for tc in range(1, int(input())+1):
    S = int(input())
    maps = [[0]*(S+1) for _ in range(S+1)]
    D = int(input())
    d_in = list(map(int, input().split()))
    plate_list = []
    for i in range(D):
        maps[d_in[i*2]][d_in[2*i+1]] = 1
    ans = 0
    plate()
    print(f'#{tc} {ans}', *plate_list)
