N = int(input())
B = list()
for _ in range(N):
    B.append(int(input()))

stack = list()

ans = 0

for i in range(N):
    while stack and stack[-1] <= B[i]:
        stack.pop()
    ans += len(stack)
    stack.append(B[i])

print(ans)
