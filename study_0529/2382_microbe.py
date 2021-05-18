import sys

sys.stdin = open("input.txt", "r")

d = [
    [],
    [-1, 0],  # 상
    [1, 0],  # 하
    [0, -1],  # 좌
    [0, 1]   # 우
]


def change_dir(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3


def move():
    for time in range(M):

        # 다음 셀로 이동
        for m in micro:
            m[0], m[1] = m[0] + d[m[3]][0], m[1] + d[m[3]][1]
            check[m[0]][m[1]] += 1

        # 약품이 칠해진 셀에 도착하면 절반이 죽고 이동방향 반대
        for m in micro[:]:
            if m[0] == 0 or m[0] == N-1 or m[1] == 0 or m[1] == N-1:
                micro.remove(m)
                if int(m[2]/2) != 0:
                    micro.append([m[0], m[1], int(m[2]/2), change_dir(m[3])])
                else:
                    check[m[0]][m[1]] -= 1
        # 두 개 이상이 한 셀에 모이게 되는 경우 합쳐짐
        # 가장 많은 놈의 d 로 되고 미생물 다 더하면 됨
        for i in range(N):
            for j in range(N):
                if check[i][j] > 1:
                    temp = []
                    for m in micro[:]:
                        if m[0] == i and m[1] == j:
                            micro.remove(m)
                            temp.append(m)
                    temp.sort(key=lambda k: -k[2])
                    k = 0
                    for t in temp:
                        k += t[2]
                    micro.append([i, j, k, temp[0][3]])
        for m in micro:
            check[m[0]][m[1]] = 0


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]  # y, x, k, d
    check = [[0] * N for _ in range(N)]
    ans = 0
    move()
    for m in micro:
        ans += m[2]
    print(f'#{tc} {ans}')
