import sys

T = 10
sys.stdin = open("input.txt", "r")

def check(_str):
    if _str == '*' or _str == '/' or _str == '+' or _str == '-':
        return True
    else:
        return False


for test_case in range(1, T + 1):
    ans = 1
    N = int(input())
    for _ in range(N):
        _tree = list(map(str, input().split()))
        if len(_tree) == 4:
            if not check(_tree[1]):
                ans = 0
        else:
            if check(_tree[1]):
                ans = 0
    print("#" + str(test_case) + " ", end='')
    print(ans)
