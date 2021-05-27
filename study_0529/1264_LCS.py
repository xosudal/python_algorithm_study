import sys
sys.stdin = open("input.txt", "r")
# https://mygumi.tistory.com/126
for tc in range(1, int(input())+1):
    N = int(input())

    LCS = [[0] * (N+1) for _ in range(N+1)]
    A = input()
    B = input()

    for i in range(N):
        for j in range(N):
            if A[i] == B[j]:
                LCS[i+1][j+1] = LCS[i][j] + 1
            else:
                LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])
    ans = LCS[N][N]/N*100
    print(f'#{tc}', format(ans, ".2f"))