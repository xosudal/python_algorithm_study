for tc in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    D = dict()
    for d in arr:
        if d not in D:
            D[d] = 0
        D[d] += 1
    for a, cnt in D.items():
        b = a^x
        if b not in D: continue
        if b < a: continue
        if a == b:
            ans += cnt * (cnt-1) // 2
        else:
            ans += cnt * D[b]

    print(ans)
