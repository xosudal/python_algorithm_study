import sys

N, L, M = map(int, input().split())

FILTER = []

for _ in range(M):
    FILTER.append(list(map(int, input().split())))


def count_virus(w1, w2, h1, h2):
    cnt = 0
    for x, y in FILTER:
        if w1 <= x <= w2 and h1 <= y <= h2:
            cnt += 1
    return cnt


result = -sys.maxsize

for width in range(1, L // 2):
    height = L // 2 - width
    for x, y in FILTER:
        # result = max(result, count_virus(x, x + width, y, y+height))
        for offset in range(height + 1):
            result = max(result, count_virus(x, x + width, y - offset, y + height - offset))

print(result)
