import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    K = int(input())
    S = input()
    arr = []
    for i in range(len(S)):
        arr.append(S[i:])
    arr.sort()
    print(f'#{tc} {arr[K-1]}')
