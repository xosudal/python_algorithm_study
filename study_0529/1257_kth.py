import sys
sys.stdin = open("input.txt", "r")


for tc in range(1, int(input())+1):
    K = int(input())
    S = input()
    temp = []
    s_set = set()
    for i in range(len(S)):
        temp.append(S[i:])

    for t in temp:
        for i in range(len(t)):
            s_set.add(t[:i+1])
    res = list(s_set)
    res.sort()
    print(f'#{tc} {res[K-1]}')
