import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def rotate(N, m):
    # 0
    for i in range(0, N, m):
        result.append(''.join(graph[i:i+m]))

    for _ in range(m-1):
        temp = graph.pop(0)
        graph.append(temp)
        for i in range(0, N, m):
            result.append(''.join(graph[i:i+m]))


for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    graph = list(input())
    m = int(N/4)

    result = list()
    rotate(N, m)
    result_set = set(result)
    result_set = list(result_set)
    result_set.sort(reverse=True)
    print(ord('A'))
    print(f'#{tc} {int(result_set[K-1],16)}')
