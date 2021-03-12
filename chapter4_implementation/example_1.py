# page 110
n = input()

data = list(map(str, input().split()))
x = 1
y = 1

for s in data:
    if s == 'R':
        if 1 <= y+1 <= int(n):
            y += 1
    elif s == 'L':
        if 1 <= y - 1 <= int(n):
            y -= 1
    elif s == 'D':
        if 1 <= x + 1 <= int(n):
            x += 1
    else:
        if 1 <= x - 1 <= int(n):
            x -= 1
print(x, y)
