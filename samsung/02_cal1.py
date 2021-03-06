import sys

T = 10
sys.stdin = open("input.txt", "r")

for test_case in range(1, T + 1):
    _len = int(input())
    _str = input()
    result = list()
    stack = list()
    for s in _str:
        if s == '+':
            stack.append(s)
        else:
            result.append(s)

    while stack:
        result.append(stack.pop())

    for i in result:
        if i == '+':
            p1 = stack.pop()
            p2 = stack.pop()
            temp = int(p1) + int(p2)
            stack.append(str(temp))
        else:
            stack.append(i)

    print("#" + str(test_case) + " ", end='')
    print(stack[0])
