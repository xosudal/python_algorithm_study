import sys
N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

visit = [sys.maxsize * N for _ in range(N)]

