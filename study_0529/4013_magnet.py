import sys

sys.stdin = open("input.txt", "r")

def rotate(m, clock):
    if clock == 1:
        temp = m.pop(7)
        m.insert(0, temp)
    elif clock == -1:
        temp = m.pop(0)
        m.append(temp)

def check(idx, c, dir):
    # 1 <= idx <= 4 dir: -1 left // 1 right
    if dir == 1 and idx <= 3:
        if M[idx][2] != M[idx+1][6]:
            temp.append([idx+1, c*-1])
            check(idx+1, c * -1, dir)

    elif dir == -1 and idx >= 2:
        if M[idx][6] != M[idx-1][2]:
            temp.append([idx-1, c*-1])
            check(idx-1, c * -1, dir)


for tc in range(1, int(input()) + 1):
    K = int(input())
    M = [list(map(int, input().split())) for _ in range(4)]
    M.insert(0, [])
    r_list = [list(map(int, input().split())) for _ in range(K)]

    for idx, c in r_list:
        temp = [[idx, c]]
        check(idx, c, 1)
        check(idx, c, -1)
        for i, clock in temp:
            rotate(M[i], clock)
    ans = 0
    for i in range(1, 5):
        if M[i][0] == 1:
            ans += 2 ** (i-1)

    print(f'#{tc} {ans}')
