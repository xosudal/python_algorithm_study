import sys

sys.stdin = open("input.txt", "r")

direction = [
    [0, 0],
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0]
]

for tc in range(1, int(input())+1):
    M, A = map(int, input().split())
    dir_a = list(map(int, input().split()))
    dir_b = list(map(int, input().split()))
    dir_a.insert(0, 0)
    dir_b.insert(0, 0)
    AP = []
    for _ in range(A):
        x, y, c, p = list(map(int, input().split()))
        AP.append([x, y, c, p])
    AP.sort(key=lambda k: k[3], reverse=True)
    a = [1, 1]
    b = [10, 10]
    bat = 0
    for m in range(M+1):
        na = [a[0] + direction[dir_a[m]][0], a[1] + direction[dir_a[m]][1]]
        nb = [b[0] + direction[dir_b[m]][0], b[1] + direction[dir_b[m]][1]]
        a, b = na, nb
        bc_a = []
        bc_b = []
        for i in range(A):
            diff_a = abs(na[0]-AP[i][0]) + abs(na[1]-AP[i][1])
            diff_b = abs(nb[0]-AP[i][0]) + abs(nb[1]-AP[i][1])

            if diff_a <= AP[i][2]:
                bc_a.append([i, AP[i][3]])

            if diff_b <= AP[i][2]:
                bc_b.append([i, AP[i][3]])

        maxB = 0
        if bc_a and bc_b:
            if bc_a[0][0] == bc_b[0][0]:
                if len(bc_a) > 1:
                    maxB = max(maxB, bc_a[1][1] + bc_b[0][1])
                if len(bc_b) > 1:
                    maxB = max(maxB, bc_a[0][1] + bc_b[1][1])
            else:
                maxB = max(maxB, bc_a[0][1] + bc_b[0][1])

        if bc_a:
            maxB = max(maxB, bc_a[0][1])

        if bc_b:
            maxB = max(maxB, bc_b[0][1])

        bat += maxB

    print(f'#{tc} {bat}')