import sys

T = 10
sys.stdin = open("input.txt", "r")

def cal(idx, _list):

    if _list[idx][1] != '*' and _list[idx][1] != '/' and _list[idx][1] != '+' and _list[idx][1] != '-':
        return int(_list[idx][1])

    left = cal(int(_list[idx][2]), _list)
    right = cal(int(_list[idx][3]), _list)
    if _list[idx][1] == '*':
        return left*right
    elif _list[idx][1] == '/':
        return left/right
    elif _list[idx][1] == '+':
        return left+right
    elif _list[idx][1] == '-':
        return left-right


for test_case in range(1, T + 1):
    N = int(input())
    _list = [list()] * (N+1)
    for i in range(1, N+1):
        _list[i] = list(map(str, input().split()))
    print("#" + str(test_case) + " ", end='')
    print(round(cal(1, _list)))
