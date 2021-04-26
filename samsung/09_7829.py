import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    P = int(input())
    _list = list(map(int, input().split()))
    _list.sort()
    print("#" + str(test_case) + " ", end='')
    print(_list[0]*_list[-1])
