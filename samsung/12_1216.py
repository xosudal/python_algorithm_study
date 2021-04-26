import sys

sys.stdin = open("input.txt", "r")

T = 10

def check(_str):
    _len = len(_str)
    for i in range(0, int(_len / 2)):
        if _str[i] != _str[_len - i - 1]:
            return False
    return True


for test_case in range(1, T + 1):
    cnt = 0
    tc = int(input())
    graph = list()
    for _ in range(100):
        graph.append(list(input()))
    graph2 = list(map(list, zip(*graph)))
    ans = 0
    for _len in range(100):
        for i in range(100):
            for j in range(100-_len+1):
                if check(graph[i][j:j+_len]):
                    ans = _len
                if check(graph2[i][j:j+_len]):
                    ans = _len

    print(f"#{tc} {ans}")
