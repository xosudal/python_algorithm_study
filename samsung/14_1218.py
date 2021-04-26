import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    ans = 1
    _len = int(input())
    _list = list(input())
    stack = list()
    for s in _list:
        if s == '(' or s == '{' or s == '<' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack.pop() != '(':
                ans = 0
                break
        elif s == '}':
            if stack.pop() != '{':
                ans = 0
                break
        elif s == ']':
            if stack.pop() != '[':
                ans = 0
                break
        elif s == '>':
            if stack.pop() != '<':
                ans = 0
                break
    print(f'#{test_case} {ans}')
