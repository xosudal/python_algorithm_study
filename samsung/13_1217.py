import sys
sys.stdin = open("input.txt", "r")

T = 10

def my_pow(_num, _p):
    if _p == 0:
        return 1
    else:
        return _num * my_pow(_num, _p-1)


for test_case in range(1, T + 1):
    tc = int(input())
    num, p = list(map(int, input().split()))
    print(f"#{tc} {my_pow(num, p)}")
