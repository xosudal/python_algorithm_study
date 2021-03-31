import sys
N = int(input())

arr = list(map(int, input().split()))

start = 0
end = N-1
ans_start = N-1
ans_end = 0
diff = sys.maxsize

while start < end:
    d = arr[start] + arr[end]
    if diff > abs(d):
        diff = abs(d)
        ans_start = start
        ans_end = end

    elif diff == abs(d):
        if ans_start > start:
            ans_start = start
            ans_end = end

    if d >= 0:
        end -= 1
    else:
        start += 1

print(ans_start, ans_end)
