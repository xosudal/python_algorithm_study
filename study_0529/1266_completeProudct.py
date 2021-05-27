import math
import sys
sys.stdin = open("input.txt", "r")
P = [2,3,5,7,11,13,17]

for tc in range(1, int(input())+1):
    N = 18
    t1, t2 = map(int, input().split())
    a, b = float(t1)/100.0, float(t2)/100.0
    r1 = 0
    r2 = 0
    for p in P:
        r1 += math.factorial(18) / (math.factorial(p) * math.factorial(18-p)) * pow(a, p) * pow(1-a, 18-p)
        r2 += math.factorial(18) / (math.factorial(p) * math.factorial(18-p)) * pow(b, p) * pow(1-b, 18-p)
    print(f'#{tc}', format(r1+r2-r1*r2,".6f"))
