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
    _len = int(input())
    graph = list()
    for _ in range(100):
        graph.append(list(map(str, input())))

    for i in range(100):
        for j in range(100-_len+1):
            row = ""
            col = ""
            for k in range(j, j+_len):
                row += graph[i][k]
                #print(k, i)
                col += graph[k][i]
            if check(row):
                cnt += 1
            if check(col):
                cnt += 1

    print("#" + str(test_case) + " ", end='')
    print(cnt)
