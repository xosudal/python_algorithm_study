import sys
sys.stdin = open("input.txt", "r")

'''
문제 발견함
이동 완료 후 대기중이던 사람은 바로 내려가기 시작해야됨
아래 로직은 대기중이던 사람은 그 다음턴에 내려가게 되어 잇음
'''
def comb(arr, r):
    res = []
    if r == 0:
        return [[]]
    for i in range(len(arr)):
        t = arr[i]
        for c in comb(arr[i + 1:], r - 1):
            res.append([t] + c)
    return res


def move():
    first_group = [[i, abs(first[i][0]-E[0][0])+abs(first[i][1]-E[0][1]), 0] for i in range(len(first))]
    second_group = [[i, abs(second[i][0]-E[1][0])+abs(second[i][1]-E[1][1]), 0] for i in range(len(second))]
    first_group.sort(key=lambda k: k[1])
    second_group.sort(key=lambda k: k[1])
    # first_group = deque(first_group)
    # second_group = deque(second_group)
    time = 0
    complete = []
    first_stair = []
    second_stair = []
    while True:
        if len(complete) == len(people):
            break
        #print("complete :", len(complete), len(people))
        time += 1
        #print("time :", time)
        if first_stair:
            for f in first_stair:
                f[2] += 1
            for f in first_stair[:]:
                if f[2] == E[0][2] + 1:
                    first_stair.remove(f)
                    complete.append(f)

        if second_stair:
            for f in second_stair:
                f[2] += 1
            for f in second_stair[:]:
                if f[2] == E[1][2] + 1:
                    second_stair.remove(f)
                    complete.append(f)
        print("first stair :", first_stair)
        print("second stair :", second_stair)
        if first_group:
            for f in first_group[:]:
                if f[1] <= time and len(first_stair) < 3:
                    first_stair.append(f)
                    first_group.remove(f)

        if second_group:
            for f in second_group[:]:
                if f[1] <= time and len(second_stair) < 3:
                    second_stair.append(f)
                    second_group.remove(f)
        # while first_group:
        #     if first_group[0][1] <= time and len(first_stair) < 3:
        #         first_stair.append(first_group.popleft())
        #     else:
        #         break
        #
        # while second_group:
        #     if second_group[0][1] <= time and len(second_stair) < 3:
        #         second_stair.append(second_group.popleft())
        #     else:
        #         break
    return time


for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    people = []
    E = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                people.append([i, j])
            if maps[i][j] > 1:
                E.append([i, j, maps[i][j]])
    people_idx = [i for i in range(len(people))]
    ans = 2**42

    for i in range(0, len(people)+1):
        temp = comb(people_idx, i)
        for j in range(len(temp)):
            first_idx = temp[j]
            second_idx = list(set(people_idx)-set(first_idx))
            first = [people[f] for f in first_idx]
            second = [people[s] for s in second_idx]
            m = move()
            if m == 18:
                print("first :",first)
                print("second :",second)
            ans = min(m, ans)

    print(f'#{tc} {ans}')