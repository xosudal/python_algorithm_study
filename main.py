import sys

sys.stdin = open("input.txt", "r")
graph = list()

for _ in range(4):
    graph.append(list(input()))
a = list(zip(*graph))
print(a[0])
