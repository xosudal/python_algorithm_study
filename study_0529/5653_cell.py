from collections import deque
import sys

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Cell:
    def __init__(self, n, m, size, life):
        self.n = n
        self.m = m
        self.size = size
        self.life = life

    def __str__(self):
        return f'{self.n}, {self.m}, {self.size}, {self.life}'


for tc in range(1, int(input()) + 1):
    N, M, K = list(map(int, input().split()))
    cell_check = [[0] * 401 for _ in range(401)]
    non_active = deque()
    active = deque()
    for n in range(N):
        temp = list(map(int, input().split()))
        for m in range(M):
            if temp[m] != 0:
                non_active.append(Cell(175+n, 175+m, temp[m], temp[m]))
                cell_check[175 + n][175 + m] = 1

    breed = list()
    breed_map = [[0] * 401 for _ in range(401)]
    for k in range(K):
        na_len = len(non_active)
        a_len = len(active)

        breed = list(set(breed))

        while breed:
            n, m = breed.pop(0)
            non_active.append(Cell(n, m, breed_map[n][m], breed_map[n][m]))
            cell_check[n][m] = 1

        for i in range(na_len):
            na = non_active.popleft()
            na.life -= 1

            if na.life == 0:
                active.append(Cell(na.n, na.m, na.size, na.size))
                for j in range(4):
                    nn, nm = na.n + dx[j], na.m + dy[j]
                    if cell_check[nn][nm]:
                        continue
                    if breed_map[nn][nm] < na.size:
                        breed_map[nn][nm] = na.size
                        breed.append((nn, nm))
            else:
                non_active.append(na)

        for i in range(a_len):
            a = active.popleft()
            a.life -= 1
            if a.life != 0:
                active.append(a)
    print(f'#{tc} {len(active) + len(non_active)}')
