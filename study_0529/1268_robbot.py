import sys
sys.stdin = open("input.txt", "r")


def GCD(a, b):
    if a < b:
        return GCD(b, a)
    elif b == 0:
        return a
    else:
        return GCD(b, a % b)


for tc in range(1, int(input())+1):
    R, N, K = map(int, input().split())
    maps = [[0] * (R+1) for _ in range(R+1)]
    Robot = []
    for _ in range(N):
        x, y = map(int, input().split())
        maps[x][y] = 1
        Robot.append([x, y])
    Robot.insert(0, [])
    ans = 0
    A = [0] * (2*N+1)
    B = [0] * (2*N+1)
    C = [0] * (N+1)
    for start in range(1, N+1):
        temp = set()
        for end in range(1, N+1):
            if start != end:
                dx = Robot[start][0] - Robot[end][0]
                dy = Robot[start][1] - Robot[end][1]
                gcd = GCD(abs(dx), abs(dy))
                temp.add((dx/gcd, dy/gcd))
        A[start] = len(temp)
        ans += len(temp)

    for i in range(1, N+1):
        for j in range(1, N+1):
            A[j] = ((A[j]*K+j)%N)+1
            A[N+j] = ((A[j]*j+K)%N)+1
        A.sort()
        B[0] = 1
        for j in range(1, 2*N+1):
            B[j] = ((B[j-1] * A[j] + j)%N) + 1
        C[i] = B[2*N]
    print(f'#{tc} {ans} {sum(C)}')