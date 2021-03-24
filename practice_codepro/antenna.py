N = int(input())

ANT = list(map(int, input().split()))

stack = list()
cnt = 0
for i in range(N):
    while stack and stack[-1] < ANT[i]:
        stack.pop()
        cnt += 1
        print("after pop ", stack, "cnt : ", cnt)
    if stack:
        if stack[-1] == ANT[i]:
            stack.pop()
        cnt += 1
        print("in stack ", stack)
    stack.append(ANT[i])
    print("after push ", stack)

print(cnt)
