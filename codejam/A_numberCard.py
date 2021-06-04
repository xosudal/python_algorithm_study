for tc in range(int(input())):
    _input = list(map(int, input().split()))
    if _input[5] > 0:
        _input[8] += _input[5]
        _input[5] = 0

    arr = []
    for i in range(len(_input)-1, -1, -1):
        for j in range(_input[i]):
            arr.append(i+1)
    arr_copy = arr[:]
    left = []

    for i in range(0, len(arr), 2):
        left.append(arr_copy[i])
        arr.remove(arr_copy[i])
    arr.sort()
    print(*(left + arr))