import sys
sys.stdin = open("input.txt", "r", encoding='UTF8')

T = 10

for test_case in range(1, T + 1):
    cnt = 0
    tc = int(input())
    s = input()
    _input = input()
    for i in range(len(_input)):
        if s[0] == _input[i]:
            if s == _input[i:(i+len(s))]:
                cnt += 1
    print("#" + str(test_case) + " ", end='')
    print(cnt)
    # print(_input.count(s))
