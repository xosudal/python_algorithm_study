import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    _input = list(map(int, input().split()))
    X = _input[:N]
    G = _input[N:]
    print(f'#{tc} ', end='')
    for i in range(N-1):
        left, right = X[i], X[i+1]
        while right - left >= 1e-12:
            mid = (left+right)/2
            l, r = 0, 0
            for i in range(N):
                temp = G[i]/(mid-X[i])**2
                if X[i] < mid:
                    l += temp
                else:
                    r += temp
            if l < r:
                right = mid
            else:
                left = mid
        print(format(mid, ".10f"), end=' ')
    print()
