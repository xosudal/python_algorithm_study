# n, m, k = list(map(int, input().split()))
n, m, k = [5, 8, 3]
# input_arr = list(map(int, input().split()))
input_arr = [2, 4, 5, 4, 6]
first = max(input_arr)
input_arr.remove(first)
second = max(input_arr)
result = 0
for i in range(1, m + 1):
    if i % (k+1) == 0:
        print("second", i)
        result += second
    else:
        print("first", i)
        result += first
print(result)
