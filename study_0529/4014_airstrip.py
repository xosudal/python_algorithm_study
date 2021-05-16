import sys

sys.stdin = open("input.txt", "r")


def check(air):
    visit = [0] * N
    for i in range(N - 1):
        if air[i] == air[i + 1]:
            continue
        if abs(air[i] - air[i + 1]) > 1:
            return 0

        if air[i] == air[i + 1] + 1:  # 아래
            j = i + 1
            cnt = 1
            while j < N-1:
                if air[j] == air[j+1]:
                    j += 1
                    cnt += 1
                else:
                    break
            if cnt >= X:
                for c in range(i+1, i+1+X):
                    visit[c] = 1
            else:
                return 0
    for i in range(N-1, 0, -1):
        if air[i] == air[i-1]:
            continue

        if abs(air[i]-air[i-1]) > 1:
            return 0

        if air[i] == air[i-1] + 1:
            j = i-1
            cnt = 1
            while j > 0:
                if air[j] == air[j-1]:
                    j -= 1
                    cnt += 1
                else:
                    break
            if cnt >= X:
                for c in range(i-1, i-1-X, -1):
                    if c == -1:
                        print("fuck", j)
                    if visit[c] == 1:
                        return 0
                    visit[c] = 1
            else:
                return 0
    print(visit)
    return 1


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    #temp = [3,3,3,2,2,2]
    #print(check(temp))
    ans = 0
    for m in maps:
        #print(check(m))
        ans += check(m)
    for m in zip(*maps):
        #print(check(m))
        ans += check(m)
    print(f'#{tc} {ans}')
